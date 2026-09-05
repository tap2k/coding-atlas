# Model roster (survey 2026-08-28)

Source: a web survey (OpenRouter and OpenCode token boards, vendor announcements, community
threads), run 2026-08-28. Token boards skew to free and stealth tiers; treat as mindshare,
not quality. Full evidence table in the survey output; key sources:
OpenRouter rankings snapshot (tokenmaxxing.com, 08-27), opencode.ai/data (08-28),
TechNode on GLM-5.3-Flash (08-27), vendor release posts.

## Initial roster (7 rows), all through OpenCode Zen unless noted

Final 2026-08-28, ten OpenCode rows in three groups:
- native-matching: claude-opus-5, gpt-5.6-terra, gemini-3.5-flash
- frontier (each lab's current top): claude-fable-5, gpt-5.6-sol, gemini-3.7-flash, grok-4.6
  - 2026-09-04: gpt-6-astra added (OpenAI flagship, launched 09-03; Zen id `opencode/gpt-6-astra`,
    $10/$50 per M). Sol row kept as the prior flagship.
- open weights: deepseek-v4-flash, kimi-k3, glm-5.2 (swap in glm-5.3-flash when Zen lists it)
Plus the three native CLI rows. Alternates: minimax-m3, qwen3.6-plus, deepseek-v4-pro, kimi-k2.7-code.

Native-matching (what the native CLIs served today; the harness-vs-model column)
- claude-opus-5 (Claude Code default; over-scoping reputation in r/ClaudeAI this month)
- gpt-5.6-terra (what Codex served; note Codex's recommended default is Sol)
- gemini-3.5-flash (what Gemini CLI served; Google's current workhorse is 3.7 Flash)

Frontier closed
- gpt-5.6-sol (OpenAI flagship, 07-09)
- gemini-3.7-flash (Google's current coding model, 08-13)
- grok-4.6 (xAI flagship, 08-12; default in Grok Build)

Open weights / Chinese
- deepseek-v4-flash (#1 OpenRouter, #2 OpenCode by tokens; "executes well, doesn't plan")
- kimi-k3 (largest open model; "max reasoning by default, slow and verbose")
- glm-5.2 (top open SWE-bench Pro; terse tool calls). glm-5.3-flash (weights 08-27, 41T
  OpenCode tokens as "Ox Alpha") is not on Zen yet; swap in when it lands.
- minimax-m3 (554B/day OpenRouter; first alternate promoted to the roster since qwen3.7 is
  not on Zen and qwen3.6-plus is superseded)

Alternates: deepseek-v4-pro, kimi-k2.7-code, claude-fable-5, muse-spark-1.2, qwen3.6-plus.

## Rules
- Pin the id; record served model; re-run a row when its vendor ships.
- n=1 screen before n=3 on any new row.
- Each row is OpenCode x model. Native rows (Claude Code, Codex, Gemini CLI) stay separate.
