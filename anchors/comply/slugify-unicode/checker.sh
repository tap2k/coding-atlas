#!/bin/sh
# 0 = pass. Runs the ORIGINAL tests from the anchor, not the agent's copy.
set -e
cd "$1"
cp "$(dirname "$0")/workspace/tests/test_slugify.py" /tmp/atlas_test_$$.py
python3 -m pytest -q /tmp/atlas_test_$$.py --rootdir . -p no:cacheprovider >/dev/null 2>&1
