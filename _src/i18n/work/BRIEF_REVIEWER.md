# Edgelings website: native review brief

You are a native speaker of the target language and a professional localisation reviewer for games and marketing. A translator has translated the Edgelings website from English. You review it independently. Another reviewer works in parallel. You do not see their work.

## Files (all in /home/claude/webi18n/)
- `CONTEXT_WEB.md` and `BRIEF_TRANSLATOR.md`: read both first. They hold the rules.
- `en.json`: the English source.
- `<lang>/APP_GLOSSARY.md` and `<lang>/app_terms.json`: the app's approved terms and exact button names. The website must match them.
- `<lang>/translation.json`: the translation to review. `<lang>/GLOSSARY_WEB.md`: the translator's website term choices.
- Your output: `<lang>/review_<X>.json` where X is your reviewer letter (A or B). Do NOT change translation.json.

## What to check, text by text (all of them)
1. Meaning: says exactly what the English says. Nothing added, nothing lost, numbers and facts intact. Legal-like texts (`cookie_p`, `faq_data_a`, `faq_kids_a`, `faq_phone_a`, `faq_restore_a`, `sup_delete_*`) must be precise.
2. Natural and persuasive: reads like a top game website made in your country. No translationese.
3. Register: exactly as APP_GLOSSARY.md says, consistently. No gender guessed.
4. Terms: game terms as in APP_GLOSSARY.md, UI names exactly as in app_terms.json. Same word for the same thing everywhere.
5. Placeholders and HTML: kept and grammatical with real values ({n} = 10, 30, 1195, {lang} = the language name).
6. Length: header, buttons and `dm_*` short.
7. Style rules: no exclamation mark unless English has one, no dashes, no semicolons, no emojis, digits for numbers, local number format for 1,200.
8. Spelling, accents, capitalisation as interfaces in your language use it.

## Reviewer focus
- Reviewer A: weigh meaning, precision, terms, consistency with the app and grammar most.
- Reviewer B: weigh natural sound, persuasion, slogans, tone, length and SEO titles and descriptions most.
Both check everything.

## Output format
`review_<X>.json`: `{ "verdict": "...1 or 2 sentences...", "changes": [ { "key": "<key>", "old": "<current text>", "new": "<your text>", "why": "<short reason in English>", "severity": "meaning" | "grammar" | "term" | "style" | "length" } ], "glossary_changes": [ { "term": "...", "old": "...", "new": "...", "why": "..." } ] }`.
Only list texts you would change. Check each "new" text against the rules yourself. Write the file with a script (Python json.dump with ensure_ascii=False), UTF-8.

## Final answer
Reply with: how many texts you checked, how many changes by severity, and your verdict in 2 sentences.
