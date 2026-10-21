# SEO handover — Playback Media & Events Hub

Read this before building the Django backend. The current site is a static
design build; everything below must survive the move to Django.

Domain: **https://www.playbackmedia.in** (canonical, `www`, HTTPS)
Old site: https://playbackmedia.in (WordPress + Yoast)

---

## 1. URL rules (do not change)

* Every page URL is lowercase, hyphenated and **ends with a trailing slash**:
  `/about-us/`, `/corporate-photography/`, `/portfolio/nse-emerge-listing/`.
  These match the handover sitemap and the old WordPress URLs Google already has.
* Django: keep `APPEND_SLASH = True` (default) and write every `path()` with a
  trailing slash. Never serve the same page at two URLs.
* Filters use query strings and must stay working and shareable:
  `/portfolio/?category=photography|video|digital|events|av|corporate-films|advertising-tv|video-editing|medical|corporate-events`,
  `/showreel/?category=<video category>`, `/blog/?category=<blog category>`,
  `/get-a-quote/?service=photography|video|digital|events`.
  The canonical tag on these pages points to the URL **without** the query string.
* Force one host: redirect `http://` and bare `playbackmedia.in` to
  `https://www.playbackmedia.in` with a single 301 (no redirect chains).

### Full URL list

`sitemap.xml` in the repo root lists all 87 pages. Main ones:

| Section | URLs |
| --- | --- |
| Corporate | `/` `/about-us/` `/meet-the-team/` `/services/` `/portfolio/` `/showreel/` `/clients-testimonials/` `/blog/` `/careers/` `/freelancers/` `/contact-us/` `/get-a-quote/` `/privacy-policy/` `/terms-conditions/` |
| Photography | `/photography/` `/corporate-photography/` `/product-photography/` `/portfolio-photography/` `/event-photography/` |
| Video | `/video-production/` `/corporate-films/` `/advertising-films/` `/television-production/` `/video-editing/` `/promotional-videos/` |
| Digital | `/digital-marketing/` `/social-media-marketing/` `/seo-services/` `/performance-marketing/` `/website-development/` `/healthcare-digital-marketing/` `/influencer-marketing/` |
| Events | `/event-management/` `/corporate-events/` `/medical-conference-management/` `/audio-visual-production/` `/exhibition-stalls-branding/` `/live-streaming/` |
| Detail pages | `/portfolio/<project-slug>/` (39) · `/blog/<post-slug>/` (10) |

---

## 2. Redirect map from the old WordPress site (301, permanent)

Audited from the old site's Yoast sitemaps (post, page, category) on 22 Oct 2026.

**Already identical — no redirect needed (11):**
`/` `/contact-us/` `/corporate-photography/` `/digital-marketing/` `/event-photography/`
`/live-streaming/` `/meet-the-team/` `/photography/` `/portfolio/` `/privacy-policy/` `/services/`

**Must redirect (28):**

| Old URL | New URL |
| --- | --- |
| `/about-playback-media/` | `/about-us/` |
| `/company-overview/` | `/about-us/` |
| `/our-clients/` | `/clients-testimonials/` |
| `/testimonials/` | `/clients-testimonials/` |
| `/our-works/` | `/portfolio/` |
| `/blogs/` | `/blog/` |
| `/category/uncategorized/` | `/blog/` |
| `/join-our-team/` | `/careers/` |
| `/get-your-free-quotation/` | `/get-a-quote/` |
| `/disclaimer/` | `/terms-conditions/` |
| `/dcm/` | `/` *(unknown old page — check what it was, map better if possible)* |
| `/corporate-shoot/` | `/corporate-films/` |
| `/tv-production/` | `/television-production/` |
| `/documentary-biography/` | `/television-production/` |
| `/motion-graphic/` | `/video-editing/` |
| `/testimonial-video/` | `/promotional-videos/` |
| `/videography-video-production/` | `/video-production/` |
| `/videography-services-delhi-ncr/` | `/video-production/` |
| `/what-types-of-video-production-do-you-offer/` | `/video-production/` |
| `/photography-services-delhi-ncr/` | `/photography/` |
| `/what-types-of-photography-services-do-you-offer/` | `/photography/` |
| `/what-type-of-digital-marketing-services-you-provide/` | `/digital-marketing/` |
| `/sports-shoot/` | `/event-photography/` |
| `/conference-live-events/` | `/showreel/?category=events` |
| `/corporate-event-video/` | `/showreel/?category=events` |
| `/educational-video/` | `/showreel/?category=education` |
| `/training-videos/` | `/showreel/?category=education` |
| `/youtube-video/` | `/showreel/?category=social` |

Before launch, also export **all indexed URLs from Google Search Console**
(the old menu linked pages that are not in its sitemap, e.g. medical, CME,
healthcare SEO and AV pages) and add any that are missing to this table.
Never redirect everything to the homepage.

Django: use `django.contrib.redirects` (editable in admin) or a small
middleware with this table; return **301**, not 302.

---

## 3. Already implemented in the static build (keep it)

