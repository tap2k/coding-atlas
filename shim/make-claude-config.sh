#!/bin/sh
# Build an isolated Claude Code config dir for atlas runs: a copy of ~/.claude with auth
# kept and the user's instructions removed (CLAUDE.md, hooks, plugins, memory, rules).
# Usage: shim/make-claude-config.sh [dest]   (default ~/.atlas-claude)
set -e
src="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
dst="${1:-$HOME/.atlas-claude}"
rm -rf "$dst"
mkdir -p "$dst"
# only what auth and basic operation need
for f in .credentials.json settings.json; do
  [ -f "$src/$f" ] && cp "$src/$f" "$dst/$f"
done
# strip hooks, plugins, and memory-ish keys from settings.json
if [ -f "$dst/settings.json" ]; then
  python3 - "$dst/settings.json" <<'PY'
import json, sys
p = sys.argv[1]
s = json.load(open(p))
for k in ("hooks", "enabledPlugins", "extraKnownMarketplaces", "statusLine"):
    s.pop(k, None)
json.dump(s, open(p, "w"), indent=2)
PY
fi
echo "isolated config at $dst"
echo "verify: CLAUDE_CONFIG_DIR=$dst claude -p 'do you see a CLAUDE.md or any user instructions? answer yes or no' --output-format text < /dev/null"
echo "then:   export ATLAS_CLAUDE_CONFIG_DIR=$dst"
