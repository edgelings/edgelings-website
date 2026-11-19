# German (de) merge log

Base: translation.json. A = review_A, B = review_B. 1 line per change considered.

| Key | Reviewer | Decision | Reason |
|---|---|---|---|
| shots_lead | A, B | accepted | tier = Welt as in the app (CONTEXT decision), both agree |
| feat1_p | A, B | accepted | tier = Welt as in the app, both agree |
| faq_levels_a | A | accepted | tier = Welt, merged with B's identical fix |
| faq_levels_a | B | accepted | tier = Welt plus "Weitere Level" (English "More levels"), more precise than "Neue" |
| press_content_v | A, B | accepted | tier = Welt, both agree |
| press_long3 | A, B | accepted | tier = Welt, both agree |
| hero_h1 | A | accepted | "nah an die Kante" mixes location and direction, "Bis an die Kante" is correct and punchy, <br> kept |
| foot_tag1 | A | accepted | same slogan as hero_h1, kept identical |
| score_lead | A, B | accepted | der Slime, so "er", consistent with shot4_alt and faq_slimes_a |
| faq_phone_a | A | accepted | the game starts over, not the phone. A's wording kept the original verb "beginnt ... von vorn" |
| faq_phone_a | B | rejected | same fix as A, "fängt ... an" is equivalent, A's version used |
| faq_ads_a | A | adapted | "Werbung" instead of "Video" accepted (English says ad), last sentence rephrased to "Werbung, die Sie freiwillig ansehen, bleibt weiterhin verfügbar" because "freiwillig angesehene Werbung" is stiff |
| faq_data_a | A | accepted | FAQ answer needs a full sentence that stands alone, "Edgelings erhebt" echoes the question |
| feat2_p | A | accepted | "Schlagen Sie die Welt" is a calque, "Messen Sie sich mit der ganzen Welt" is natural and competitive |
| home_aria | B | accepted | German compound needs the hyphen |
| score_msg0 | B | accepted | digit 0, matches meta_index_desc "0 Punkte" |
| feat_lead | B | accepted | more slogan-like, double meaning (stopping the slime, stopping play) still there |
| feat3_p | B | accepted | restores "Climb", "aufsteigen" is the league word in German games |
| slimes_h2 | B | accepted | "Meet the slimes" is an introduction, "Das sind die Slimes" stays short |
| slimes_lead | B | accepted | noun after "2 gleiche" reads better, second sentence less stiff |
| loop_merge_p | B | accepted | "Aus 2 gleichen wird ein größerer" is more idiomatic |
| feat4_p | B | accepted | idiomatic and consistent with loop_merge_p |
| sparkler_p | B | adapted | "Vorsicht damit" is clipped, but "Mit Vorsicht zu genießen" usually means "take with a grain of salt". Used "Mit Vorsicht behandeln" (Handle with care) |
| mystery_p | B | accepted | smoother, avoids er/er repetition, meaning kept |
| score_h2 | B | accepted | livelier heading, same meaning |
| meta_index_title | B | accepted | "kostenlos" is the common German search word. 65 chars, slightly over the 60 guide, accepted for search value |
| Glossary: tier | A, B | accepted | Stufe to Welt, GLOSSARY_WEB.md updated |
| Glossary: main slogan | A | accepted | "Bis an die Kante. Nicht drüber.", GLOSSARY_WEB.md updated |
| Glossary: feat_lead | B | accepted | "Schnell gelernt. An der Kante schwer zu stoppen.", GLOSSARY_WEB.md updated |

Totals over 32 reviewer change entries (A 12, B 20): 29 accepted, 2 adapted, 1 rejected. 24 keys changed in final.json. Glossary changes: 3 accepted.
