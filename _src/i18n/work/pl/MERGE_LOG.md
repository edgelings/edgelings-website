# Polish (pl) merge log

Base: translation.json. A = review_A.json, B = review_B.json.

| Key | Reviewer | Decision | Reason |
|---|---|---|---|
| sup_delete_mail | A | adapted | English subject „Delete my Edgelings account” as decided. Merged with B's wording |
| sup_delete_mail | B | accepted | English subject plus "wysłać e-mail ... podać w nim", which fits "z tematem" better |
| dm_more | A, B | accepted | "Jeszcze {n} poziomów" ({n}=1195, genitive plural correct), fixes broken 2 line pair |
| dm_full | A, B | accepted | "czeka" agrees with numeral 5+ |
| step3 | A | accepted | Removes "wzrosną 3 razy" ambiguity, shortest, matches score_msg3 pattern |
| step3 | B | rejected | Same fix as A but longer for a very short step |
| meta_support_desc | A, B | accepted | "ustawienia reklam" = ad consent choices, not a selection of ads |
| feat2_p | A | accepted | "Cały świat do pokonania" clashes with "świat" = tier. New text is unambiguous |
| shot4 | A | accepted | Ice makes slimes slide, not speed up |
| score_blob_alt | A | accepted | Colon makes Mossy the speaker, not the addressee |
| faq_what_a | A | accepted | "pstrykać czymś" (instrumental) is the idiomatic construction (cf. pstrykać kapslami), now consistent with hero_lead |
| faq_kids_a | A, B | accepted | "porównywane z listą" is idiomatic |
| press_video_p | A | accepted | Fixes split word order |
| press_long3 | A, B | accepted | Removes "ligach ... ligami" repetition |
| qr_text | A | accepted | "Na komputerze?" is closest to English, short, gender neutral |
| qr_text | B | rejected | "Strona otwarta na komputerze?" is longer and still stiff. A's version chosen |
| meta_index_title | B | accepted | Restores the edge hook, keeps free and both platforms, 60 characters |
| meta_index_desc | B | adapted | Flick restored, but "Pstryk i" instead of "Pstryknięcie i" to stay within 155 characters (151) |
| hero_chip | B | accepted | "na urządzenia" is stiff for a chip |
| band_p | B | accepted | Shorter and punchier, same facts |
| hero_lead | B | rejected | Instrumental "pstryknąć glutkiem" is correct Polish (A's glossary decision). Current text is precise and complete |
| score_lead | B | accepted | "Za daleko? Spada." is natural, removes calque |
| video_lead | B | accepted | "Bez reżyserowanych ujęć" is the usual phrase for staged footage |
| shots_lead | B | accepted | Restores the swipe invitation, short hint in imperative as the register allows |
| feat4_h | B | accepted | Lively heading with the app term "fuzja". Growth is carried by feat4_p |
| faq_levels_a | B | accepted | Removes calques "dodaje sztuczki", "przychodzą z serwera", same facts |
| faq_restore_a | B | accepted | "Te" points clearly to coins and used up items |
| press_genre_v | B | accepted | Removes dangling adjective |
| glossary: flick | A | accepted | One construction everywhere: pstrykać/pstryknąć glutkiem, pstrykanie glutkami. Added to GLOSSARY_WEB.md |
| glossary: deletion subject | A | accepted | Added to GLOSSARY_WEB.md as English text in Polish quotes |

Totals (1 line per change, shared A+B changes counted once): 25 accepted, 2 adapted, 3 rejected.
