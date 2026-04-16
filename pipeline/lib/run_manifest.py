"""
Per-run manifest writer.

Each `run_update_force.py` invocation produces `pipeline/_runs/{ts}.json`
recording mode/source/images/duration/per-step success-fail/file changes.
Used for sanity tracking and post-incident debugging.
"""

import json
import os
import socket
import sys
from datetime import datetime
from pathlib import Path

from .atomic_io import atomic_write_json

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PIPELINE_ROOT / "_runs"


class RunManifest:
    def __init__(self, mode, topic, **kwargs):
        self.start_iso = datetime.now().isoformat(timespec="seconds")
        self.start_t = datetime.now().timestamp()
        self.data = {
            "start": self.start_iso,
            "host": socket.gethostname(),
            "python": sys.version.split()[0],
            "mode": mode,
            "topic": topic,
            "argv": sys.argv,
            "kwargs": {k: v for k, v in kwargs.items()
                       if isinstance(v, (str, int, float, bool, list, dict, type(None)))},
            "steps": [],
            "files_changed": {"created": 0, "modified": 0, "deleted": 0},
            "errors": [],
        }

    def step(self, name, status, duration_s=None, detail=None):
        self.data["steps"].append({
            "name": name,
            "status": status,
            "duration_s": round(duration_s, 2) if duration_s else None,
            "detail": detail,
        })

    def error(self, where, msg):
        self.data["errors"].append({"where": where, "msg": str(msg)[:400]})

    def file_change(self, kind, n=1):
        if kind in self.data["files_changed"]:
            self.data["files_changed"][kind] += n

    def save(self):
        self.data["end"] = datetime.now().isoformat(timespec="seconds")
        self.data["duration_s"] = round(datetime.now().timestamp() - self.start_t, 1)
        ts_safe = self.start_iso.replace(":", "").replace("-", "")
        out = RUNS_DIR / f"{ts_safe}_{self.data.get('mode','run')}.json"
        atomic_write_json(out, self.data)
        return out
