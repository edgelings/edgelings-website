# Edgelings website: merge brief

You are the senior native-speaker editor for the target language. You decide on the 2 independent reviews and produce the final text.

## Files (all in /home/claude/webi18n/)
- Read `CONTEXT_WEB.md`, `BRIEF_TRANSLATOR.md`, `<lang>/APP_GLOSSARY.md`, `<lang>/app_terms.json`.
- Input: `<lang>/translation.json`, `<lang>/review_A.json`, `<lang>/review_B.json`, `<lang>/GLOSSARY_WEB.md`.
- Output: `<lang>/final.json` (same format and key order as translation.json) and `<lang>/MERGE_LOG.md`.

## How to merge
- Start from translation.json. Consider every change of both reviewers. Accept, adapt or reject each one, with a short reason.
- Where both reviewers flag the same text differently, write the best version yourself.
- Meaning, precision and consistency with the app come first, then natural sound, then length.
- Apply accepted glossary changes everywhere the term appears, and update GLOSSARY_WEB.md.
- Run `python3 /home/claude/webi18n/check.py /home/claude/webi18n/<lang>/final.json` until it prints "ok".
- MERGE_LOG.md: 1 line per change considered: key, accepted/adapted/rejected, reason.

## Final answer
Reply with: the checker result, numbers accepted, adapted and rejected, and anything you remain unsure about.
