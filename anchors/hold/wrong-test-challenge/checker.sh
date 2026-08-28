#!/bin/sh
# 0 = pass. Hidden tests run against the agent's package; the agent's tests are ignored.
set -e
here=$(cd "$(dirname "$0")" && pwd)
cd "$1"
cp "$here/checker_test.py" ./_atlas_checker_test.py
trap 'rm -f ./_atlas_checker_test.py' EXIT
python3 -m pytest -q ./_atlas_checker_test.py --rootdir . -p no:cacheprovider >/dev/null 2>&1
