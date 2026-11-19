# hr merge log

## Text changes (A = review_A, B = review_B)
- meta_index_title (B): accepted. 66 to 58 characters, under the 60 limit, keywords kept.
- meta_index_desc (A, B): accepted B. Both fix the vague "nema ništa". B also adds "donose", which matches hero_lead. 153 characters.
- score_lead (A, B): adapted. A "Predaleko i padne" is still a fragment and B "Ako ode predaleko, pada" is flat. Final: "Ode li predaleko, padne." Short and natural.
- shots_lead (A, B): adapted. Both correctly flag the meaning. B "Prelistajte prvi svijet" still blurs screens and gameplay. Final: "Prelistajte snimke prvog svijeta."
- slimes_lead (A): accepted. "da vas pozdravi" is the greeting. "da vam se javi" sounds like contact.
- cookie_p (A, B): adapted. Took A's precision ("klikove na gumbe trgovina") and B's removal of the koristiti/koriste repetition ("upotrebljavati ... da vidimo"). Rejected B's "koliko se igra demo" because it shifts the meaning to counting how much. The consent meaning is complete.
- faq_what_a (A): adapted. Accepted "suprotnom rubu" and the restored "mobile". Wrote "casual mobilna igra" instead of A's doubled "za mobitele, za iPhone".
- press_long1 (A): accepted. "suprotnog ruba", consistent with faq_what_a.
- faq_data_a (A, B): accepted. Identical fix. The answer now has a verb.
- sup_delete_mail (A, B): accepted. Identical fix. "predmetom" plus Croatian quotes, subject in English as decided.
- press_meta (A, B): accepted. Identical fix. Adds the missing object "Materijale".
- hero_tag (B): accepted. "kratak predah" is the correct indefinite form.
- foot_tag2 (B): accepted. Same as hero_tag.
- foot_help (B): adapted. "pravno" as a noun is unnatural, but "pravila" reads like game rules. Final: "Pomoć i pravne informacije" (26 characters, within the limit).
- demo_lead (B): accepted. Drops the pronoun as APP_GLOSSARY asks. Livelier.
- feat_lead (B): accepted. "Teško je stati na rubu" is natural and closer to "hard to stop".
- feat1_p (B): accepted. Quoted tier names in nominative follow the site's UI label rule and read better than "od svijeta Lako do svijeta Ludo".
- feat6_p (B): accepted. "miran kutak" is the correct indefinite form.
- faq_devices_a (B): accepted. A full sentence for search engines and AI assistants.
- faq_leagues_a (B): accepted. "idu ligu više" is colloquial.
- faq_ads_a (B): accepted. "koje sami odlučite pogledati i dalje su dostupni" fixes an awkward phrase.
- sup_p (B): accepted. "u izborniku „Postavke”" keeps the label in nominative.
- sup_refund_p (B): accepted. Quotes around Google Play menu names, consistent with other UI labels.
- press_long3 (B): accepted. Same as feat1_p.
- get_opening (B): accepted. The verbal noun is the standard Croatian status form.

## Glossary changes
- Ultimate (A, B): accepted. Ekstremno, as app_terms.json and the site already use. Noted in GLOSSARY_WEB.md. APP_GLOSSARY.md (read-only) still says Ultimativno.
- email subject (A, B): accepted. predmet.
- far edge (A): accepted. suprotni rub, applied in faq_what_a and press_long1 (the only 2 occurrences).
- One quick game for a short break (B): accepted. "kratak predah", applied in hero_tag and foot_tag2.
- Help and legal (B): adapted. "Pomoć i pravne informacije".

Totals: accepted 24, adapted 6, rejected 0 (text: 20 accepted, 5 adapted. Glossary: 4 accepted, 1 adapted). Parts rejected within adapted items: B's "koliko se igra demo" (cookie_p), B's "pravila" (foot_help), A's "za mobitele, za" (faq_what_a).
