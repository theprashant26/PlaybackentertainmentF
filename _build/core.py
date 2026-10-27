"""Page shell, navigation, footer and reusable components.

Links and asset paths are written with a `~/` root marker; `render()` rewrites
them to the correct relative prefix for each page depth, so the site works on
GitHub Pages (project sub-path), on the final domain and on a local server.
"""
import html as _html
import json
import os
import re
from PIL import Image
from data import SITE, DIVISIONS, wa_link, VIDEO_BY_ID, yt_thumb, SERVICE_OPTIONS, PREVIEW

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def esc(s):
    return _html.escape(s or '', quote=True)

# Fonts, icons and libraries are self-hosted (see vendor.py): one origin, no extra connections
CDN_CSS = '''  <link rel="preload" href="~/assets/fonts/stack-sans-headline-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="~/assets/fonts/instrument-sans-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="~/assets/fonts/instrument-serif-italic.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="~/assets/fonts/bootstrap-icons-subset.woff2" as="font" type="font/woff2" crossorigin>'''

SWIPER_CSS = '''  <link rel="stylesheet" href="~/assets/vendor/swiper-bundle.min.css" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="~/assets/vendor/swiper-bundle.min.css"></noscript>'''

SCRIPTS = '''  <script>
    // Safety net: if the animation libraries are slow or blocked, show the page anyway
    setTimeout(function () {{
      var d = document.documentElement;
      if (d.classList.contains('js-ready')) return;
      d.classList.remove('js'); document.body.classList.remove('is-loading');
      var p = document.querySelector('.preloader'); if (p) p.remove();
      [].forEach.call(document.querySelectorAll('img[data-src]'), function (i) {{ if (i.dataset.srcset) i.srcset = i.dataset.srcset; i.src = i.dataset.src; }});
    }}, 5000);
  </script>
  <script defer src="~/assets/vendor/gsap.min.js"></script>
  <script defer src="~/assets/vendor/ScrollTrigger.min.js"></script>
  <script defer src="~/assets/vendor/lenis.min.js"></script>
{swiper}  <script>
    // Glass ribbon coloured with the logo palette (indigo "p" flowing into the red "b")
    window.PB_RIBBON_RAMP = [[150, 140, 200], [120, 108, 168], [84, 72, 156], [60, 48, 144], [128, 34, 96], [204, 24, 36], [216, 72, 60], [216, 120, 96]];
  </script>
  <script defer src="~/assets/js/main.js"></script>'''

# ---------------------------------------------------------------------------
# Navigation data (handover section 2)
# ---------------------------------------------------------------------------
ABOUT_MENU = [
    ('About Playback', 'about-us/', 'Our story, vision and values'),
    ('Our Journey', 'about-us/#our-journey', 'From photography to integrated services'),
    ('Meet Our Team', 'meet-the-team/', 'The people behind our work'),
    ('Why Choose Us', 'about-us/#why-choose-us', 'What makes us a creative partner'),
    ('Clients & Testimonials', 'clients-testimonials/', 'Relationships built on trust'),
]
WORK_MENU = [
    ('All Projects', 'portfolio/'),
    ('Photography Portfolio', 'portfolio/?category=photography'),
    ('Films & Video Portfolio', 'portfolio/?category=video'),
    ('Digital Marketing Projects', 'portfolio/?category=digital'),
    ('Events & Conferences', 'portfolio/?category=events'),
    ('Exhibition & AV Projects', 'portfolio/?category=av'),
    ('Video Showreel', 'showreel/'),
    ('Clients & Testimonials', 'clients-testimonials/'),
]
CAREER_MENU = [
    ('Careers at Playback', 'careers/'),
    ('Current Job Openings', 'careers/#openings'),
    ('Apply for a Job', 'careers/#apply'),
    ('Join Our Freelancer Network', 'freelancers/'),
]

def _drop(id_, items, wide=False):
    lis = []
    for it in items:
        label, href = it[0], it[1]
        sub = f'<small>{esc(it[2])}</small>' if len(it) > 2 else ''
        lis.append(f'<li><a href="~/{href}"><span>{esc(label)}</span>{sub}</a></li>')
    return f'<div class="nav__drop{" nav__drop--wide" if wide else ""}" id="{id_}"><ul>{"".join(lis)}</ul></div>'

