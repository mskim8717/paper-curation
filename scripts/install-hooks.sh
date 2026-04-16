#!/bin/sh
# Install paper-curation git hooks.
# Usage: bash scripts/install-hooks.sh

set -e
ROOT="$(git rev-parse --show-toplevel)"
HOOKS="$ROOT/.git/hooks"
mkdir -p "$HOOKS"
cp "$ROOT/scripts/pre-push" "$HOOKS/pre-push"
chmod +x "$HOOKS/pre-push"
echo "Installed: $HOOKS/pre-push"
echo "Override per-push with: git push --no-verify"