| Item | Where / how |
| --- | --- |
| Unique `<title>` per page (≤ ~66 chars, brand suffix shortened on long titles) | `core.page()` |
| Unique meta description per page (~60–165 chars) | each page/service/project/post |
| `<link rel="canonical">` (absolute, `www`, trailing slash) | `core.page()` |
| Open Graph + Twitter card (title, description, image, URL) | `core.page()` |
| `lang="en-IN"` | `core.page()` |
| Exactly one `<h1>` per page, logical `h2/h3` | all templates |
| JSON-LD: `LocalBusiness` + `WebSite` (home), `BreadcrumbList` (inner pages), `Service` + `FAQPage` (service pages), `CreativeWork` (projects), `BlogPosting` (posts), `ContactPage` | `core.page()`, `services.py`, `pages.py` |
| Visible breadcrumbs that match the JSON-LD | `core.crumbs_html()` |
| `sitemap.xml` + `robots.txt` | `build.py` |
| Custom 404 page | `404.html` |
| Descriptive image `alt`; WebP images; `-sm` thumbnails for grids; `loading="lazy"` + `decoding="async"` | everywhere |
| YouTube loads only on click (thumbnail facade, `youtube-nocookie.com`) | `main.js` |
| Internal linking: mega menu, footer, related services, project → service links, blog → service CTA | templates |
| NAP consistency: Playback Media & Events Hub · Ghaziabad, Delhi NCR · +91 9999104399 · mail@playbackmedia.in | `data.py` `SITE` |

---

## 4. Django implementation checklist

**Templates & metadata**
- [ ] `base.html` = `core.page()` + `header()` + `footer()`; blocks for `title`, `meta_description`, `canonical`, `og_image`, `schema`, `content`.
- [ ] Every model that renders a page (ServicePage, Project, BlogPost, Job…) gets `seo_title`, `meta_description`, `og_image`, `slug` (unique), editable in admin, with sensible fallbacks.
- [ ] Canonical = `request.build_absolute_uri(request.path)` forced to `https://www.` (no query string).
- [ ] Output JSON-LD from the same data as the visible page (breadcrumbs, FAQs, articles).

**Sitemaps, robots, errors**
- [ ] `django.contrib.sitemaps` for static pages, services, projects, posts (with `lastmod` from `updated_at`); only published items.
- [ ] `robots.txt` view; on **staging** return `Disallow: /` and add `<meta name="robots" content="noindex">` so the dev site is never indexed.
- [ ] Real `404.html` / `500.html` templates returning the correct status codes.
- [ ] Unpublished/draft content returns 404, not an empty page.

**Content management (from the handover)**
- [ ] Blog: categories, featured image, author, publish date & scheduling, SEO fields, rich text with internal links.
- [ ] Portfolio: one project record shown under several categories (many-to-many) — no duplicate pages.
- [ ] Team: display order + publish toggle; no personal contact details.
- [ ] Careers: openings from the database; when none, show the "Don't See a Suitable Opening?" block.

**Forms / CRM**
- [ ] Keep field names already used by the front end (`name`/`full_name`, `email`, `mobile`, `service`, `message`, `form_type`, `source_page`, `utm`, `consent`, honeypot `company_website`).
- [ ] Server-side validation, CSRF, rate limiting, honeypot check, file-type/size checks for resumes (PDF/DOC/DOCX ≤ 5 MB).
- [ ] Store every enquiry in the CRM; admin email notification; success message only after saving.
- [ ] Thank-you state must not create a new indexable URL (or mark it `noindex`).

**Performance (Core Web Vitals)**
- [ ] Serve static files with long cache headers + hashed filenames (`ManifestStaticFilesStorage`/WhiteNoise); gzip/brotli.
- [ ] Keep image sizes as in the static build (full + `-sm`); generate thumbnails on upload for new images.
- [ ] Don't add render-blocking scripts; `main.js` stays at the end of `<body>`.

**Launch day**
- [ ] 301 redirects from section 2 live and tested (one hop each).
- [ ] Submit the new sitemap in Google Search Console; request indexing for key pages.
- [ ] Update Google Business Profile: name, website URL, phone, category, Ghaziabad location (no old Lado Sarai address).
- [ ] Analytics (GA4) + Search Console verified; track form submissions, WhatsApp and phone clicks as conversions.

---

## 5. Moving this build to Django (no need to flatten folders)

The folders (`about-us/index.html`) exist only to give the static site the
same clean URLs Django will serve. Don't move or edit the generated HTML;
port the **source** in `_build/` instead:

| `_build/` today | Django equivalent |
| --- | --- |
| `core.page()`, `header()`, `mobile_menu()`, `footer()` | `templates/base.html` + includes |
| `core.py` components (`phero`, `shead`, `steps`, `faq`, `gallery`, `vcard`, `form`…) | template includes / inclusion tags |
| `pages.py` page functions | one template + view per page |
| `services.py` `S` dict | `ServicePage` model (or fixtures) + one `service_detail.html` |
| `data.py` `PROJECTS`, `VIDEOS`, `TEAM`, `CLIENTS`, `TESTIMONIALS`, `JOBS` | models, managed in Django admin |
| `blog.py` `POSTS` | `BlogPost` model |
| `~/` path prefix in `render()` | `{% url %}` and `{% static %}` |
| `assets/` | `static/` (unchanged files) |

Keep `assets/css/style.css` and `assets/js/main.js` as they are — the design
does not depend on the folder layout.
