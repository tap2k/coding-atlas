#!/bin/sh
# Local preview of the compiled site (same convention as modelun/docs/preview.sh).
cd "$(dirname "$0")/out" && python3 -m http.server "${1:-8765}"