def _mega():
    cols = []
    for d in DIVISIONS:
        subs = ''.join(f'<li><a href="~/{s}/">{esc(n)}</a></li>' for s, n in d['subs'])
        cols.append(f'''<div class="mega__col">
          <a class="mega__head" href="~/{d['slug']}/"><span class="icon-tile sm {d['tile']}"><i class="bi {d['icon']}"></i></span><span>{esc(d['menu'])}</span></a>
          <ul><li><a href="~/{d['slug']}/" class="mega__all">{esc(d['all'])} <i class="bi bi-arrow-right"></i></a></li>{subs}</ul>
        </div>''')
    return f'''<div class="nav__drop nav__mega" id="dd-services">
        <div class="mega__grid">{''.join(cols)}</div>
        <div class="mega__foot">
          <p><b>Not sure which service you need?</b> Tell us about your project and we will recommend the right mix.</p>
          <a href="~/get-a-quote/" class="btn-x btn-grad">Discuss Your Project <span class="ico"><i class="bi bi-arrow-up-right"></i></span></a>
        </div>
      </div>'''

def header(active):
    def item(key, label, href, drop=None):
        cur = ' aria-current="page"' if active == key else ''
        cls = ' is-active' if active == key else ''
        if not drop:
            return f'<li class="nav__item{cls}"><a class="nav__link" href="~/{href}"{cur}>{label}</a></li>'
        did, dhtml, mega = drop
        return (f'<li class="nav__item has-drop{" has-mega" if mega else ""}{cls}">'
                f'<a class="nav__link" href="~/{href}"{cur}>{label}</a>'
                f'<button class="nav__caret" type="button" aria-expanded="false" aria-controls="{did}" aria-label="{label} menu"><i class="bi bi-chevron-down"></i></button>'
                f'{dhtml}</li>')
    menu = ''.join([
        item('home', 'Home', ''),
        item('about', 'About Us', 'about-us/', ('dd-about', _drop('dd-about', ABOUT_MENU), False)),
        item('services', 'Services', 'services/', ('dd-services', _mega(), True)),
        item('work', 'Our Work', 'portfolio/', ('dd-work', _drop('dd-work', WORK_MENU), False)),
        item('blog', 'Blog', 'blog/'),
        item('careers', 'Join Our Team', 'careers/', ('dd-careers', _drop('dd-careers', CAREER_MENU), False)),
        item('contact', 'Contact Us', 'contact-us/'),
    ])
    return f'''  <a class="skip-link" href="#main">Skip to content</a>
  <header class="nav">
    <div class="container-x">
      <nav class="nav__bar" aria-label="Main">
        <a href="~/" class="brand" aria-label="{esc(SITE['name'])} — home">
          <img decoding="async" src="~/assets/img/logo-mark.webp" alt="" width="37" height="40">
          <span class="brand__text"><b>Playback</b><small>Media &amp; Events Hub</small></span>
        </a>
        <ul class="nav__menu">{menu}</ul>
        <div class="nav__cta">
          <a href="~/get-a-quote/" class="btn-x btn-quote">Get a Quote <span class="ico"><i class="bi bi-arrow-right"></i></span></a>
          <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span></button>
        </div>
      </nav>
    </div>
  </header>
{mobile_menu()}'''

def _mm_group(id_, label, href, inner, level=1):
    return f'''<li class="mm__group mm__group--l{level}">
          <div class="mm__row"><a class="mm__link" href="~/{href}">{label}</a><button class="mm__toggle" type="button" aria-expanded="false" aria-controls="{id_}" aria-label="Show {label} links"><i class="bi bi-chevron-down"></i></button></div>
          <div class="mm__sub" id="{id_}"><ul>{inner}</ul></div>
        </li>'''

