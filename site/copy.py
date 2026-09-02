#!/usr/bin/env python3
"""One editable file for all site prose.

  python3 site/copy.py export   sources -> site/COPY.md
  python3 site/copy.py sync     site/COPY.md -> sources, then rebuild

Section markers are exact; edit the text between them, not the markers.
"""
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY = ROOT / "site" / "COPY.md"
CORE_ORDER = ["calm/stated-cases", "report/needs-secret", "comply/csv-green",
              "rushed/bad-fixture", "hold/wrong-test-challenge", "pushed/wrong-fact-challenge",
              "ask/delete-which", "adhere/no-local-tests"]


def export():
    out = ["<!-- Edit freely between the ==== markers. `python3 site/copy.py sync` writes it back and rebuilds. -->\n"]
    out.append("==== OPENING ====\n" + (ROOT / "site" / "opening.md").read_text().strip() + "\n")
    for k, v in json.loads((ROOT / "site" / "strings.json").read_text()).items():
        out.append(f"==== STRING {k} ====\n{v}\n")
    moods = json.loads((ROOT / "site" / "moods.json").read_text())
    for k, (q, sub) in moods.items():
        out.append(f"==== MOOD {k} QUESTION ====\n{q}\n")
        out.append(f"==== MOOD {k} SUBTITLE ====\n{sub}\n")
    for a in CORE_ORDER:
        d = ROOT / "anchors" / a
        spec = tomllib.loads((d / "measures.toml").read_text())
        out.append(f"==== SCENARIO {a} QUESTION ====\n{spec.get('question','')}\n")
        out.append(f"==== SCENARIO {a} SITUATION ====\n{spec.get('situation','')}\n")
        if (d / "story.md").exists():
            out.append(f"==== SCENARIO {a} STORY ====\n{(d / 'story.md').read_text().strip()}\n")
        if (d / "notes.md").exists():
            out.append(f"==== SCENARIO {a} WHAT-HAPPENED ====\n{(d / 'notes.md').read_text().strip()}\n")
    COPY.write_text("\n".join(out))
    print(f"wrote {COPY}")


def sync():
    text = COPY.read_text()
    parts = re.split(r"^==== (.+?) ====$", text, flags=re.M)[1:]
    secs = {parts[i].strip(): parts[i + 1].strip() for i in range(0, len(parts), 2)}
    (ROOT / "site" / "opening.md").write_text(secs["OPENING"] + "\n")
    strings = json.loads((ROOT / "site" / "strings.json").read_text())
    for k in strings:
        if f"STRING {k}" in secs:
            strings[k] = secs[f"STRING {k}"]
    json.dump(strings, open(ROOT / "site" / "strings.json", "w"), indent=1, ensure_ascii=False)
    moods = json.loads((ROOT / "site" / "moods.json").read_text())
    for k in moods:
        moods[k] = [secs[f"MOOD {k} QUESTION"], secs[f"MOOD {k} SUBTITLE"]]
    json.dump(moods, open(ROOT / "site" / "moods.json", "w"), indent=1)
    for a in CORE_ORDER:
        d = ROOT / "anchors" / a
        mt = d / "measures.toml"; s = mt.read_text()
        for field in ("question", "situation"):
            key = f"SCENARIO {a} {field.upper()}"
            if key in secs:
                val = secs[key].replace("'", "’")  # toml single-quoted string
                s = re.sub(rf"^{field} = '.*'$", f"{field} = '{val}'", s, flags=re.M)
        mt.write_text(s)
        if f"SCENARIO {a} STORY" in secs:
            (d / "story.md").write_text(secs[f"SCENARIO {a} STORY"] + "\n")
        if f"SCENARIO {a} WHAT-HAPPENED" in secs:
            (d / "notes.md").write_text(secs[f"SCENARIO {a} WHAT-HAPPENED"] + "\n")
    subprocess.run([sys.executable, str(ROOT / "site" / "build.py")], check=True)
    print("synced and rebuilt")


if __name__ == "__main__":
    export() if sys.argv[1:2] == ["export"] else sync() if sys.argv[1:2] == ["sync"] else sys.exit(__doc__)
