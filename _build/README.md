# Playback Media & Events Hub — website build

The site is plain HTML, CSS and JavaScript. Pages are generated from the Python
files in this folder so that the header, mega menu, footer and design stay
identical on every page.

## Rebuild after editing

```
python _build/build.py
```

This rewrites every page folder (`about-us/index.html`, `corporate-photography/index.html`,
`portfolio/<project>/index.html`, `blog/<post>/index.html` …), plus `sitemap.xml`,
`robots.txt` and `404.html`. Do not edit the generated HTML by hand; edit the
source files below and rebuild. Requires Python 3.9+ (no extra packages).

## Where things live

| What to change | File |
| --- | --- |
| Phone numbers, email, socials, team, clients, testimonials, videos, portfolio projects, job openings | `_build/data.py` |
| Service pages (photography, video, digital, events and their sub-pages) | `_build/services.py` |
| Blog articles | `_build/blog.py` |
| Homepage, About, Team, Portfolio, Showreel, Careers, Contact, Quote, legal pages | `_build/pages.py` |
| Header, mega menu, mobile menu, footer, shared components, forms | `_build/core.py` |
| All styles | `assets/css/style.css` |
| All interactions | `assets/js/main.js` |

## Common tasks

* **Add a job opening:** add an entry to `JOBS` in `data.py`
  (`title, department, location, type, experience, summary, details`) and rebuild.
  With no openings the Careers page shows the "Don't See a Suitable Opening?" panel.
* **Add a portfolio project:** add a `_p(...)` entry to `PROJECTS` in `data.py`.
  Photos go in `assets/img/work/<slug>/01.webp, 02.webp …` with matching
  `01-sm.webp …` thumbnails (about 760 px). A project can belong to several
  categories without being duplicated.
* **Add a video:** add `(youtube_id, title, [categories])` to `VIDEOS` in `data.py`.
* **Add a blog post:** add a dict to `POSTS` in `blog.py`.
* **Team order / hide a profile:** reorder or remove entries in `TEAM`.

## Forms (contact, quote, careers, freelancers, service enquiries)

Forms are validated in the browser, include a spam honeypot, prevent double
submission and capture the source page and UTM parameters.

To store submissions in the CRM, set the endpoint at the top of
`assets/js/main.js`:

```js
const FORM_ENDPOINT = 'https://your-crm.example.com/api/enquiries';
```

The endpoint receives a `multipart/form-data` POST (files included) and should
return a 2xx status. Every form sends `form_type`, `source_page` and `utm`.
Server-side validation, rate limiting, storage and admin notifications belong
on that endpoint.

Until an endpoint is set, a valid submission shows the visitor prefilled
"Send by email" (to mail@playbackmedia.in) and "Send on WhatsApp" buttons.

## Hosting

Upload or push the whole folder. Folders that start with `_` are not published
by GitHub Pages. The site works on the GitHub Pages project URL and on
www.playbackmedia.in without changes; canonical URLs and the sitemap point to
https://www.playbackmedia.in.
