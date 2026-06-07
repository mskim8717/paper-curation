// Cloudflare Worker entry — serves static assets from docs/ via the
// ASSETS binding, and intercepts POST /api/audio-email to forward the
// generated MP3 to Resend for email delivery.
//
// Secrets (set via `npx wrangler secret put <NAME>`):
//   RESEND_API_KEY  — Resend API key (re_xxx). Required.
//   AUDIO_REPLY_TO  — Optional. Reply-To header (e.g. "jehyun.lee@gmail.com")
//                      so visitors' replies land in the operator's inbox even
//                      though the From: stays on resend.dev.
//   AUDIO_FROM      — Optional. Override "From:" address. Defaults to
//                      "Paper Curation <onboarding@resend.dev>" (Resend's
//                      shared sandbox sender — only delivers to the Resend
//                      account email until a custom domain is verified).
//
// Limits:
//   - 25 MB request body (Resend attachment cap), 10 recipients max.
//   - One Resend call per recipient (Resend free tier: 100 mails/day).

const DEFAULT_FROM = "Paper Curation <onboarding@resend.dev>";
const MAX_ATTACHMENT_BYTES = 25 * 1024 * 1024;
const MAX_RECIPIENTS = 10;

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

function bytesToBase64(bytes) {
  // Workers runtime has btoa but it expects a binary string. Build it in
  // 32 KB chunks so we don't blow the call-stack on multi-MB attachments.
  let s = "";
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) {
    s += String.fromCharCode.apply(null, bytes.subarray(i, i + chunk));
  }
  return btoa(s);
}

async function handleAudioEmail(request, env) {
  if (!env.RESEND_API_KEY) {
    return new Response("RESEND_API_KEY not configured on Worker", { status: 503 });
  }

  let form;
  try {
    form = await request.formData();
  } catch (e) {
    return new Response("Invalid form data", { status: 400 });
  }

  const recipients = form.getAll("email")
    .map(v => String(v).trim())
    .filter(v => EMAIL_RE.test(v));
  if (!recipients.length) {
    return new Response("No valid recipient", { status: 400 });
  }
  if (recipients.length > MAX_RECIPIENTS) {
    return new Response(`Too many recipients (max ${MAX_RECIPIENTS})`, { status: 400 });
  }

  const file = form.get("mp3");
  if (!file || typeof file === "string") {
    return new Response("Missing mp3 attachment", { status: 400 });
  }
  const buf = await file.arrayBuffer();
  if (buf.byteLength > MAX_ATTACHMENT_BYTES) {
    return new Response("Attachment too large", { status: 413 });
  }
  const b64 = bytesToBase64(new Uint8Array(buf));

  const filename = String(form.get("filename") || file.name || "audio-overview.mp3");
  const title = String(form.get("title") || "Audio Overview");
  const lang = String(form.get("lang") || "ko");
  const isKo = lang === "ko";

  const subject = isKo
    ? `[Paper Curation] Audio Overview: ${title}`
    : `[Paper Curation] Audio Overview: ${title}`;
  const html = isKo
    ? `<p>요청하신 Audio Overview 가 첨부되어 있습니다.</p>
       <p><b>제목</b>: ${escapeHtml(title)}</p>
       <p>이 메일은 Paper Curation 의 자동 발송입니다. 답장은 운영자에게 전달됩니다.</p>`
    : `<p>Your requested Audio Overview is attached.</p>
       <p><b>Title</b>: ${escapeHtml(title)}</p>
       <p>This is an automated message from Paper Curation. Replies route to the operator.</p>`;

  const payloadBase = {
    from: env.AUDIO_FROM || DEFAULT_FROM,
    subject,
    html,
    attachments: [{ filename, content: b64 }],
  };
  if (env.AUDIO_REPLY_TO) payloadBase.reply_to = env.AUDIO_REPLY_TO;

  const results = await Promise.all(recipients.map(async (to) => {
    const payload = { ...payloadBase, to: [to] };
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    const text = await r.text();
    return { to, ok: r.ok, status: r.status, body: text.slice(0, 400) };
  }));

  const anyFail = results.some(r => !r.ok);
  const status = anyFail ? 502 : 200;
  return new Response(JSON.stringify({ results }), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/audio-email") {
      if (request.method !== "POST") {
        return new Response("Method Not Allowed", {
          status: 405,
          headers: { "Allow": "POST" },
        });
      }
      return handleAudioEmail(request, env);
    }
    // Everything else falls through to the static-assets binding.
    return env.ASSETS.fetch(request);
  },
};
