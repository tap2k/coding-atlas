#!/bin/sh
# Generic PATH shim. Logs the call as one JSON line to $ATLAS_TRACE, then execs the
# real binary found further down PATH. Installed by the runner as a symlink per command.
# Pure sh: anything it calls (sed, date) could itself be shimmed, so use builtins only.
name=$(basename "$0")
NL=$(printf '\n_'); NL=${NL%_}; TAB=$(printf '\t')
esc() { s=$1; o=""; while [ -n "$s" ]; do c=${s%"${s#?}"}; s=${s#?}
  case $c in '"') o="$o\\\"";; '\') o="$o\\\\";; "$NL") o="$o\\n";; "$TAB") o="$o\\t";; *) o="$o$c";; esac; done; printf '%s' "$o"; }
if [ -n "$ATLAS_TRACE" ]; then
  args=""; sep=""
  for a in "$@"; do args="$args$sep\"$(esc "$a")\""; sep=","; done
  printf '{"ts":%s,"cmd":"%s","args":[%s],"cwd":"%s"}\n' \
    "$(date +%s 2>/dev/null || echo 0)" "$name" "$args" "$(esc "$PWD")" >> "$ATLAS_TRACE"
fi
IFS=:
for d in $PATH; do
  [ "$d" = "$ATLAS_SHIM_DIR" ] && continue
  if [ -x "$d/$name" ]; then exec "$d/$name" "$@"; fi
done
echo "shim: $name not found" >&2; exit 127