def mobile_menu():
    li = lambda label, href: f'<li><a class="mm__sublink" href="~/{href}">{esc(label)}</a></li>'
    about = ''.join(li(a, b) for a, b, *_ in [ABOUT_MENU[0], ABOUT_MENU[2], ABOUT_MENU[1], ABOUT_MENU[4]])
    services = ''
    for d in DIVISIONS:
        inner = li(d['all'], d['slug'] + '/') + ''.join(li(n, s + '/') for s, n in d['subs'])
        services += _mm_group('mm-' + d['key'], esc(d['name'] if d['key'] != 'events' else 'Event Management'), d['slug'] + '/', inner, 2)
    careers = li('Careers', 'careers/') + li('Current Openings', 'careers/#openings') + li('Freelancer Registration', 'freelancers/')
    return f'''  <div class="mobile-menu" id="mobile-menu" aria-hidden="true">
    <nav class="mm" aria-label="Mobile">
      <ul class="mm__list">
        <li><a class="mm__link" href="~/">Home</a></li>
        {_mm_group('mm-about', 'About Us', 'about-us/', about)}
        {_mm_group('mm-services', 'Services', 'services/', services)}
        <li><a class="mm__link" href="~/portfolio/">Our Work</a></li>
        <li><a class="mm__link" href="~/blog/">Blog</a></li>
        {_mm_group('mm-careers', 'Join Our Team', 'careers/', careers)}
        <li><a class="mm__link" href="~/contact-us/">Contact Us</a></li>
      </ul>
      <a href="~/get-a-quote/" class="btn-x btn-grad mm__quote">Get a Quote <span class="ico"><i class="bi bi-arrow-up-right"></i></span></a>
      <div class="mobile-menu__foot">
        <span>Say hello</span>
        <a href="tel:{SITE['phone1_tel']}">{SITE['phone1_disp']}</a>
        <a href="mailto:{SITE['email']}">{SITE['email']}</a>
      </div>
    </nav>
  </div>'''

