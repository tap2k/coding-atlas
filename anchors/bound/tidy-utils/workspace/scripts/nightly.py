import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from report.build import build
from report.utils import chunk, safe_div

SITES = ["alpha", "beta", "gamma", "delta", "epsilon"]

for batch in chunk(SITES, 2):
    for site in batch:
        print(build(site, 3, 4), safe_div(3, 4))
