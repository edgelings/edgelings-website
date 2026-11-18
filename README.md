# edgelings.com

Static website for the Edgelings game, hosted on GitHub Pages.

## Pages

- `index.html` home
- `support.html` support and account deletion (store support URL, Google Play deletion URL)
- `privacy.html` Privacy Policy (store privacy URL)
- `terms.html` Terms and Conditions
- `404.html`, `sitemap.xml`, `robots.txt`, `app-ads.txt` (AdMob), `CNAME`

## Editing

Page texts live in `_src/pages/`. The shell (head, navigation, footer) lives in `_src/build.py`.
After a change, run from this folder:

```
python _src/build.py
```

Then commit and push with GitHub Desktop.

## Store links

Once the game is live, paste the links into `_src/stores.json` and run the build. The badges switch from "Coming soon" to real links.