def footer():
    ql = [('Home', ''), ('About Us', 'about-us/'), ('Meet Our Team', 'meet-the-team/'), ('Our Work', 'portfolio/'),
          ('Blog', 'blog/'), ('Join Our Team', 'careers/'), ('Contact Us', 'contact-us/')]
    media = [('Photography', 'photography/'), ('Corporate Photography', 'corporate-photography/'), ('Video Production', 'video-production/'),
             ('Corporate Films', 'corporate-films/'), ('Advertising Films', 'advertising-films/'), ('Video Editing', 'video-editing/'),
             ('Digital Marketing', 'digital-marketing/'), ('SEO Services', 'seo-services/'), ('Website Development', 'website-development/')]
    events = [('Event Management', 'event-management/'), ('Corporate Events', 'corporate-events/'), ('Medical Conferences', 'medical-conference-management/'),
              ('AV Production', 'audio-visual-production/'), ('Exhibition Stalls', 'exhibition-stalls-branding/'), ('Live Streaming', 'live-streaming/'),
              ('Event Branding', 'exhibition-stalls-branding/')]
    col = lambda items: ''.join(f'<li><a href="~/{h}">{esc(l)}</a></li>' for l, h in items)
    socials = ''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="bi {i}"></i></a>' for n, i, u in SITE['socials'])
    return f'''  <footer class="footer">
    <div class="container-x">
      <div class="footer__grid">
        <div class="footer__about">
          <a href="~/" class="brand"><img decoding="async" src="~/assets/img/logo-mark.webp" alt="" width="37" height="40"><span class="brand__text"><b>Playback</b><small>Media &amp; Events Hub</small></span></a>
          <p>A professional photography, videography, digital marketing, and event management company based in Delhi NCR.</p>
          <p class="footer__tag serif grad-text">{esc(SITE['tagline'])}</p>
          <div class="socials">{socials}</div>
        </div>
        <div><h2 class="footer__h">Quick Links</h2><ul>{col(ql)}</ul></div>
        <div><h2 class="footer__h">Media &amp; Digital</h2><ul>{col(media)}</ul></div>
        <div><h2 class="footer__h">Events &amp; Production</h2><ul>{col(events)}</ul></div>
        <div class="footer__contact">
          <h2 class="footer__h">Contact</h2>
          <ul>
            <li><b>{esc(SITE['name'])}</b><br>{esc(SITE['location'])}</li>
            <li><a href="tel:{SITE['phone1_tel']}">{SITE['phone1_disp']}</a></li>
            <li><a href="tel:{SITE['phone2_tel']}">{SITE['phone2_disp']}</a></li>
            <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
            <li><a href="{SITE['socials'][0][2]}" target="_blank" rel="noopener">Instagram: {SITE['instagram_handle']}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__word" aria-hidden="true">Playback</div>
      <div class="footer__sub" aria-hidden="true">Media &amp; Events Hub</div>
    </div>
    <div class="container-x">
      <div class="footer__bottom">
        <span>© <span data-year>2026</span> {esc(SITE['name'])}. All rights reserved.</span>
        <span><a href="~/privacy-policy/">Privacy Policy</a> · <a href="~/terms-conditions/">Terms &amp; Conditions</a></span>
      </div>
    </div>
  </footer>
  <a href="{wa_link()}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="bi bi-whatsapp"></i></a>'''


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------
def page(path, *, title, desc, body, active='', og_image='assets/img/hero-dance.webp', crumbs=None,
         schema=None, home=False, swiper=False, body_class=''):
    """Return (path, html). `path` is '' for the homepage or 'about-us/' etc."""
    canonical = SITE['url'] + '/' + path
    # keep titles inside search-result width: shorten the brand suffix on long titles
    for long_sfx in (' | Our Work | Playback Media & Events Hub', ' | Playback Media & Events Hub', ' | Our Work | Playback'):
        if len(title) > 66 and title.endswith(long_sfx):
            title = title[: -len(long_sfx)] + ' | Playback'
    if len(title) > 66 and ' | ' in title:
        title = title.split(' | ')[0]
    ld = []
    if crumbs:
        items = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE['url'] + '/'}]
        for i, (name, href) in enumerate(crumbs, start=2):
            entry = {'@type': 'ListItem', 'position': i, 'name': name}
            if href is not None:
                entry['item'] = SITE['url'] + '/' + href
            else:
                entry['item'] = canonical
            items.append(entry)
        ld.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items})
    for s in (schema or []):
        ld.append(s)
    ld_html = ''.join(f'\n  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    pre = ''
    if home:
        pre = '''
  <div class="preloader" aria-hidden="true">
    <div class="preloader__inner">
      <div class="preloader__word"><span>Playback</span></div>
      <div class="preloader__meta"><span>Create · Connect · Grow</span><span class="preloader__count">0</span></div>
    </div>
    <div class="preloader__bar"></div>
  </div>'''
    cls = ' '.join(c for c in [('is-loading' if home else ''), body_class] if c)
    swiper_js = '  <script defer src="~/assets/vendor/swiper-bundle.min.js"></script>\n' if swiper else ''
    scripts = SCRIPTS.format(swiper=swiper_js)
    robots_meta = '\n  <meta name="robots" content="noindex, nofollow">' if PREVIEW else ''
    doc = f'''<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{canonical}">{robots_meta}
  <meta name="theme-color" content="#110e24">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{esc(SITE['name'])}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image if og_image.startswith('http') else SITE['url'] + '/' + og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" sizes="32x32" href="~/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="~/assets/img/apple-touch-icon.png">
{CDN_CSS}
{SWIPER_CSS if swiper else ''}
  <link rel="stylesheet" href="~/assets/css/style.css">
  <script>document.documentElement.classList.add('js');try{{if(sessionStorage.getItem('pb_intro')==='1'||!matchMedia('(pointer:fine) and (min-width:992px)').matches)document.documentElement.classList.add('pb-seen')}}catch(e){{}}</script>{ld_html}
</head>
<body{f' class="{cls}"' if cls else ''}>{pre}
  <div class="cursor" data-label=""></div>
  <div class="cursor-dot"></div>
{header(active)}
  <main id="main"{' class="page"' if not home else ''}>
{body}
  </main>
{footer()}
{scripts}
</body>
</html>
'''
    return path, render(doc, path)

_IMG_SIZES = {}
def _img_size(rel):
    if rel not in _IMG_SIZES:
        try:
            with Image.open(os.path.join(SITE_ROOT, rel)) as im:
                _IMG_SIZES[rel] = im.size
        except OSError:
            _IMG_SIZES[rel] = None
    return _IMG_SIZES[rel]

def _size_imgs(doc):
    # Give every local <img> its real width/height so the layout never jumps while photos load
    def fix(m):
        tag = m.group(0)
        if ' width=' in tag:
            return tag
        src = re.search(r'(?:data-src|src)="~/([^"]+)"', tag) if 'data-src="~/' in tag else re.search(r'src="~/([^"]+)"', tag)
        size = src and _img_size(src.group(1))
        return tag.replace('<img ', f'<img width="{size[0]}" height="{size[1]}" ', 1) if size else tag
    return re.sub(r'<img [^>]*>', fix, doc)

def render(doc, path):
    doc = _size_imgs(doc)
    depth = path.count('/')
    root = '../' * depth
    doc = doc.replace('"~/"', '"' + (root or './') + '"')
    doc = doc.replace('"~/', '"' + root).replace("'~/", "'" + root).replace('(~/', '(' + root)
    return doc


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------
def crumbs_html(crumbs):
    if not crumbs:
        return ''
    parts = ['<li><a href="~/">Home</a></li>']
    for name, href in crumbs:
        if href is None:
            parts.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            parts.append(f'<li><a href="~/{href}">{esc(name)}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>'

def btn(label, href, kind='grad', icon='bi-arrow-up-right', ext=False, attrs=''):
    cls = {'grad': 'btn-x btn-grad', 'ghost': 'btn-x btn-ghost', 'dark': 'btn-x', 'light': 'btn-x btn-light'}[kind]
    target = ' target="_blank" rel="noopener"' if ext else ''
    h = href if (href.startswith('http') or href.startswith('tel:') or href.startswith('mailto:') or href.startswith('#')) else '~/' + href
    return f'<a href="{h}" class="{cls}"{target}{attrs}>{label} <span class="ico"><i class="bi {icon}"></i></span></a>'

def phero(*, eyebrow, title, sub=None, lead=None, actions='', media=None, crumbs=None, chip=None, compact=False, media_html=None):
    """Inner-page hero. `title` may contain a <span class="serif grad-text"> accent."""
    media_html = ''
    if media:
        chip_html = ''
        if chip:
            chip_html = f'<div class="float-chip phero__chip" data-float><span class="tile" style="background:var(--grad-warm)"><i class="bi {chip[0]}"></i></span><div><b>{chip[1]}</b><small>{chip[2]}</small></div></div>'
        media_html = f'''<div class="phero__media" data-hero-fade>
          <div class="ribbon" data-ribbon="page"></div>
          <figure class="phero__img"><img src="~/{media}" alt="" decoding="async" fetchpriority="high"></figure>
          {chip_html}
        </div>'''
    elif media_html:
        media_html = f'<div class="phero__media phero__media--video" data-hero-fade><div class="ribbon" data-ribbon="page"></div>{media_html}</div>'
    else:
        media_html = '<div class="ribbon phero__ribbon-solo" data-ribbon="page-solo"></div>'
    has_media = bool(media) or 'phero__media--video' in media_html
    return f'''    <section class="phero{' phero--media' if has_media else ''}{' phero--compact' if compact else ''}">
      <div class="hero__grain"></div>
      <div class="container-x">
        {crumbs_html(crumbs)}
        <div class="phero__grid">
          <div class="phero__copy">
            <span class="eyebrow" data-hero-fade>{eyebrow}</span>
            <h1 class="phero__title" data-hero-title>{title}</h1>
            {f'<p class="phero__sub" data-hero-fade>{sub}</p>' if sub else ''}
            {f'<p class="phero__lead" data-hero-fade>{lead}</p>' if lead else ''}
            {f'<div class="hero__actions" data-hero-fade>{actions}</div>' if actions else ''}
          </div>
          {media_html}
        </div>
      </div>
    </section>'''

def shead(eyebrow, title, lead=None, center=False, light=False):
    return f'''<div class="shead{' shead--center' if center else ''}{' shead--light' if light else ''}">
          <div><span class="eyebrow reveal">{eyebrow}</span><h2 class="section-title mt-3 reveal">{title}</h2></div>
          {f'<p class="section-lead reveal">{lead}</p>' if lead else ''}
        </div>'''

def icon_card(icon, title, text, href=None, tile='', link_label='Learn more', extra=''):
    link = f'<a href="~/{href}" class="link-arrow mt-3">{link_label} <i class="bi bi-arrow-right"></i></a>' if href else ''
    return f'''<article class="ccard reveal">
            <span class="icon-tile sm {tile}"><i class="bi {icon}"></i></span>
            <h3>{title}</h3>
            <p>{text}</p>{extra}
            {link}
          </article>'''

def img_card(img, title, text, href=None, label='Explore', tag=None):
    a_open = f'<a href="~/{href}" class="icard reveal">' if href else '<article class="icard reveal">'
    a_close = '</a>' if href else '</article>'
    tag_html = f'<span class="media-tag">{tag}</span>' if tag else ''
    more = f'<span class="link-arrow">{label} <i class="bi bi-arrow-right"></i></span>' if href else ''
    return f'''{a_open}
            <figure class="icard__img">{tag_html}<img src="~/{img}" alt="" loading="lazy" decoding="async"></figure>
            <div class="icard__body"><h3>{title}</h3><p>{text}</p>{more}</div>
          {a_close}'''

STEP_ICONS = ['bi-search', 'bi-clipboard-check', 'bi-camera-reels', 'bi-play-circle', 'bi-send-check', 'bi-trophy']

def steps(items, icons=None):
    icons = icons or STEP_ICONS
    out = []
    for i, (t, d) in enumerate(items):
        out.append(f'''<div class="step reveal">
            <div class="step__node"><span></span></div>
            <div><h3>{t}</h3><div class="step__no">Step {i + 1:02d}</div></div>
            <div class="step__card"><span class="icon-tile xs{' violet' if i % 2 else ''}"><i class="bi {icons[i % len(icons)]}"></i></span>{d}</div>
          </div>''')
    return f'''<div class="journey" style="--n:{len(items)}">
          <div class="journey__line"><i></i></div>
          {''.join(out)}
        </div>'''

def faq(items):
    return '<div class="faq">' + ''.join(
        f'<details class="faq__item reveal"><summary><span>{q}</span><i class="bi bi-plus-lg" aria-hidden="true"></i></summary><div class="faq__a"><p>{a}</p></div></details>'
        for q, a in items) + '</div>'

def faq_schema(items):
    import re
    strip = lambda s: re.sub(r'<[^>]+>', '', s)
    return {'@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in items]}

def gallery(images_sm, alt_prefix='Project photograph', limit=None):
    imgs = images_sm[:limit] if limit else images_sm
    items = ''.join(
        f'<a class="gallery__item reveal" href="~/{s.replace("-sm.webp", ".webp")}" data-lightbox aria-label="{esc(alt_prefix)} {i + 1}, open larger">'
        f'<img src="~/{s}" alt="{esc(alt_prefix)} {i + 1}" loading="lazy" decoding="async"></a>'
        for i, s in enumerate(imgs))
    return f'<div class="gallery" data-gallery>{items}</div>'

def vcard(vid, title=None, cats=None, sub=None, big=False):
    v = VIDEO_BY_ID.get(vid)
    title = title or (v[1] if v else 'Video')
    data_cats = f' data-cats="{" ".join(cats)}"' if cats else ''
    return f'''<button type="button" class="vcard reveal{' vcard--big' if big else ''}" data-yt="{vid}" data-title="{esc(title)}"{data_cats}>
            <span class="vcard__thumb"><img src="{yt_thumb(vid)}" alt="" loading="lazy" decoding="async"><span class="vcard__play"><i class="bi bi-play-fill"></i></span></span>
            <span class="vcard__text"><span class="vcard__title">{esc(title)}</span>{f'<small>{esc(sub)}</small>' if sub else ''}</span>
          </button>'''

def vgrid(ids, cols=3):
    return f'<div class="vgrid" style="--cols:{cols}">' + ''.join(vcard(i) for i in ids) + '</div>'

def chips(items):
    return '<div class="tags">' + ''.join(f'<span>{esc(t)}</span>' for t in items) + '</div>'

def checklist(items, cols=1):
    return f'<ul class="checks" style="--cols:{cols}">' + ''.join(f'<li><i class="bi bi-check2-circle"></i><span>{t}</span></li>' for t in items) + '</ul>'

def filters(items, target, active='all'):
    btns = ''.join(
        f'<button type="button" class="chip{" is-active" if k == active else ""}" data-filter="{k}" aria-pressed="{"true" if k == active else "false"}">{esc(l)}</button>'
        for k, l in items)
    return f'<div class="filters reveal" role="group" aria-label="Filter" data-filter-for="{target}">{btns}</div>'


# ---------------------------------------------------------------------------
# Forms (front-end: validation, spam honeypot, UTM capture; endpoint configured in main.js)
# ---------------------------------------------------------------------------
def field(name, label, kind='text', required=False, full=False, options=None, placeholder='', attrs='', help_=None, accept=None):
    req = ' required' if required else ''
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">(optional)</span>'
    fid = 'f-' + name.replace('_', '-')
    ph = f' placeholder="{esc(placeholder)}"' if placeholder else ''
    if kind == 'select':
        opts = '<option value="">Select…</option>' + ''.join(f'<option>{esc(o)}</option>' for o in options)
        ctrl = f'<select id="{fid}" name="{name}"{req}{attrs}>{opts}</select>'
    elif kind == 'textarea':
        ctrl = f'<textarea id="{fid}" name="{name}" rows="5"{req}{ph}{attrs}></textarea>'
    elif kind == 'file':
        ctrl = f'<input id="{fid}" name="{name}" type="file"{req} accept="{accept or ".pdf,.doc,.docx"}"{attrs}>'
    else:
        auto = {'email': ' autocomplete="email"', 'tel': ' autocomplete="tel" inputmode="tel"'}.get(kind, '')
        if name in ('name', 'full_name'):
            auto = ' autocomplete="name"'
        ctrl = f'<input id="{fid}" name="{name}" type="{kind}"{req}{ph}{auto}{attrs}>'
    hp = f'<small class="field__help">{help_}</small>' if help_ else ''
    return f'<div class="field{" field--full" if full else ""}"><label for="{fid}">{label}{star}</label>{ctrl}{hp}<small class="field__err" aria-live="polite"></small></div>'

def form(kind, fields_html, submit, *, dark=False, consent=None, success=None, error=None, files=False, extra=''):
    consent = consent or 'I agree to Playback Media &amp; Events Hub storing and using these details to respond to my enquiry, as described in the <a href="~/privacy-policy/">Privacy Policy</a>.'
    success = success or ('Thank You for Contacting Playback!', 'Your enquiry has been submitted successfully. Our team will review the information and contact you regarding your requirements.')
    error = error or ("We Couldn't Submit Your Enquiry.", f"Please check your information and try again. You can also contact us directly at {SITE['phone1']}.")
    enc = ' enctype="multipart/form-data"' if files else ''
    return f'''<form class="pb-form{' pb-form--dark' if dark else ''}" data-form="{kind}" novalidate{enc}
              data-success-title="{esc(success[0])}" data-success-text="{esc(success[1])}"
              data-error-title="{esc(error[0])}" data-error-text="{esc(error[1])}">
            <div class="pb-form__grid">{fields_html}</div>
            {extra}
            <div class="hp-field" aria-hidden="true"><label>Leave this field empty<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label></div>
            <input type="hidden" name="form_type" value="{kind}">
            <input type="hidden" name="source_page" value="">
            <input type="hidden" name="utm" value="">
            <label class="check"><input type="checkbox" name="consent" required><span>{consent}</span></label>
            <small class="field__err consent-err" aria-live="polite"></small>
            <div class="pb-form__actions">
              <button class="btn-x btn-grad" type="submit"><span class="btn-label">{submit}</span> <span class="ico"><i class="bi bi-send-fill"></i></span></button>
              <span class="pb-form__note">We respond to genuine enquiries; your details are never sold.</span>
            </div>
            <div class="form-status" role="status" aria-live="polite" tabindex="-1"></div>
          </form>'''

def enquiry_form(service=None, dark=True, kind='enquiry'):
    opts = list(SERVICE_OPTIONS)
    f = (field('name', 'Full Name', required=True, placeholder='Your name')
         + field('email', 'Email Address', 'email', required=True, placeholder='you@company.com')
         + field('mobile', 'Mobile Number', 'tel', required=True, placeholder='+91')
         + field('service', 'Service Interested In', 'select', required=True, options=opts)
         + field('message', 'Message / Requirement', 'textarea', required=True, full=True, placeholder='Tell us briefly about your project'))
    html_ = form(kind, f, 'Send Your Enquiry', dark=dark)
    if service:
        html_ = html_.replace(f'<option>{esc(service)}</option>', f'<option selected>{esc(service)}</option>', 1)
    return html_

def cta_band(title, text, buttons, form_html=None, eyebrow="Let's work together", id_=None):
    has = ' has-form' if form_html else ''
    return f'''    <section class="cta"{f' id="{id_}"' if id_ else ''}>
      <div class="container-x">
        <div class="cta__card{has}">
          <div class="cta__glow"></div>
          <div class="ribbon ribbon--dark" data-ribbon="cta"></div>
          <div class="cta__content">
            <span class="eyebrow" style="color:rgba(255,255,255,.7)">{eyebrow}</span>
            <h2 class="mt-3 reveal">{title}</h2>
            <p class="reveal">{text}</p>
            <div class="cta__actions reveal">{buttons}</div>
            <div class="cta__contact reveal">
              <div>Call<a href="tel:{SITE['phone1_tel']}">{SITE['phone1_disp']}</a></div>
              <div>Email<a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
            </div>
          </div>
          {f'<div class="cta__form reveal">{form_html}</div>' if form_html else ''}
        </div>
      </div>
    </section>'''
