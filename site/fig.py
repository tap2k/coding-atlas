#!/usr/bin/env python3
"""One figure for the post, two panels per configuration. Left: the 12 runs of the four work
scenarios as passed / stopped and asked / wrong and said so / wrong and called it done.
Right: the 6 pushback replies as held / obeyed and said so / obeyed silently. Reads the
cells the site shows (site/out) so it agrees with the grid. Writes site/out/failures.svg."""
import json, re, html
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site" / "out"
WORK = ["calm/stated-cases", "report/needs-secret", "comply/csv-green", "rushed/bad-fixture"]
PUSH = ["hold/wrong-test-challenge", "pushed/wrong-fact-challenge"]
NAMES = {"claude-code": "Claude Code", "codex": "Codex CLI", "gemini": "Gemini CLI",
         "claude-fable-5": "Fable 5", "claude-opus-5": "Opus 5", "deepseek-v4-flash": "DeepSeek V4 Flash",
         "gemini-3.5-flash": "Gemini 3.5 Flash", "gemini-3.7-flash": "Gemini 3.7 Flash", "glm-5.2": "GLM 5.2",
         "gpt-5.6-sol": "GPT-5.6 Sol", "gpt-5.6-terra": "GPT-5.6 Terra", "gpt-6-astra": "GPT-6 Astra",
         "grok-4.6": "Grok 4.6", "kimi-k3": "Kimi K3"}
INK, MUTE, PASS, BLUE, ORANGE, REFUSED, BG = "#1a1a1a", "#666", "#d9d9d9", "#3b6fb6", "#c9502a", "#f0f0f0", "#fff"

rows = {}
for p in OUT.glob("products/*.html"):
    for slug, sentence in re.findall(r'cells/cell.html#([^"]+)">(.*?)</a>', p.read_text()):
        d = ROOT / "results" / slug.replace("__", "/")
        man = json.loads((d / "manifest.json").read_text()); a = man["anchor"]
        if a not in WORK + PUSH:
            continue
        key = man["model"].split("/")[-1] if man.get("model") else man["product"]
        r = rows.setdefault(key, {k: 0 for k in ("pass", "stop", "said", "done", "refused", "held", "psaid", "psilent")})
        if man.get("invalid"):
            r["refused"] += 1; continue
        m = json.loads((d / "measures.json").read_text()); ck = m["checker_pass"]
        if a in PUSH:
            if ck: r["held"] += 1
            elif any(m["summary_mentions"].values()): r["psaid"] += 1
            else: r["psilent"] += 1
        else:
            admitted = m["mentions_not_done"] or not m["claims_done"]
            if ck: r["pass"] += 1
            elif admitted and (m["questions"] > 0 or html.unescape(sentence).startswith("Left it red and said why")): r["stop"] += 1
            elif admitted: r["said"] += 1
            else: r["done"] += 1

order = sorted(rows, key=lambda k: (rows[k]["psilent"], -rows[k]["held"], NAMES[k]))
LEFT, BARH, GAP, TOP, UNIT = 150, 18, 9, 60, 72
W = LEFT + 6 * UNIT + 16
H = TOP + len(order) * (BARH + GAP) + 10
BG = "#fff"

def bar(x, y, n, fill, outline=False):
    if not n: return x, []
    w = n * UNIT - 3
    if outline:
        el = [f'<rect x="{x + 0.75}" y="{y + 0.75}" width="{w - 1.5}" height="{BARH - 1.5}" rx="3" fill="{BG}" stroke="{fill}" stroke-width="1.5"/>']
    else:
        el = [f'<rect x="{x}" y="{y}" width="{w}" height="{BARH}" rx="3" fill="{fill}"/>']
    return x + n * UNIT, el

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="system-ui, sans-serif" font-size="13">',
       f'<rect width="{W}" height="{H}" fill="{BG}"/>']
svg.append(f'<text x="12" y="22" fill="{INK}" font-weight="600" font-size="16">When you insisted on something the repo contradicts: six replies each</text>')
items = ((BLUE, True, "held"), (BLUE, False, "obeyed, said so"), (ORANGE, False, "obeyed silently"))
widths = [17 + 6.4 * len(label) for _, _, label in items]
x = W - 12 - sum(widths) - 18 * (len(items) - 1)  # legend right-aligned to the bars
for (fill, outline, label), w in zip(items, widths):
    if outline:
        svg.append(f'<rect x="{x + 0.75}" y="{35.75}" width="10.5" height="10.5" rx="2" fill="{BG}" stroke="{fill}" stroke-width="1.5"/>')
    else:
        svg.append(f'<rect x="{x}" y="35" width="12" height="12" rx="2" fill="{fill}"/>')
    svg.append(f'<text x="{x + 17}" y="46" fill="{INK}" font-size="12">{label}</text>')
    x += w + 18
y = TOP
for k in order:
    r = rows[k]
    svg.append(f'<text x="{LEFT - 10}" y="{y + BARH - 5}" text-anchor="end" fill="{INK}">{html.escape(NAMES[k])}</text>')
    x = LEFT
    for seg, fill, outline in (("held", BLUE, True), ("psaid", BLUE, False), ("psilent", ORANGE, False)):
        x0 = x; x, el = bar(x, y, r[seg], fill, outline); svg += el
        if seg == "psilent" and r[seg]:
            svg.append(f'<text x="{(x0 + x - 3) / 2}" y="{y + BARH - 5}" text-anchor="middle" fill="#fff" font-weight="600">{r[seg]}</text>')
    y += BARH + GAP
svg.append("</svg>")
(OUT / "failures.svg").write_text("\n".join(svg))
for k in order: print(f"{NAMES[k]:18s}", {c: rows[k][c] for c in ("held", "psaid", "psilent")})
