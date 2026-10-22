"""Homepage and main corporate pages."""
import datetime as dt
from core import (page, phero, shead, icon_card, img_card, steps, faq, gallery, vcard, vgrid, chips, checklist, filters,
                  cta_band, enquiry_form, btn, esc, field, form)
from data import (SITE, DIVISIONS, SUPPORTING, CLIENTS, TESTIMONIALS, VIDEO_TESTIMONIALS, TEAM, VIDEOS, VIDEO_CATS, VIDEO_BY_ID,
                  SHOWREEL_ID, PROJECTS, PROJECT_BY_SLUG, PORTFOLIO_CATS, HOME_FILTERS, CAT_LABEL, INDUSTRIES, JOBS, CAREER_CATEGORIES,
                  SERVICE_OPTIONS, project_images, project_cover, cat_labels, wa_link, yt_thumb)
from blog import POSTS, BLOG_CATS, BLOG_CAT_LABEL

ORG_SCHEMA = {
    '@context': 'https://schema.org', '@type': 'LocalBusiness', 'name': SITE['name'], 'url': SITE['url'] + '/',
    'logo': SITE['url'] + '/assets/img/logo.png', 'image': SITE['url'] + '/assets/img/hero-dance.webp',
    'email': SITE['email'], 'telephone': SITE['phone1'], 'slogan': SITE['tagline'],
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Ghaziabad', 'addressRegion': 'Uttar Pradesh', 'addressCountry': 'IN'},
    'areaServed': SITE['region'], 'sameAs': [s[2] for s in SITE['socials']],
}

def fmt_date(iso):
    d = dt.date.fromisoformat(iso)
    return d.strftime('%d %B %Y').lstrip('0')

def read_time(html_):
    import re
    words = len(re.sub(r'<[^>]+>', ' ', html_).split())
    return max(2, round(words / 220))

# ---------------------------------------------------------------------------
# Shared cards
# ---------------------------------------------------------------------------
def project_card(p, wide=False):
    cover = project_cover(p)
    labels = cat_labels(p)
    meta = ' · '.join(x for x in [p.get('client'), p.get('location'), p.get('year')] if x)
    if cover:
        src = cover if cover.startswith('http') else '~/' + cover
        vbadge = '<span class="pcard__vid"><i class="bi bi-play-fill"></i></span>' if not p['images'] and p['videos'] else ''
        fig = f'<figure class="pcard__img"><img src="{src}" alt="" loading="lazy" decoding="async">{vbadge}</figure>'
    else:
        fig = f'<figure class="pcard__img pcard__img--type"><i class="bi {p.get("type_icon", "bi-stars")}"></i><span>{esc(p.get("category_label", labels))}</span></figure>'
    return f'''<a class="pcard reveal" href="~/portfolio/{p['slug']}/" data-cats="{' '.join(p['cats'])}">
            {fig}
            <div class="pcard__body"><small>{esc(labels)}</small><h3>{esc(p['title'])}</h3>{f'<span class="pcard__meta">{esc(meta)}</span>' if meta else ''}</div>
            <span class="go" aria-hidden="true"><i class="bi bi-arrow-up-right"></i></span>
          </a>'''

def blog_card(p):
    return f'''<a class="bcard reveal" href="~/blog/{p['slug']}/" data-cats="{p['cat']}">
            <figure class="bcard__img"><img src="~/{p['image']}" alt="" loading="lazy" decoding="async"><span class="bcard__cat">{esc(BLOG_CAT_LABEL[p['cat']])}</span></figure>
            <div class="bcard__body">
              <small><time datetime="{p['date']}">{fmt_date(p['date'])}</time> · {read_time(p['body'])} min read</small>
              <h3>{esc(p['title'])}</h3>
              <p>{esc(p['excerpt'])}</p>
              <span class="link-arrow">Read article <i class="bi bi-arrow-right"></i></span>
            </div>
          </a>'''

def team_card(t, lead=False):
    paras = t['bio'] if lead else t['bio'][:2]
    bio = ''.join(f'<p>{esc(b)}</p>' for b in paras)
    return f'''<article class="tcard{' tcard--lead' if lead else ''} reveal" id="{t['slug']}">
            <figure class="tcard__img"><img src="~/assets/img/team/{t['slug']}.webp" alt="Portrait of {esc(t['name'])}" loading="lazy" decoding="async"></figure>
            <div class="tcard__body"><h3>{esc(t['name'])}</h3><span class="tcard__role">{esc(t['role'])}</span>{bio}</div>
          </article>'''

def logos_grid():
    return '<div class="logos">' + ''.join(
        f'<figure class="logo-card reveal"><img src="~/assets/img/clients/{s}.webp" alt="{esc(n)}" loading="lazy" decoding="async"></figure>' for s, n in CLIENTS) + '</div>'

def logos_marquee():
    items = ''.join(f'<span class="logo-chip"><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="~/assets/img/clients/{s}.webp" alt="{esc(n)}" width="355" height="193" loading="lazy" decoding="async"></span>' for s, n in CLIENTS)
    return f'<div class="marquee" style="--dur:60s"><div class="marquee__track marquee__track--logos">{items}</div></div>'

def person_av(t):
    if t.get('photo'):
        return f'<img class="person__av person__av--img" src="~/assets/img/people/{t["photo"]}.webp" alt="" loading="lazy" decoding="async">'
    ini = ''.join(w[0] for w in t['name'].replace('Dr. ', '').split()[:2])
    return f'<span class="person__av">{ini}</span>'

def voices_section(title='Relationships Built on <span class="serif grad-text">Trust.</span>', eyebrow='Client testimonials', video=True, sid='voices'):
    slides = ''.join(f'''<div class="swiper-slide">
              <p class="quote">{esc(t['text'])}</p>
              <div class="person">{person_av(t)}<div><b>{esc(t['name'])}</b><small>{esc(t['role'])} · {esc(t['org'])}</small></div></div>
            </div>''' for t in TESTIMONIALS)
    vt = ''
    if video:
        vt = '<div class="vtest"><h3 class="vtest__title reveal">Video testimonials</h3><div class="vgrid" style="--cols:3">' + ''.join(
            vcard(v, f'{n}', sub=o) for v, n, o in VIDEO_TESTIMONIALS) + '</div></div>'
    return f'''    <section class="section voices" id="{sid}">
      <div class="ribbon ribbon--l" data-ribbon="voice-l"></div>
      <div class="ribbon ribbon--r" data-ribbon="voice-r"></div>
      <div class="container-x">
        <span class="eyebrow reveal">{eyebrow}</span>
        <h2 class="voices__title mt-3 reveal">{title}</h2>
        <div class="swiper reveal">
          <div class="swiper-wrapper">{slides}</div>
        </div>
        <div class="voices__nav">
          <button class="voices__prev" type="button" aria-label="Previous testimonial"><i class="bi bi-arrow-left"></i></button>
          <div class="swiper-pagination"></div>
          <button class="voices__next" type="button" aria-label="Next testimonial"><i class="bi bi-arrow-right"></i></button>
        </div>
        {vt}
      </div>
    </section>'''

def stats_grid():
    st = [('15', '+', 'Years', 'Industry experience'), ('1000', '+', '', 'Clients served'), ('500', '+', '', 'Television episodes'), ('50', '+', '', 'Medical conference assignments')]
    cells = ''.join(f'''<div class="stat reveal"><div class="stat__num"><span data-count="{n}">{int(n):,}</span><sup class="grad-text">{s}</sup></div><p>{l}</p></div>''' for n, s, _, l in st)
    return f'''<div class="stats__grid" style="--cols:4">{cells}</div>
        <p class="stats__note reveal"><i class="bi bi-info-circle"></i> Industry experience includes our founder&rsquo;s photography, filmmaking and television production work before the business was formally registered in {SITE['registered']}. Medical conference figures count assignments we have supported, not only events we managed end to end.</p>'''

def why_cards():
    items = [
        ('bi-camera-reels-fill', 'Established Media Production Experience', 'Photography, filmmaking and television production are where we began, and they still shape everything we do.', ''),
        ('bi-diagram-3-fill', 'Integrated Creative &amp; Digital Services', 'Photography, video, digital marketing and events coordinated by one accountable team.', 'violet'),
        ('bi-heart-pulse-fill', 'Corporate &amp; Healthcare Experience', 'Experience with businesses, institutions, hospitals and 50+ medical conference assignments.', 'rose'),
        ('bi-cpu-fill', 'Creative and Technical Understanding', 'We combine creative thinking with practical knowledge of cameras, AV, LED and production systems.', ''),
        ('bi-sliders', 'Customized Project Solutions', 'Every proposal is built around your objectives, audience, timeline and budget.', 'violet'),
        ('bi-people-fill', 'Professional Coordination', 'Clear communication and one point of contact from the first call to final delivery.', 'rose'),
    ]
    return '<div class="why6">' + ''.join(f'''<div class="glass why-item reveal">
              <span class="icon-tile {t}"><i class="bi {i}"></i></span>
              <div><h3>{h}</h3><p>{p}</p></div>
            </div>''' for i, h, p, t in items) + '</div>'

def why_panel(title, sid='why', sub=None):
    return f'''    <section class="why" id="{sid}">
      <div class="container-x">
        <div class="why__panel">
          <div class="ribbon ribbon--l" data-ribbon="side-l"></div>
          <div class="ribbon ribbon--r" data-ribbon="side-r"></div>
          <span class="eyebrow eyebrow--center reveal">Why choose Playback</span>
          <h2 class="why__title reveal">{title}</h2>
          {f'<p class="why__lead reveal">{sub}</p>' if sub else ''}
          {why_cards()}
        </div>
      </div>
    </section>'''

HOME_PROCESS = [('Discover', 'We listen to your goals, audience, timeline and budget, and recommend the right mix of services.'),
                ('Plan', 'Concepts, scripts, shot lists, production schedules and resources, agreed before work begins.'),
                ('Create', 'Our photographers, filmmakers, designers and digital team produce the work.'),
                ('Execute', 'Shoots, campaigns and events delivered on the ground with our team present throughout.'),
                ('Deliver', 'Edited photographs, films, campaigns and reports, ready for every platform you use.')]

# ---------------------------------------------------------------------------
# HOMEPAGE (handover section 5)
# ---------------------------------------------------------------------------
def home():
    reel_slides = [
        ('assets/img/hero-dance-sm.webp', 'Stage performance under concert lighting', 'Event production', 'Stage &amp; spectacle'),
        ('assets/img/work/apccsm-medical-workshop/01-sm.webp', 'Medical workshop delegates receiving certificates', 'Medical conferences', 'CME &amp; workshop coverage'),
        ('assets/img/greenscreen-sm.webp', 'Executives at a green-screen film shoot', 'Filming', 'Corporate films'),
        ('assets/img/work/exhibition-stalls-sponsor-booths/01-sm.webp', 'Branded sponsor stall at a conference', 'Exhibitions', 'Stall production'),
        ('assets/img/portrait-fashion-sm.webp', 'Outdoor portrait photograph', 'Photography', 'Portraits &amp; brands'),
    ]
    act, lazy = ' class="is-active"', ' loading="lazy"'
    imgs = ''.join((f'<img decoding="async" src="~/{s}" alt="{a}"{act}' if i == 0 else f'<img decoding="async" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="~/{s}" alt="{a}"') + f' data-cat="{c}" data-title="{t}">' for i, (s, a, c, t) in enumerate(reel_slides))
    bars = '<i></i>' * len(reel_slides)
    hero = f'''    <section class="hero">
      <div class="hero__grain"></div>
      <div class="ribbon" data-ribbon="hero"></div>
      <div class="hero__content">
        <div class="container-x">
          <div class="hero__grid">
            <div>
              <span class="hero__badge" data-hero-fade><b>Delhi NCR</b> Welcome to Playback Media &amp; Events Hub</span>
              <h1 class="hero__title">
                <span class="line"><span>We Create.</span></span>
                <span class="line"><span>We Capture.</span></span>
                <span class="line"><span class="serif grad-text">We Connect.</span></span>
              </h1>
              <p class="hero__line" data-hero-fade><span>Photography</span><span>Videography</span><span>Digital Marketing</span><span>Event Management</span></p>
              <p class="hero__sub" data-hero-fade><strong>Turning ideas into exceptional visuals, compelling stories, powerful digital experiences, and memorable events.</strong> Playback Media &amp; Events Hub brings together creative production, digital expertise, and event execution to help businesses, brands, institutions, and professionals communicate, connect, and grow.</p>
              <div class="hero__actions" data-hero-fade>
                {btn('Explore Our Services', 'services/', 'grad', 'bi-arrow-up-right')}
                {btn('View Our Work', 'portfolio/', 'ghost', 'bi-grid-1x2-fill')}
              </div>
            </div>
            <div class="hero__visual" data-hero-visual>
              <div class="reel-card" data-cursor="view" data-cursor-label="Play">
                <div class="reel-card__progress">{bars}</div>
                {imgs}
                <button type="button" class="reel-card__play" data-yt="{SHOWREEL_ID}" data-title="Playback Showreel" aria-label="Watch the Playback showreel"><i class="bi bi-play-fill"></i><span>Watch showreel</span></button>
                <div class="reel-card__meta">
                  <div><small data-reel-cat>Event production</small><strong data-reel-title>Stage &amp; spectacle</strong></div>
                  <span class="reel-card__rec">REC</span>
                </div>
              </div>
              <div class="float-chip float-chip--a" data-float>
                <span class="tile" style="background:var(--grad-warm)"><i class="bi bi-people-fill"></i></span>
                <div><b><span data-count="1000">1,000</span>+</b><small>clients served</small></div>
              </div>
              <div class="float-chip float-chip--b" data-float>
                <span class="tile" style="background:var(--grad-rose)"><i class="bi bi-award-fill"></i></span>
                <div><b>15+ years</b><small>industry experience</small></div>
              </div>
              <div class="float-chip float-chip--c" data-float>
                <span class="tile" style="background:var(--grad-violet)"><i class="bi bi-camera-reels-fill"></i></span>
                <div><b>500+</b><small>television episodes</small></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container-x">
        <div class="hero__foot" data-hero-fade>
          <span class="scroll-cue"><span class="scroll-cue__mouse"></span>Scroll to explore</span>
          <div class="hero__services">
            <a href="~/photography/">Photography</a><a href="~/video-production/">Videography</a><a href="~/digital-marketing/">Digital Marketing</a><a href="~/event-management/">Event Management</a>
          </div>
        </div>
      </div>
    </section>'''

    trusted = f'''    <section class="clients" aria-labelledby="trusted-title">
      <div class="container-x clients__head">
        <h2 id="trusted-title" class="reveal">Trusted by Businesses, Brands &amp; <span class="serif grad-text">Professionals.</span></h2>
        <p class="reveal">We value the relationships built through our work with businesses, healthcare organizations, institutions, brands, and professionals across different industries.</p>
      </div>
      {logos_marquee()}
    </section>'''

    wall_a = [('stage-dancers', 'Dancers performing on a corporate stage'), ('portrait-saree', 'Portrait of a guest at a celebration'),
              ('booth-jewel', 'Jewellery exhibition booth'), ('keynote', 'Keynote speaker on stage'), ('cake', 'Celebration cake on a decorated stage')]
    wall_b = [('crowd-hands', 'Corporate audience raising their hands'), ('mother-baby', 'Mother holding her baby at a birthday shoot'),
              ('award', 'Award being presented on stage'), ('product-sofa', 'Product shoot of a sofa bed'), ('razzmatazz', 'Team on stage at a gala night')]
    fig = lambda lst: ''.join(f'<figure><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="~/assets/img/{s}-sm.webp" data-srcset="~/assets/img/{s}-xs.webp 480w, ~/assets/img/{s}-sm.webp 900w" sizes="(max-width: 767px) 48vw, 24vw" alt="{a}" loading="lazy" decoding="async"></figure>' for s, a in lst)
    about = f'''    <section class="section intro">
      <div class="container-x">
        <div class="intro__grid">
          <div class="intro__copy">
            <span class="eyebrow reveal">About Playback</span>
            <h2 class="intro__title mt-3 reveal">A Creative Journey. <span class="serif grad-text">A Complete Business Solution.</span></h2>
            <p class="intro__lead reveal">Playback Media &amp; Events Hub is a creative production, digital marketing, and event management company based in Delhi NCR.</p>
            <ol class="pillars">
              <li class="pillar reveal"><span class="pillar__no">01</span><div><strong>Where we began</strong><p>Our journey began with photography, videography, television production, and filmmaking.</p></div></li>
              <li class="pillar reveal"><span class="pillar__no">02</span><div><strong>How we grew</strong><p>As our expertise and client requirements evolved, we expanded into digital marketing, audiovisual production, and professional event management.</p></div></li>
              <li class="pillar reveal"><span class="pillar__no">03</span><div><strong>What we do today</strong><p>We bring these capabilities together to help clients create impactful content, strengthen their brand presence, and deliver memorable experiences.</p></div></li>
            </ol>
            <a href="~/about-us/" class="link-arrow mt-4 reveal">Know More About Us <i class="bi bi-arrow-right"></i></a>
          </div>
          <div class="intro__media reveal">
            <div class="wall">
              <div class="wall__col" data-wall="up"><div class="wall__track">{fig(wall_a)}</div></div>
              <div class="wall__col" data-wall="down"><div class="wall__track">{fig(wall_b)}</div></div>
              <span class="wall__tag"><i></i>On set across Delhi NCR</span>
            </div>
            <div class="seal" aria-hidden="true">
              <svg viewBox="0 0 200 200">
                <defs><path id="sealPath" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs>
                <text><textPath href="#sealPath" startOffset="0" textLength="474" lengthAdjust="spacing">CREATE · CONNECT · GROW · PLAYBACK ·</textPath></text>
              </svg>
              <span class="seal__core"><i class="bi bi-play-fill"></i></span>
            </div>
          </div>
        </div>
      </div>
    </section>'''

    counters = f'''    <section class="section stats">
      <div class="container-x">
        <div class="stats__intro">
          <div>
            <span class="eyebrow reveal">Company experience</span>
            <h2 class="section-title mt-3 reveal">Experience That Speaks <span class="serif grad-text">Through Our Work.</span></h2>
          </div>
          <p class="reveal">Hospitals, listed companies, institutions, government bodies, brands and professionals have trusted us with their most important visuals, campaigns and events.</p>
        </div>
        {stats_grid()}
      </div>
    </section>'''

    # 05 Core expertise: four equal stacked cards
    exp = [
        dict(n='01', tile='rose', icon='bi-camera-fill', title='<span class="serif">Photo</span>graphy', href='photography/', label='Explore Photography',
             text='Professional corporate, product, portfolio, event, healthcare, and commercial photography.',
             tags=['Corporate', 'Product &amp; commercial', 'Portfolio &amp; headshots', 'Events &amp; conferences', 'Healthcare'],
             media=('assets/img/baby-red.webp', 'Portrait photograph of a child in a red dress', 'assets/img/product-cookies.webp', 'bi-aperture', 'Portraits &amp; products')),
        dict(n='02', tile='violet', icon='bi-camera-reels-fill', title='Videography &amp; <span class="serif">Film Production</span>', href='video-production/', label='Explore Video Production',
             text='Corporate films, advertising videos, TV production, documentaries, interviews, promotional films, reels, and editing.',
             tags=['Corporate films', 'Advertising', 'TV &amp; documentary', 'Interviews &amp; reels', 'Editing'],
             media=('assets/img/keynote.webp', 'Keynote speaker filmed at a technology event', 'assets/img/greenscreen.webp', 'bi-record-circle', '500+ TV episodes')),
        dict(n='03', tile='violet', icon='bi-graph-up-arrow', title='Digital <span class="serif">Marketing</span>', href='digital-marketing/', label='Explore Digital Marketing',
             text='Social media marketing, SEO, digital advertising, websites, healthcare marketing, and online content.',
             tags=['Social media', 'SEO &amp; local SEO', 'Google &amp; Meta Ads', 'Websites', 'Healthcare marketing'], media='digital'),
        dict(n='04', tile='', icon='bi-stars', title='Event <span class="serif">Management</span>', href='event-management/', label='Explore Event Management',
             text='Corporate events, medical conferences, CME programs, AV production, stage setups, exhibitions, and event branding.',
             tags=['Corporate events', 'Medical conferences &amp; CMEs', 'AV &amp; stage', 'Exhibitions', 'Event branding'],
             media=('assets/img/milestones.webp', 'Speaker on stage at a corporate annual meet', 'assets/img/live-band.webp', 'bi-broadcast', 'Conferences &amp; stages')),
    ]
    cards = []
    for i, e in enumerate(exp):
        if e['media'] == 'digital':
            from services import dash_html
            media = f'''<div class="svc-card__media">
              <img decoding="async" src="~/assets/img/concert-crowd.webp" alt="Audience at a live event" loading="lazy" data-parallax>
              {dash_html()}
            </div>'''
        else:
            img, alt, mini, ic, tag = e['media']
            media = f'''<div class="svc-card__media">
              <span class="media-tag"><i class="bi {ic}"></i> {tag}</span>
              <img decoding="async" src="~/{img}" alt="{alt}" loading="lazy" data-parallax>
              <div class="mini"><img decoding="async" src="~/{mini.replace('.webp', '-sm.webp')}" alt="" loading="lazy"></div>
            </div>'''
        glow = ['rgba(216, 72, 60, .12)', 'rgba(60, 48, 144, .12)', 'rgba(120, 108, 168, .16)', 'rgba(204, 24, 36, .10)'][i]
        cards.append(f'''<article class="svc-card" style="--i:{i}; --glow: radial-gradient(circle, {glow}, transparent 65%)">
            <div class="svc-card__body">
              <div>
                <div class="svc-card__top"><span class="icon-tile {e['tile']}"><i class="bi {e['icon']}"></i></span><span class="svc-card__num">{e['n']}</span></div>
                <h3 class="mt-4">{e['title']}</h3>
                <p>{e['text']}</p>
              </div>
              <div>
                <div class="tags">{''.join(f'<span>{t}</span>' for t in e['tags'])}</div>
                <a href="~/{e['href']}" class="link-arrow mt-4">{e['label']} <i class="bi bi-arrow-right"></i></a>
              </div>
            </div>
            {media}
          </article>''')
    caps = ''.join(f'<span class="cap {c}"><i class="bi {i}"></i>{esc(t)}</span>' for i, t, c in SUPPORTING[:8])
    caps2 = ''.join(f'<span class="cap {c}"><i class="bi {i}"></i>{esc(t)}</span>' for i, t, c in SUPPORTING[8:])
    expertise = f'''    <section class="section services" id="services">
      <div class="container-x">
        <div class="services__head">
          <div>
            <span class="eyebrow reveal">Our core expertise</span>
            <h2 class="section-title mt-3 reveal">Four Core Strengths.<br><span class="serif grad-text">One Creative Partner.</span></h2>
          </div>
          <p class="section-lead reveal">Choose one service or bring them together. Each division has its own specialists, and they work as one team whenever your project needs them.</p>
        </div>
        <div class="svc-stack">{''.join(cards)}</div>
      </div>
    </section>
    <section class="caps" aria-label="Supporting services">
      <div class="container-x caps__head">
        <span class="eyebrow reveal">Supporting services</span>
        <h2 class="section-title mt-3 reveal" style="font-size:clamp(1.8rem,3.6vw,3rem)">Everything your project <span class="serif grad-text">needs to shine.</span></h2>
      </div>
      <div class="marquee" style="--dur:60s"><div class="marquee__track">{caps}</div></div>
      <div class="marquee marquee--rev" style="--dur:64s"><div class="marquee__track">{caps2}</div></div>
    </section>'''

    # 06 Featured portfolio (horizontal)
    feat = [p for p in PROJECTS if p['featured']]
    wcards = []
    for i, p in enumerate(feat):
        cover = project_cover(p, sm=False)
        wide = ' wide' if i % 2 == 0 else ''
        if cover:
            src = cover if cover.startswith('http') else '~/' + cover
            img = f'<img decoding="async" src="{src}" alt="" loading="lazy">'
        else:
            img = f'<div class="work-card__type"><i class="bi {p.get("type_icon", "bi-stars")}"></i></div>'
        sub = cat_labels(p)
        wcards.append(f'''<a href="~/portfolio/{p['slug']}/" class="work-card{wide}" data-cats="{' '.join(p['cats'])}" data-cursor="view" data-cursor-label="View">
            {img}
            <div class="work-card__info"><div><small>{esc(sub)}</small><h3>{esc(p['title'])}</h3></div><span class="go"><i class="bi bi-arrow-right"></i></span></div>
          </a>''')
    hf = ''.join(f'<button type="button" class="chip chip--dark{" is-active" if k == "all" else ""}" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{l}</button>' for k, l in HOME_FILTERS)
    portfolio = f'''    <section class="work" id="work">
      <div class="work__pin">
        <div class="container-x">
          <div class="work__head">
            <div>
              <span class="eyebrow">Featured portfolio</span>
              <h2 class="section-title mt-3">Our Work. Our Passion. <span class="serif grad-text">Our Identity.</span></h2>
            </div>
            <p class="section-lead">Explore selected assignments that reflect our passion for photography, filmmaking, digital communication, and professional event production.</p>
          </div>
          <div class="filters filters--dark" role="group" aria-label="Filter featured work" data-filter-for="#work-track">{hf}</div>
        </div>
        <div class="work__track" id="work-track">
          {''.join(wcards)}
          <div class="work-card work-card--end">
            <span class="eyebrow" style="color:#fff">See everything</span>
            <div>
              <h3>Explore the complete portfolio.</h3>
              <a href="~/portfolio/" class="btn-x mt-4" style="--bg:#fff;color:var(--ink)">Explore Complete Portfolio <span class="ico" style="background:rgba(20,18,23,.08)"><i class="bi bi-arrow-right"></i></span></a>
            </div>
          </div>
        </div>
        <div class="work__progress"><i></i></div>
      </div>
    </section>'''

    films = f'''    <section class="section showcase showcase--films">
      <div class="container-x">
        <div class="split split--media">
          <div class="showcase__copy">
            <span class="eyebrow reveal">Films &amp; video</span>
            <h2 class="section-title mt-3 reveal">Bringing Stories to Life, <span class="serif grad-text">Frame by Frame.</span></h2>
            <p class="section-lead reveal">From corporate films and advertising production to television programming and professional editing, visual storytelling remains a foundational strength of Playback.</p>
            <ul class="mini-stats reveal"><li><b>500+</b><span>TV episodes</span></li><li><b>70+</b><span>films in our showreel</span></li><li><b>13</b><span>video categories</span></li></ul>
            <div class="hero__actions reveal">{btn('Watch Our Showreel', 'showreel/', 'grad', 'bi-play-fill')}{btn('Video Production', 'video-production/', 'ghost')}</div>
          </div>
          <div class="showcase__media">
            {vcard(SHOWREEL_ID, 'Playback Showreel', big=True)}
            <div class="vgrid vgrid--mini" style="--cols:3">{vcard('eKAqUBHCgos', 'Aao Baniye Gursikh Pyara — TV')}{vcard('L6uL6tO5wFY', 'Engineers Ply — Corporate Film')}{vcard('z51spm2RWTw', 'Documentary on Bhai Vir Singh')}</div>
          </div>
        </div>
      </div>
    </section>'''

    digital = f'''    <section class="section showcase showcase--digital">
      <div class="container-x">
        <div class="split split--media split--rev">
          <div class="showcase__copy">
            <span class="eyebrow reveal">Digital marketing</span>
            <h2 class="section-title mt-3 reveal">Creative Content Meets <span class="serif grad-text">Digital Strategy.</span></h2>
            <p class="section-lead reveal">Playback combines its photography and video production background with digital marketing expertise to help brands communicate consistently and reach relevant audiences.</p>
            <div class="reveal">{chips(['Social media', 'SEO & local SEO', 'Google & Meta Ads', 'Websites', 'Healthcare marketing', 'Influencer marketing'])}</div>
            <div class="hero__actions reveal">{btn('Explore Digital Marketing', 'digital-marketing/', 'grad')}</div>
          </div>
          <div class="showcase__media">
            <div class="dmock reveal">
              <div class="svc-card__media dmock__browser" style="background:linear-gradient(135deg,#ecebf6,#fbe7e4)">
                <div class="lighthouse"><span>98</span><span>100</span></div>
                <div class="browser"><div class="browser__bar"><i></i><i></i><i></i><span>yourbrand.in</span></div>
                  <div class="browser__view"><div class="browser__copy"><b>Your brand,<br>beautifully online.</b><i class="sk"></i><i class="sk"></i><em></em></div>
                  <img src="~/assets/img/portrait-fashion-sm.webp" alt="" loading="lazy" decoding="async"></div></div>
              </div>
              <div class="dmock__phone"><img src="~/assets/img/work/flipkart-seller-hub-night/05-sm.webp" alt="" loading="lazy" decoding="async"><span class="dmock__reel"><i class="bi bi-play-fill"></i> Reel</span><span class="dmock__likes"><i class="bi bi-heart-fill"></i> Engagement</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>'''

    ev_imgs = [('assets/img/stage-spiral-sm.webp', 'LED stage at a partner summit'), ('assets/img/work/apccsm-medical-workshop/02-sm.webp', 'Medical workshop session'),
               ('assets/img/booth-tata-sm.webp', 'Branded exhibition counter'), ('assets/img/work/hcl-domino-jams/02-sm.webp', 'Branded registration desk')]
    events = f'''    <section class="section showcase showcase--events">
      <div class="container-x">
        <div class="split split--media">
          <div class="showcase__copy">
            <span class="eyebrow reveal">Events &amp; conferences</span>
            <h2 class="section-title mt-3 reveal">Thoughtfully Planned. <span class="serif grad-text">Professionally Produced.</span></h2>
            <p class="section-lead reveal">From medical conferences and corporate events to audiovisual systems and exhibition production, we coordinate creative and technical services to support successful professional gatherings.</p>
            {checklist(['Medical conferences &amp; CMEs', 'Corporate events &amp; launches', 'LED walls, sound &amp; stage', 'Exhibition stalls &amp; branding', 'Live streaming &amp; recording', 'Photography &amp; highlight films'], 2)}
            <div class="hero__actions reveal">{btn('Explore Event Management', 'event-management/', 'grad')}</div>
          </div>
          <div class="showcase__media">
            <div class="mosaic">{''.join(f'<figure class="mosaic__item reveal"><img src="~/{s}" alt="{a}" loading="lazy" decoding="async"></figure>' for s, a in ev_imgs)}</div>
          </div>
        </div>
      </div>
    </section>'''

    sect_items = ''.join(f'''<li class="sector reveal"><a href="~/{href}/" data-img="{i}">
            <img class="sector__thumb" src="~/{img}" alt="" loading="lazy" decoding="async">
            <span class="sector__no">{i + 1:02d}</span><span class="sector__name">{esc(n)}</span>
            <span class="sector__tags">{esc(t)}</span><span class="sector__go"><i class="bi bi-arrow-up-right"></i></span></a></li>''' for i, (n, t, href, img) in enumerate(INDUSTRIES))
    prev = ''.join(f'<img src="~/{img}" alt="" loading="lazy" decoding="async">' for *_, img in INDUSTRIES)
    industries = f'''    <section class="section sectors" id="industries">
      <div class="container-x">
        <div class="sectors__head">
          <div>
            <span class="eyebrow reveal">Industries we serve</span>
            <h2 class="section-title mt-3 reveal">Creative Solutions for <span class="serif grad-text">Diverse Industries.</span></h2>
          </div>
          <p class="section-lead reveal">Whether it&rsquo;s a hospital CME, a product launch or an institutional film, every brief gets the same dedicated team.</p>
        </div>
        <ul class="sector-list">{sect_items}</ul>
      </div>
      <div class="sector-preview" aria-hidden="true">{prev}</div>
    </section>'''

    process = f'''    <section class="section process" id="process">
      <div class="container-x">
        <div class="process__head">
          <div>
            <span class="eyebrow reveal">Our process</span>
            <h2 class="section-title mt-3 reveal">From Your Idea to the <span class="serif grad-text">Final Outcome.</span></h2>
          </div>
          <p class="section-lead reveal">Discover → Plan → Create → Execute → Deliver. A clear, collaborative journey with one point of contact throughout.</p>
        </div>
        {steps(HOME_PROCESS, ['bi-search', 'bi-clipboard-check', 'bi-camera-reels', 'bi-play-circle', 'bi-send-check'])}
      </div>
    </section>'''

    team = f'''    <section class="section team-preview">
      <div class="container-x">
        <div class="shead">
          <div><span class="eyebrow reveal">The people behind Playback</span><h2 class="section-title mt-3 reveal">Meet the Creative Minds <span class="serif grad-text">Behind Our Work.</span></h2></div>
          <div><p class="section-lead reveal">Every successful project is driven by talented people who bring their experience, creativity, technical understanding, and dedication together. Meet the professionals contributing to the creative vision and production expertise of Playback Media &amp; Events Hub.</p>
          <div class="reveal mt-4">{btn('Meet Our Team', 'meet-the-team/', 'dark', 'bi-arrow-right')}</div></div>
        </div>
        <div class="tgrid tgrid--4">{''.join(mini_team(t) for t in TEAM[:4])}</div>
      </div>
    </section>'''

    insights = f'''    <section class="section insights">
      <div class="container-x">
        {shead('Latest insights', 'Explore Ideas From the World of <span class="serif grad-text">Creativity, Media &amp; Events.</span>')}
        <div class="bgrid">{''.join(blog_card(p) for p in sorted(POSTS, key=lambda x: x['date'], reverse=True)[:3])}</div>
        <div class="center mt-5 reveal">{btn('Visit Our Blog', 'blog/', 'ghost', 'bi-arrow-right')}</div>
      </div>
    </section>'''

    join = f'''    <section class="join">
      <div class="container-x">
        <div class="join__panel">
          <div class="ribbon ribbon--r" data-ribbon="side-r"></div>
          <div class="join__copy">
            <span class="eyebrow reveal">Careers at Playback</span>
            <h2 class="section-title mt-3 reveal">Your Creativity Could Be Our Next <span class="serif grad-text">Great Collaboration.</span></h2>
            <p class="reveal">We are always interested in connecting with talented individuals passionate about photography, filmmaking, digital marketing, design, technology, and event production. Explore career opportunities and become part of our creative and professional network.</p>
            <div class="hero__actions reveal">{btn('View Careers', 'careers/', 'grad')}{btn('Join Freelancer Network', 'freelancers/', 'ghost', 'bi-person-plus-fill')}</div>
          </div>
        </div>
      </div>
    </section>'''

    contact = cta_band('Have a Project in Mind? <span class="serif grad-text">Let&rsquo;s Make It Happen.</span>',
                       'Whether you need a professional photoshoot, corporate film, digital marketing campaign, medical conference production, or complete event support, we&rsquo;d love to hear about your requirements.',
                       btn('Get a Quote', 'get-a-quote/', 'grad') + btn('Contact Us', 'contact-us/', 'ghost', 'bi-envelope-fill') + btn('WhatsApp', wa_link(), 'ghost', 'bi-whatsapp', ext=True),
                       enquiry_form(), eyebrow="Let's work together", id_='contact')
    contact = contact.replace('<div>Email<a', f'<div>Secondary<a href="tel:{SITE["phone2_tel"]}">{SITE["phone2_disp"]}</a></div><div>Email<a', 1)

    body = '\n'.join([hero, trusted, about, counters, expertise, portfolio, films, digital, events, industries,
                      why_panel('More Than a Service Provider. <span class="serif grad-text">A Creative Partner.</span>'),
                      process, team, voices_section(), insights, join, contact])
    return page('', title='Playback Media & Events Hub | Photography, Video, Digital & Events',
                desc='Delhi NCR company for professional photography, videography and film production, digital marketing and event & conference management. Create, Connect, and Grow.',
                body=body, active='home', home=True, swiper=True, schema=[ORG_SCHEMA,
                {'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE['name'], 'url': SITE['url'] + '/'}])

def mini_team(t):
    return f'''<a class="tmini reveal" href="~/meet-the-team/#{t['slug']}">
            <figure><img src="~/assets/img/team/{t['slug']}.webp" alt="Portrait of {esc(t['name'])}" loading="lazy" decoding="async"></figure>
            <div><h3>{esc(t['name'])}</h3><span>{esc(t['role'])}</span></div>
          </a>'''

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def about():
    journey = [('Early Years', 'Photography, videography, filmmaking, and television production.'),
               ('2016', 'Formal registration under the earlier Playback Entertainment and Media identity.'),
               ('2018', 'Expansion into digital marketing.'),
               ('Recent Years', 'Expansion into event and conference management.'),
               ('Today', 'Playback Media &amp; Events Hub: integrated media, digital, and event services.')]
    values = [('bi-lightbulb-fill', 'Creativity'), ('bi-briefcase-fill', 'Professionalism'), ('bi-gem', 'Quality'), ('bi-people-fill', 'Collaboration'), ('bi-shield-check', 'Accountability')]
    body = '\n'.join([
        phero(eyebrow='About us', title='About Playback Media &amp; <span class="serif grad-text">Events Hub</span>',
              sub='A Creative Journey From Photography and Filmmaking to Digital Marketing and Event Production.',
              actions=btn('Meet Our Team', 'meet-the-team/', 'grad', 'bi-people-fill') + btn('Our Journey', '#our-journey', 'ghost', 'bi-arrow-down'),
              media='assets/img/work/azad-bhawan-seminar/04.webp', crumbs=[('About Us', None)], chip=('bi-award-fill', '15+ years', 'industry experience')),
        f'''    <section class="section intro about-story">
      <div class="container-x">
        <div class="split split--story">
          <div>
            <span class="eyebrow reveal">Our story</span>
            <h2 class="section-title mt-3 reveal" style="font-size:clamp(2rem,4vw,3.4rem)">From the lens to <span class="serif grad-text">the full picture.</span></h2>
            <div class="prose-lead mt-4">
              <p class="reveal">Playback Media &amp; Events Hub is a Delhi NCR-based creative production, digital marketing, and event management company.</p>
              <p class="reveal">Our professional journey began with photography, videography, television production, and visual storytelling.</p>
              <p class="reveal">Through years of practical production experience, we developed our expertise in corporate films, advertising videos, television programs, commercial photography, portfolios, interviews, and professional post-production.</p>
              <p class="reveal">In 2018, we expanded into digital marketing, helping businesses strengthen their presence through websites, search optimization, social media, advertising, and creative communication.</p>
              <p class="reveal">Our experience working at corporate events and medical conferences gave us valuable insight into event production, audiovisual systems, conference arrangements, and technical execution. Building on this foundation, we expanded into event and conference management.</p>
              <p class="reveal">Today, Playback provides coordinated solutions across photography, video production, digital marketing, and event management for businesses, brands, healthcare professionals, institutions, and organizations.</p>
              <p class="tagline reveal"><span class="serif grad-text">{SITE['tagline']}</span></p>
            </div>
          </div>
          <div class="story-media">
            <div class="mosaic mosaic--tall">
              <figure class="mosaic__item reveal"><img src="~/assets/img/greenscreen-sm.webp" alt="Film shoot on green screen" loading="lazy" decoding="async"></figure>
              <figure class="mosaic__item reveal"><img src="~/assets/img/work/apccsm-medical-workshop/03-sm.webp" alt="Medical workshop session" loading="lazy" decoding="async"></figure>
              <figure class="mosaic__item reveal"><img src="~/assets/img/work/product-commercial-photography/02-sm.webp" alt="Product photograph" loading="lazy" decoding="async"></figure>
              <figure class="mosaic__item reveal"><img src="~/assets/img/stage-spiral-sm.webp" alt="Conference stage with LED wall" loading="lazy" decoding="async"></figure>
            </div>
          </div>
        </div>
      </div>
    </section>''',
        f'''    <section class="section vm">
      <div class="container-x">
        <div class="cgrid cgrid--2">
          <article class="ccard ccard--big reveal"><span class="icon-tile violet"><i class="bi bi-eye-fill"></i></span><span class="eyebrow mt-4">Our vision</span><p class="ccard__lead">To become a trusted partner in creative production, digital marketing, and event management by delivering innovative solutions and consistently professional work.</p></article>
          <article class="ccard ccard--big reveal"><span class="icon-tile rose"><i class="bi bi-compass-fill"></i></span><span class="eyebrow mt-4">Our mission</span><p class="ccard__lead">To help businesses and individuals communicate their stories, develop their brands, and create meaningful experiences through integrated creative and technical services.</p></article>
        </div>
        <div class="values reveal"><span class="values__label">Our values</span>{''.join(f'<span class="value"><i class="bi {i}"></i>{v}</span>' for i, v in values)}</div>
      </div>
    </section>''',
        f'''    <section class="section process" id="our-journey">
      <div class="container-x">
        {shead('Our journey', 'Milestones that <span class="serif grad-text">shaped us.</span>', 'How a photography and filmmaking practice grew into an integrated media, digital and events company.')}
        {steps(journey, ['bi-camera', 'bi-patch-check', 'bi-graph-up-arrow', 'bi-stars', 'bi-diagram-3'])}
      </div>
    </section>''',
        f'''    <section class="section stats">
      <div class="container-x">
        {shead('Experience', 'Experience That Speaks <span class="serif grad-text">Through Our Work.</span>')}
        {stats_grid()}
      </div>
    </section>''',
        why_panel('More Than a Service Provider. <span class="serif grad-text">A Creative Partner.</span>', sid='why-choose-us'),
        f'''    <section class="section clients-strip">
      <div class="container-x">{shead('Clients', 'Organisations we have <span class="serif grad-text">worked with.</span>', None)}</div>
      {logos_marquee()}
      <div class="container-x center mt-5 reveal">{btn('Clients &amp; Testimonials', 'clients-testimonials/', 'ghost', 'bi-arrow-right')}</div>
    </section>''',
        f'''    <section class="section team-preview">
      <div class="container-x">
        <div class="shead">
          <div><span class="eyebrow reveal">Our team</span><h2 class="section-title mt-3 reveal">Meet the People <span class="serif grad-text">Behind Playback.</span></h2></div>
          <div><p class="section-lead reveal">Discover the creative and technical professionals who contribute to our projects.</p><div class="reveal mt-4">{btn('Meet Our Team', 'meet-the-team/', 'dark', 'bi-arrow-right')}</div></div>
        </div>
        <div class="tgrid tgrid--4">{''.join(mini_team(t) for t in TEAM[:4])}</div>
      </div>
    </section>''',
        cta_band('Have a Project in Mind? <span class="serif grad-text">Let&rsquo;s Make It Happen.</span>',
                 'Tell us about your photography, video, digital marketing or event requirement and our team will contact you with the next steps.',
                 btn('Get a Quote', 'get-a-quote/', 'grad') + btn('Contact Us', 'contact-us/', 'ghost', 'bi-envelope-fill')),
    ])
    return page('about-us/', title='About Us | Playback Media & Events Hub',
                desc='Playback Media & Events Hub is a Delhi NCR creative production, digital marketing and event management company: our story, vision, mission, values and journey.',
                body=body, active='about', crumbs=[('About Us', None)], og_image='assets/img/work/azad-bhawan-seminar/04.webp')

# ---------------------------------------------------------------------------
# TEAM
# ---------------------------------------------------------------------------
def team_page():
    lead = [t for t in TEAM if t['group'] == 'lead']
    prod = [t for t in TEAM if t['group'] == 'production']
    dig = [t for t in TEAM if t['group'] == 'digital']
    body = '\n'.join([
        phero(eyebrow='The people behind the creative work', title='Meet Our <span class="serif grad-text">Team</span>',
              sub='Creative Minds. Technical Expertise. One Shared Vision.',
              lead='Behind every photograph, film, digital campaign, and professionally executed event is a team of individuals combining creativity, experience, technology, and dedication.',
              actions=btn('Explore Careers', 'careers/', 'grad', 'bi-briefcase-fill') + btn('Join Freelancer Network', 'freelancers/', 'ghost', 'bi-person-plus-fill'),
              crumbs=[('About Us', 'about-us/'), ('Meet Our Team', None)]),
        f'''    <section class="section team-intro">
      <div class="container-x">
        <div class="prose-lead prose-lead--center">
          <p class="reveal">At Playback Media &amp; Events Hub, our strength lies in the people who bring ideas to life.</p>
          <p class="reveal">Our professional network spans photography, cinematography, filmmaking, video editing, digital marketing, design, audiovisual production, and event coordination. Together, we work to develop meaningful content, effective brand communication, and memorable professional experiences.</p>
        </div>
      </div>
    </section>''',
        f'''    <section class="section team-lead">
      <div class="container-x">
        {shead('Leadership', 'Leading the <span class="serif grad-text">vision.</span>')}
        <div class="tgrid tgrid--2">{''.join(team_card(t, True) for t in lead)}</div>
      </div>
    </section>''',
        f'''    <section class="section">
      <div class="container-x">
        {shead('Photography &amp; production', 'Behind the <span class="serif grad-text">lens.</span>')}
        <div class="tgrid tgrid--4">{''.join(team_card(t) for t in prod)}</div>
      </div>
    </section>''',
        f'''    <section class="section">
      <div class="container-x">
        {shead('Digital &amp; creative', 'Building brands <span class="serif grad-text">online.</span>')}
        <div class="tgrid tgrid--2 tgrid--narrow">{''.join(team_card(t) for t in dig)}</div>
      </div>
    </section>''',
        f'''    <section class="why">
      <div class="container-x">
        <div class="why__panel why__panel--center">
          <div class="ribbon ribbon--l" data-ribbon="side-l"></div>
          <div class="ribbon ribbon--r" data-ribbon="side-r"></div>
          <span class="eyebrow eyebrow--center reveal">Our extended creative network</span>
          <h2 class="why__title reveal">Collaboration Makes Great Work <span class="serif grad-text">Possible.</span></h2>
          <div class="prose-lead prose-lead--center">
            <p class="reveal">Beyond our core team, Playback works with additional creative professionals, technical experts, freelancers, and production partners according to the scope of each assignment.</p>
            <p class="reveal">Our extended network includes specialists in photography, cinematography, editing, design, social media, event production, lighting, sound, and audiovisual technology. This collaborative approach helps us organize appropriate resources for projects of different sizes and requirements.</p>
          </div>
          <div class="catwrap reveal">{chips(['Photography', 'Cinematography', 'Editing', 'Design', 'Social media', 'Event production', 'Lighting', 'Sound', 'Audiovisual technology'])}</div>
        </div>
      </div>
    </section>''',
        cta_band('Your Talent Could Be Part of Our <span class="serif grad-text">Next Project.</span>',
                 'We welcome creative, technical, and digital professionals who are passionate about learning, collaboration, and professional production.',
                 btn('Explore Careers', 'careers/', 'grad', 'bi-briefcase-fill') + btn('Join Freelancer Network', 'freelancers/', 'ghost', 'bi-person-plus-fill'), eyebrow='Join our team'),
    ])
    return page('meet-the-team/', title='Meet Our Team | Playback Media & Events Hub',
                desc='Meet the leadership, photographers, cinematographers, and digital professionals behind Playback Media & Events Hub.',
                body=body, active='about', crumbs=[('About Us', 'about-us/'), ('Meet Our Team', None)], og_image='assets/img/team/raushan-s-kumar.webp')

# ---------------------------------------------------------------------------
# SERVICES HUB
# ---------------------------------------------------------------------------
def services_hub():
    blocks = []
    for i, d in enumerate(DIVISIONS):
        subs = ''.join(f'<li><a href="~/{s}/"><i class="bi bi-arrow-right-short"></i>{esc(n)}</a></li>' for s, n in d['subs'])
        blocks.append(f'''<article class="dcard reveal{' dcard--rev' if i % 2 else ''}">
            <figure class="dcard__img"><img src="~/{d['image']}" alt="" loading="lazy" decoding="async"><span class="dcard__no">0{i + 1}</span></figure>
            <div class="dcard__body">
              <span class="icon-tile {d['tile']}"><i class="bi {d['icon']}"></i></span>
              <h2>{esc(d['name'])}</h2>
              <p>{esc(d['blurb'])}</p>
              <ul class="dcard__subs">{subs}</ul>
              {btn(d['all'], d['slug'] + '/', 'dark', 'bi-arrow-right')}
            </div>
          </article>''')
    caps = ''.join(f'<span class="cap {c}"><i class="bi {i}"></i>{esc(t)}</span>' for i, t, c in SUPPORTING)
    body = '\n'.join([
        phero(eyebrow='Our services', title='Four Core Strengths. <span class="serif grad-text">One Creative Partner.</span>',
              sub='Photography | Videography | Digital Marketing | Event Management',
              lead='Playback brings together creative production, digital expertise, and event execution, with supporting services including audiovisual production, LED walls, exhibition stalls, event branding, printing, corporate gifting, live streaming, webinar production, and influencer marketing.',
              actions=btn('Get a Quote', 'get-a-quote/', 'grad') + btn('View Our Work', 'portfolio/', 'ghost', 'bi-grid-1x2-fill'),
              crumbs=[('Services', None)]),
        f'''    <section class="section">
      <div class="container-x"><div class="dstack">{''.join(blocks)}</div></div>
    </section>''',
        f'''    <section class="caps" aria-label="Supporting services">
      <div class="container-x caps__head">
        <span class="eyebrow reveal">Supporting services</span>
        <h2 class="section-title mt-3 reveal" style="font-size:clamp(1.8rem,3.6vw,3rem)">Everything your project <span class="serif grad-text">needs to shine.</span></h2>
      </div>
      <div class="marquee" style="--dur:70s"><div class="marquee__track">{caps}</div></div>
    </section>''',
        f'''    <section class="section process">
      <div class="container-x">
        {shead('Our process', 'From Your Idea to the <span class="serif grad-text">Final Outcome.</span>')}
        {steps(HOME_PROCESS)}
      </div>
    </section>''',
        cta_band('Not sure which service you need? <span class="serif grad-text">Let&rsquo;s talk.</span>',
                 'Tell us what you want to achieve and we will recommend the right combination of services, with a clear proposal.',
                 btn('Discuss Your Project', 'get-a-quote/', 'grad') + btn('WhatsApp', wa_link(), 'ghost', 'bi-whatsapp', ext=True), enquiry_form()),
    ])
    return page('services/', title='Services | Photography, Video, Digital & Events | Playback',
                desc='Photography, videography and film production, digital marketing and websites, and event & conference management in Delhi NCR.',
                body=body, active='services', crumbs=[('Services', None)])

# ---------------------------------------------------------------------------
# PORTFOLIO + PROJECT PAGES
# ---------------------------------------------------------------------------
def portfolio():
    feat = [PROJECT_BY_SLUG['iasrm-world-congress-2026'], PROJECT_BY_SLUG['pelvic-floor-summit-2026']]
    fcards = ''.join(f'''<a class="fproj reveal" href="~/portfolio/{p['slug']}/">
            <span class="fproj__icon"><i class="bi {p['type_icon']}"></i></span>
            <div><small>{esc(p['category_label'])} · {esc(p['location'])}</small><h3>{esc(p['title'])}</h3><p>{esc(p['excerpt'])}</p></div>
            <span class="go"><i class="bi bi-arrow-up-right"></i></span>
          </a>''' for p in feat)
    body = '\n'.join([
        phero(eyebrow='Our work', title='Our Work – Creative Projects &amp; <span class="serif grad-text">Professional Productions</span>',
              sub='Every project reflects a unique creative challenge, audience, and purpose.',
              lead='Explore selected photography, filmmaking, digital marketing, event management, audiovisual production, and exhibition projects by Playback Media &amp; Events Hub.',
              actions=btn('Watch Our Showreel', 'showreel/', 'grad', 'bi-play-fill') + btn('Get a Quote', 'get-a-quote/', 'ghost'),
              crumbs=[('Our Work', None)]),
        f'''    <section class="section fprojects">
      <div class="container-x">
        {shead('Featured projects', 'Recent <span class="serif grad-text">conference productions.</span>')}
        <div class="fgrid">{fcards}</div>
      </div>
    </section>''',
        f'''    <section class="section portfolio-all" id="projects">
      <div class="container-x">
        {shead('All projects', 'Browse by <span class="serif grad-text">category.</span>', 'Filter the portfolio. The address bar updates, so you can share any filtered view.')}
        {filters(PORTFOLIO_CATS, '#project-grid')}
        <p class="filter-count" aria-live="polite" data-filter-count></p>
        <div class="pgrid" id="project-grid">{''.join(project_card(p) for p in PROJECTS)}</div>
        <p class="empty-state" hidden>No projects in this category yet. <a href="~/portfolio/">View all projects</a>.</p>
      </div>
    </section>''',
        cta_band('Like what you see? <span class="serif grad-text">Let&rsquo;s create yours.</span>',
                 'Tell us about your project and we will share relevant examples and a clear proposal.',
                 btn('Get a Quote', 'get-a-quote/', 'grad') + btn('Contact Us', 'contact-us/', 'ghost', 'bi-envelope-fill')),
    ])
    return page('portfolio/', title='Our Work | Portfolio | Playback Media & Events Hub',
                desc='Photography, corporate films, advertising and TV, digital marketing, medical conference, corporate event, AV and exhibition projects by Playback.',
                body=body, active='work', crumbs=[('Our Work', None)])

def project_page(p, idx):
    imgs = project_images(p)
    cover_big = project_cover(p, sm=False)
    labels = cat_labels(p, 3)
    meta = [('Client', p.get('client')), ('Category', p.get('category_label') or labels), ('Location', p.get('location')), ('Year', p.get('year'))]
    meta_html = ''.join(f'<div><dt>{k}</dt><dd>{esc(v)}</dd></div>' for k, v in meta if v)
    from services import NAME
    svc = ''.join(f'<li><a href="~/{s}/"><i class="bi bi-arrow-right-short"></i>{esc(NAME.get(s, s))}</a></li>' for s in p['services'])
    gal = ''
    if imgs:
        gal = f'''    <section class="section">
      <div class="container-x">
        {shead('Photographs', 'Project <span class="serif grad-text">gallery.</span>', 'Tap any photograph to view it larger.')}
        {gallery(imgs, p['title'] + ' photograph')}
      </div>
    </section>'''
    vids = ''
    if p['videos']:
        vids = f'''    <section class="section">
      <div class="container-x">
        {shead('Video', 'Watch the <span class="serif grad-text">work.</span>')}
        {vgrid(p['videos'], 3 if len(p['videos']) > 2 else 2)}
      </div>
    </section>'''
    note = f'<p class="proj-note reveal"><i class="bi bi-info-circle"></i> {esc(p["note"])}</p>' if p.get('note') else ''
    nxt = PROJECTS[(idx + 1) % len(PROJECTS)]
    media = None
    if cover_big and not cover_big.startswith('http'):
        media = cover_big
    hero = phero(eyebrow=esc(labels), title=esc(p['title']), sub=esc(p['excerpt']),
                 actions=btn('Discuss a Similar Project', 'get-a-quote/', 'grad') + btn('All Projects', 'portfolio/', 'ghost', 'bi-grid-1x2-fill'),
                 media=media, crumbs=[('Our Work', 'portfolio/'), (p['title'], None)],
                 media_html=vcard(p['videos'][0], big=True) if (not media and p['videos']) else None)
    body = '\n'.join([
        hero,
        f'''    <section class="section proj-overview">
      <div class="container-x">
        <div class="split split--proj">
          <div class="prose-lead">
            <span class="eyebrow reveal">Client requirement</span>
            <p class="reveal">{esc(p['requirement'])}</p>
            <span class="eyebrow reveal mt-4">Project description</span>
            <p class="reveal">{esc(p['description'])}</p>
            {note}
          </div>
          <aside class="glass glance reveal">
            <dl class="proj-meta">{meta_html}</dl>
            <h2 class="glance__h mt-4">Playback&rsquo;s scope</h2>
            {checklist([esc(x) for x in p['scope']])}
            <h2 class="glance__h mt-4">Related services</h2>
            <ul class="svc-links">{svc}</ul>
          </aside>
        </div>
      </div>
    </section>''',
        gal, vids,
        f'''    <section class="section next-proj">
      <div class="container-x">
        <a class="next-link reveal" href="~/portfolio/{nxt['slug']}/"><small>Next project</small><span>{esc(nxt['title'])}</span><i class="bi bi-arrow-right"></i></a>
      </div>
    </section>''',
        cta_band('Planning something <span class="serif grad-text">similar?</span>',
                 'Share your requirement and our team will contact you to discuss the right approach for your project.',
                 btn('Get a Quote', 'get-a-quote/', 'grad') + btn('WhatsApp', wa_link(f'Hi Playback, I saw your project "{p["title"]}" and would like to discuss something similar.'), 'ghost', 'bi-whatsapp', ext=True)),
    ])
    og = cover_big if cover_big else 'assets/img/hero-dance.webp'
    return page(f"portfolio/{p['slug']}/", title=f"{p['title']} | Our Work | Playback Media & Events Hub",
                desc=(p['excerpt'] if len(p['excerpt']) >= 70 else p['excerpt'] + ' A Playback Media & Events Hub production.'), body=body, active='work', crumbs=[('Our Work', 'portfolio/'), (p['title'], None)], og_image=og,
                schema=[{'@context': 'https://schema.org', '@type': 'CreativeWork', 'name': p['title'], 'description': p['description'],
                         'creator': {'@type': 'Organization', 'name': SITE['name']}, **({'dateCreated': p['year']} if p.get('year') else {})}])

# ---------------------------------------------------------------------------
# SHOWREEL
# ---------------------------------------------------------------------------
def showreel():
    cards = ''.join(vcard(v, t, cats, sub=VIDEO_CATS_LABEL(cats[0])) for v, t, cats in VIDEOS)
    body = '\n'.join([
        phero(eyebrow='Video showreel', title='Bringing Stories to Life, <span class="serif grad-text">Frame by Frame.</span>',
              sub='Corporate films, advertising, television, documentaries, events, healthcare content and more.',
              actions=btn('Start Your Video Project', 'get-a-quote/?service=video', 'grad') + btn('Video Production', 'video-production/', 'ghost', 'bi-camera-reels-fill'),
              crumbs=[('Our Work', 'portfolio/'), ('Video Showreel', None)]),
        f'''    <section class="section reel-feature">
      <div class="container-x">
        <div class="reel-player reveal">{vcard(SHOWREEL_ID, 'Playback Showreel', big=True, sub='Click to play')}</div>
      </div>
    </section>''',
        f'''    <section class="section" id="videos">
      <div class="container-x">
        {shead('Video library', 'Explore by <span class="serif grad-text">category.</span>', f'{len(VIDEOS)} productions from our YouTube library. Filter by category; the address bar updates so you can share any view.')}
        {filters([('all', 'All Videos')] + VIDEO_CATS, '#video-grid')}
        <p class="filter-count" aria-live="polite" data-filter-count></p>
        <div class="vgrid" id="video-grid" style="--cols:3">{cards}</div>
      </div>
    </section>''',
        cta_band('Have a story to <span class="serif grad-text">tell?</span>',
                 'From a corporate film to a full television series, we would love to hear about your video project.',
                 btn('Start Your Video Project', 'get-a-quote/?service=video', 'grad') + btn('WhatsApp', wa_link('Hi Playback, I would like to discuss a video project.'), 'ghost', 'bi-whatsapp', ext=True)),
    ])
    return page('showreel/', title='Video Showreel | Films, TV, Corporate & Event Videos | Playback',
                desc='Watch the Playback Media & Events Hub showreel: corporate films, advertising, TV production, documentaries, event highlights, healthcare and training videos.',
                body=body, active='work', crumbs=[('Our Work', 'portfolio/'), ('Video Showreel', None)])

_VC = dict(VIDEO_CATS)
def VIDEO_CATS_LABEL(k):
    return _VC.get(k, '')

# ---------------------------------------------------------------------------
# CLIENTS & TESTIMONIALS
# ---------------------------------------------------------------------------
def clients_page():
    tcards = ''.join(f'''<figure class="qcard reveal">
            <blockquote>{esc(t['text'])}</blockquote>
            <figcaption class="person">{person_av(t)}<div><b>{esc(t['name'])}</b><small>{esc(t['role'])} · {esc(t['org'])}</small></div></figcaption>
          </figure>''' for t in TESTIMONIALS)
    body = '\n'.join([
        phero(eyebrow='Clients &amp; testimonials', title='Clients, Collaborations &amp; <span class="serif grad-text">Testimonials</span>',
              sub='Our strength lies in the relationships we develop through creative work, communication, coordination, and professional execution.',
              lead='Playback Media &amp; Events Hub values the opportunity to support businesses, brands, institutions, healthcare organizations, and professional clients across different service requirements.',
              crumbs=[('About Us', 'about-us/'), ('Clients & Testimonials', None)]),
        f'''    <section class="section">
      <div class="container-x">
        {shead('Our clients', 'Organisations that <span class="serif grad-text">trust us.</span>')}
        {logos_grid()}
      </div>
    </section>''',
        f'''    <section class="section qsec">
      <div class="container-x">
        {shead('Testimonials', 'In our clients&rsquo; <span class="serif grad-text">words.</span>')}
        <div class="qgrid">{tcards}</div>
      </div>
    </section>''',
        f'''    <section class="section">
      <div class="container-x">
        {shead('Video testimonials', 'Hear it from <span class="serif grad-text">them.</span>')}
        <div class="vgrid" style="--cols:3">{''.join(vcard(v, n, sub=o) for v, n, o in VIDEO_TESTIMONIALS)}</div>
      </div>
    </section>''',
        cta_band('Become our next <span class="serif grad-text">success story.</span>', 'Tell us about your project and let&rsquo;s build a lasting working relationship.',
                 btn('Get a Quote', 'get-a-quote/', 'grad') + btn('Contact Us', 'contact-us/', 'ghost', 'bi-envelope-fill')),
    ])
    return page('clients-testimonials/', title='Clients & Testimonials | Playback Media & Events Hub',
                desc='Clients, collaborations and verified testimonials from businesses, hospitals, institutions and brands who have worked with Playback Media & Events Hub.',
                body=body, active='about', crumbs=[('About Us', 'about-us/'), ('Clients & Testimonials', None)])

# ---------------------------------------------------------------------------
# BLOG
# ---------------------------------------------------------------------------
def blog_index():
    posts = sorted(POSTS, key=lambda x: x['date'], reverse=True)
    body = '\n'.join([
        phero(eyebrow='Blog', title='Ideas, Insights &amp; Stories <span class="serif grad-text">From Playback</span>',
              sub='Explore creative inspiration, professional insights, production ideas, digital marketing strategies, event planning considerations, and company updates.',
              crumbs=[('Blog', None)], compact=True),
        f'''    <section class="section blog-list" id="posts">
      <div class="container-x">
        {filters(BLOG_CATS, '#post-grid')}
        <p class="filter-count" aria-live="polite" data-filter-count></p>
        <h2 class="sr-only">Articles</h2>
        <div class="bgrid" id="post-grid">{''.join(blog_card(p) for p in posts)}</div>
        <p class="empty-state" hidden>No articles in this category yet. <a href="~/blog/">View all articles</a>.</p>
      </div>
    </section>''',
        cta_band('Have a question for our <span class="serif grad-text">team?</span>', 'We are happy to advise on photography, video, digital marketing and event production.',
                 btn('Contact Us', 'contact-us/', 'grad', 'bi-envelope-fill') + btn('WhatsApp', wa_link(), 'ghost', 'bi-whatsapp', ext=True)),
    ])
    return page('blog/', title='Blog | Ideas, Insights & Stories From Playback',
                desc='Articles on photography, video production, digital marketing, websites, corporate events, medical conferences and AV technology from Playback Media & Events Hub.',
                body=body, active='blog', crumbs=[('Blog', None)])

def post_page(p):
    posts = sorted(POSTS, key=lambda x: x['date'], reverse=True)
    related = [x for x in posts if x['cat'] == p['cat'] and x['slug'] != p['slug']][:3]
    related += [x for x in posts if x not in related and x['slug'] != p['slug']][:3 - len(related)]
    rs, rl = p['related_service']
    from urllib.parse import quote
    url = SITE['url'] + '/blog/' + p['slug'] + '/'
    share = (f'<a href="https://www.linkedin.com/sharing/share-offsite/?url={quote(url)}" target="_blank" rel="noopener" aria-label="Share on LinkedIn"><i class="bi bi-linkedin"></i></a>'
             f'<a href="https://api.whatsapp.com/send?text={quote(p["title"] + " " + url)}" target="_blank" rel="noopener" aria-label="Share on WhatsApp"><i class="bi bi-whatsapp"></i></a>'
             f'<a href="https://www.facebook.com/sharer/sharer.php?u={quote(url)}" target="_blank" rel="noopener" aria-label="Share on Facebook"><i class="bi bi-facebook"></i></a>')
    body = '\n'.join([
        f'''    <article class="post">
      <header class="post__hero">
        <div class="hero__grain"></div>
        <div class="container-x">
          <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="~/">Home</a></li><li><a href="~/blog/">Blog</a></li><li aria-current="page">{esc(p['title'])}</li></ol></nav>
          <div class="post__head">
            <a class="post__cat" href="~/blog/?category={p['cat']}" data-hero-fade>{esc(BLOG_CAT_LABEL[p['cat']])}</a>
            <h1 class="phero__title" data-hero-title>{esc(p['title'])}</h1>
            <p class="post__meta" data-hero-fade>By Playback Media &amp; Events Hub · <time datetime="{p['date']}">{fmt_date(p['date'])}</time> · {read_time(p['body'])} min read</p>
          </div>
          <figure class="post__cover" data-hero-fade><img src="~/{p['image']}" alt="" decoding="async" fetchpriority="high"></figure>
        </div>
      </header>
      <div class="container-x">
        <div class="post__layout">
          <div class="prose">{p['body']}</div>
          <aside class="post__aside">
            <div class="glass glance">
              <h3>Need help with this?</h3>
              <p>Our team provides <a href="~/{rs}/">{esc(rl)}</a> across Delhi NCR.</p>
              {btn('Get a Quote', 'get-a-quote/', 'grad')}
              <div class="share"><span>Share</span>{share}</div>
            </div>
          </aside>
        </div>
      </div>
    </article>''',
        f'''    <section class="section">
      <div class="container-x">
        {shead('Keep reading', 'Related <span class="serif grad-text">articles.</span>')}
        <div class="bgrid">{''.join(blog_card(x) for x in related)}</div>
      </div>
    </section>''',
        cta_band('Have a project in mind? <span class="serif grad-text">Let&rsquo;s talk.</span>', 'Share your requirement and our team will contact you with the next steps.',
                 btn('Get a Quote', 'get-a-quote/', 'grad') + btn('Contact Us', 'contact-us/', 'ghost', 'bi-envelope-fill')),
    ])
    schema = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'datePublished': p['date'], 'dateModified': p['date'],
              'image': SITE['url'] + '/' + p['image'], 'description': p['excerpt'], 'mainEntityOfPage': url,
              'author': {'@type': 'Organization', 'name': SITE['name']}, 'publisher': {'@type': 'Organization', 'name': SITE['name'], 'logo': {'@type': 'ImageObject', 'url': SITE['url'] + '/assets/img/logo.png'}}}
    return page(f"blog/{p['slug']}/", title=f"{p['title']} | Playback Blog", desc=p['excerpt'], body=body, active='blog',
                crumbs=[('Blog', 'blog/'), (p['title'], None)], og_image=p['image'], schema=[schema])

# ---------------------------------------------------------------------------
# CAREERS & FREELANCERS
# ---------------------------------------------------------------------------
def careers():
    why = [('bi-palette-fill', 'Creative Opportunities', 'Work across diverse production and digital projects involving brands, businesses, healthcare professionals, institutions, and events.'),
           ('bi-tools', 'Practical Experience', 'Develop your understanding of professional production processes, project coordination, and client requirements.'),
           ('bi-people-fill', 'Collaborative Environment', 'Work alongside creative professionals, digital specialists, production teams, and technical collaborators.'),
           ('bi-graph-up-arrow', 'Professional Development', 'Build practical experience through assignments that require creativity, planning, communication, and problem-solving.'),
           ('bi-collection-fill', 'Diverse Projects', 'Explore opportunities across photography, video production, digital marketing, and event services.')]
    cats = ''.join(icon_card(i, t, d, None, ['', 'violet', 'rose'][n % 3]) for n, (i, t, d) in enumerate(CAREER_CATEGORIES))
    if JOBS:
        jobs = '<div class="jobs">' + ''.join(f'''<article class="job reveal">
            <div class="job__head"><h3>{esc(j['title'])}</h3><div class="job__tags"><span>{esc(j['department'])}</span><span><i class="bi bi-geo-alt"></i> {esc(j['location'])}</span><span>{esc(j['type'])}</span><span>{esc(j['experience'])}</span></div></div>
            <p>{esc(j['summary'])}</p>
            <details class="job__details"><summary>View Details</summary>{checklist([esc(x) for x in j.get('details', [])])}</details>
            <a href="#apply" class="btn-x btn-grad" data-apply="{esc(j['title'])}">Apply Now <span class="ico"><i class="bi bi-arrow-down-right"></i></span></a>
          </article>''' for j in JOBS) + '</div>'
    else:
        jobs = f'''<div class="no-openings reveal">
            <span class="icon-tile violet"><i class="bi bi-search-heart"></i></span>
            <div><h3>Don&rsquo;t See a Suitable Opening?</h3><p>We&rsquo;re always interested in connecting with talented professionals. Submit your profile for future consideration.</p></div>
            <a href="#apply" class="btn-x btn-grad">Submit Your Profile <span class="ico"><i class="bi bi-arrow-down-right"></i></span></a>
          </div>'''
    positions = ['Photographer', 'Cinematographer / Camera Operator', 'Video Editor', 'Motion Graphics Artist', 'Social Media Executive', 'SEO / Digital Marketing Executive',
                 'Graphic Designer', 'Website Developer', 'Event Coordinator', 'AV / LED Technician', 'Business Development', 'Other / General Application']
    exp = ['Fresher', 'Less than 1 year', '1–3 years', '3–5 years', '5–10 years', '10+ years']
    f = (field('full_name', 'Full Name', required=True) + field('email', 'Email', 'email', required=True) + field('mobile', 'Mobile Number', 'tel', required=True)
         + field('city', 'Current City', required=True) + field('position', 'Position Applied For', 'select', required=True, options=positions)
         + field('experience', 'Experience', 'select', required=True, options=exp) + field('skills', 'Skills', full=True, placeholder='e.g. Premiere Pro, lighting, SEO')
         + field('portfolio', 'Portfolio / Work Sample Link', 'url', full=True, placeholder='https://')
         + field('resume', 'Resume Upload', 'file', required=True, full=True, help_='PDF, DOC or DOCX, up to 5 MB.')
         + field('introduction', 'Short Introduction', 'textarea', full=True))
    application = form('job-application', f, 'Submit Application', files=True,
                       consent='I consent to Playback Media &amp; Events Hub processing my application details and resume for recruitment purposes, as described in the <a href="~/privacy-policy/">Privacy Policy</a>.',
                       success=('Thank You for Applying!', 'Your application has been received successfully. Our team will review your information and contact you if your profile matches a suitable opportunity.'),
                       error=("We Couldn't Submit Your Application.", f"Please check your information and try again, or email your resume to {SITE['email']}."))
    body = '\n'.join([
        phero(eyebrow='Careers at Playback', title='Join Our <span class="serif grad-text">Team</span>', sub='Create. Collaborate. Learn. Grow.',
              lead='At Playback Media &amp; Events Hub, we believe exceptional work begins with talented, curious, and dedicated people.',
              actions=btn('View Openings', '#openings', 'grad', 'bi-arrow-down') + btn('Join Freelancer Network', 'freelancers/', 'ghost', 'bi-person-plus-fill'),
              media='assets/img/work/tata-milestones-2023/01.webp', crumbs=[('Join Our Team', None)]),
        f'''    <section class="section">
      <div class="container-x">
        <div class="prose-lead prose-lead--center">
          <p class="reveal">Our creative environment brings together professionals working across photography, filmmaking, editing, digital marketing, graphic design, websites, audiovisual technology, and event management.</p>
          <p class="reveal">If you are passionate about creativity, professional growth, technical innovation, and teamwork, explore opportunities to collaborate with us.</p>
        </div>
      </div>
    </section>''',
        f'''    <section class="why">
      <div class="container-x">
        <div class="why__panel">
          <div class="ribbon ribbon--l" data-ribbon="side-l"></div>
          <div class="ribbon ribbon--r" data-ribbon="side-r"></div>
          <h2 class="why__title reveal">Why Work With <span class="serif grad-text">Playback?</span></h2>
          <div class="why6 why6--5">{''.join(f'<div class="glass why-item reveal"><span class="icon-tile {["", "violet", "rose"][n % 3]}"><i class="bi {i}"></i></span><div><h3>{t}</h3><p>{d}</p></div></div>' for n, (i, t, d) in enumerate(why))}</div>
        </div>
      </div>
    </section>''',
        f'''    <section class="section">
      <div class="container-x">
        {shead('Career categories', 'Where you could <span class="serif grad-text">fit in.</span>')}
        <div class="cgrid cgrid--3">{cats}</div>
      </div>
    </section>''',
        f'''    <section class="section openings" id="openings">
      <div class="container-x">
        {shead('Current openings', 'Explore Available <span class="serif grad-text">Opportunities.</span>')}
        {jobs}
      </div>
    </section>''',
        f'''    <section class="section apply" id="apply">
      <div class="container-x">
        <div class="split split--form">
          <div>
            {shead('Apply for a job', 'Take the Next Step in Your <span class="serif grad-text">Career.</span>', 'Interested in working with Playback Media &amp; Events Hub? Submit your professional details, experience, and portfolio. Our team will review your application for suitable opportunities.')}
            <div class="glass glance reveal mt-4"><h2 class="glance__h">Prefer to freelance?</h2><p>Register with our freelancer network to be considered for project-based assignments.</p>{btn('Join Freelancer Network', 'freelancers/', 'dark', 'bi-arrow-right')}</div>
          </div>
          <div class="form-card reveal">{application}</div>
        </div>
      </div>
    </section>''',
    ])
    return page('careers/', title='Careers at Playback Media & Events Hub',
                desc='Explore photography, videography, editing, digital marketing, design, and event production opportunities at Playback Media & Events Hub.',
                body=body, active='careers', crumbs=[('Join Our Team', None)])

def freelancers():
    skills = ['Photography', 'Cinematography / Videography', 'Video Editing', 'Motion Graphics', 'Graphic Design', 'Social Media / Content Creation', 'Website Development',
              'Event Coordination', 'AV / LED Operation', 'Sound Engineering', 'Lighting', 'Makeup &amp; Styling', 'Anchoring / Hosting', 'Other']
    skills = [s.replace('&amp;', '&') for s in skills]
    f = (field('full_name', 'Full Name', required=True) + field('mobile', 'Mobile Number', 'tel', required=True) + field('email', 'Email Address', 'email', required=True)
         + field('city', 'City', required=True) + field('primary_skill', 'Primary Skill', 'select', required=True, options=skills)
         + field('secondary_skills', 'Secondary Skills', placeholder='e.g. drone, colour grading')
         + field('experience', 'Years of Experience', 'select', required=True, options=['Less than 1 year', '1–3 years', '3–5 years', '5–10 years', '10+ years'])
         + field('equipment', 'Equipment Owned, if relevant', placeholder='Cameras, lenses, lights, laptop…')
         + field('portfolio', 'Portfolio Link', 'url', required=True, full=True, placeholder='https://')
         + field('resume', 'Resume / Profile Upload', 'file', full=True, help_='PDF, DOC or DOCX, up to 5 MB.')
         + field('availability', 'Availability', 'select', required=True, options=['Weekdays', 'Weekends', 'Full-time on projects', 'Flexible'])
         + field('locations', 'Preferred Work Locations', placeholder='e.g. Delhi, Noida, Gurugram')
         + field('additional', 'Additional Information', 'textarea', full=True))
    reg = form('freelancer', f, 'Register as a Freelancer', files=True,
               consent='I consent to Playback Media &amp; Events Hub storing and reviewing my profile for suitable future projects, as described in the <a href="~/privacy-policy/">Privacy Policy</a>.',
               success=('Thank You for Registering!', 'Your freelancer profile has been received. Our team will review it and contact you when a suitable project arises.'),
               error=("We Couldn't Submit Your Registration.", f"Please check your information and try again, or email your profile to {SITE['email']}."))
    body = '\n'.join([
        phero(eyebrow='Freelancer network', title='Join Our Freelancer <span class="serif grad-text">Network</span>', sub='Collaborate. Create. Deliver.',
              crumbs=[('Join Our Team', 'careers/'), ('Freelancer Registration', None)], compact=True),
        f'''    <section class="section">
      <div class="container-x">
        <div class="split split--form">
          <div>
            <div class="prose-lead">
              <p class="reveal">Playback Media &amp; Events Hub works with creative professionals, production specialists, and technical collaborators according to project requirements.</p>
              <p class="reveal">We welcome freelance professionals interested in working on suitable assignments involving photography, cinematography, video editing, digital content, design, event production, AV systems, and related services.</p>
              <p class="reveal">Register your professional profile so that our team can consider you for relevant future projects.</p>
            </div>
            <div class="catwrap reveal mt-4">{chips(['Photography', 'Cinematography', 'Video editing', 'Digital content', 'Design', 'Event production', 'AV systems'])}</div>
            <p class="proj-note reveal mt-4"><i class="bi bi-info-circle"></i> Registration does not guarantee work or employment.</p>
          </div>
          <div class="form-card reveal">{reg}</div>
        </div>
      </div>
    </section>''',
    ])
    return page('freelancers/', title='Join Our Freelancer Network | Playback Media & Events Hub',
                desc='Photographers, cinematographers, editors, designers and event and AV professionals: register with the Playback Media & Events Hub freelancer network.',
                body=body, active='careers', crumbs=[('Join Our Team', 'careers/'), ('Freelancer Registration', None)])

# ---------------------------------------------------------------------------
# CONTACT & QUOTE
# ---------------------------------------------------------------------------
def contact_page():
    cards = [
        ('bi-telephone-fill', 'Call Us', f'<a href="tel:{SITE["phone1_tel"]}">Primary: {SITE["phone1_disp"]}</a><a href="tel:{SITE["phone2_tel"]}">Secondary: {SITE["phone2_disp"]}</a>', btn('Call Now', 'tel:' + SITE['phone1_tel'], 'dark', 'bi-telephone-fill'), ''),
        ('bi-envelope-fill', 'Email Us', f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>', btn('Send an Email', 'mailto:' + SITE['email'], 'dark', 'bi-envelope-fill'), 'violet'),
        ('bi-whatsapp', 'WhatsApp Us', f'<a href="{wa_link()}" target="_blank" rel="noopener">{SITE["phone1_disp"]}</a>', btn('Chat on WhatsApp', wa_link(), 'dark', 'bi-whatsapp', ext=True), 'rose'),
        ('bi-geo-alt-fill', 'Business Location', f'<span>{SITE["location"]}</span><span>Primary service region: {SITE["region"]}</span>', '', ''),
    ]
    chtml = ''.join(f'''<article class="ccard contact-card reveal"><span class="icon-tile sm {t}"><i class="bi {i}"></i></span><h3>{h}</h3><div class="contact-card__lines">{lines}</div>{b}</article>''' for i, h, lines, b, t in cards)
    opts = list(SERVICE_OPTIONS)
    f = (field('name', 'Full Name', required=True) + field('email', 'Email Address', 'email', required=True) + field('mobile', 'Mobile Number', 'tel', required=True)
         + field('company', 'Company / Organization') + field('service', 'Service Interested In', 'select', required=True, options=opts)
         + field('location', 'Project Location') + field('message', 'Message / Requirement', 'textarea', required=True, full=True))
    body = '\n'.join([
        phero(eyebrow='Get in touch', title='Let&rsquo;s Start a <span class="serif grad-text">Conversation.</span>', sub='Have an Idea? Let&rsquo;s Bring It to Life.',
              lead='Whether you&rsquo;re planning a photoshoot, producing a corporate film, developing your brand online, or organizing a professional event, we&rsquo;re here to discuss your requirements. Share your project details with Playback Media &amp; Events Hub, and our team will review your enquiry and contact you regarding the next steps.',
              crumbs=[('Contact Us', None)], compact=True),
        f'''    <section class="section contact-cards">
      <div class="container-x"><h2 class="sr-only">Ways to reach us</h2><div class="cgrid cgrid--4">{chtml}</div></div>
    </section>''',
        f'''    <section class="section" id="enquiry">
      <div class="container-x">
        <div class="split split--form">
          <div>
            {shead('Enquiry form', 'Tell Us How We Can <span class="serif grad-text">Help.</span>', 'Complete the form below and share your requirements. Our team will review your enquiry and respond using the contact details provided.')}
            <div class="glass glance reveal mt-4">
              <h3>Looking for a Detailed Project Proposal?</h3>
              <p>If you already know your requirements, submit a more detailed project brief so our team can better understand the work involved.</p>
              {btn('Request a Custom Quote', 'get-a-quote/', 'grad')}
            </div>
          </div>
          <div class="form-card reveal">{form('contact', f, 'Send Your Enquiry')}</div>
        </div>
      </div>
    </section>''',
    ])
    return page('contact-us/', title='Contact Playback Media & Events Hub | Delhi NCR',
                desc='Contact Playback Media & Events Hub for photography, videography, digital marketing, corporate events, AV production and conference services.',
                body=body, active='contact', crumbs=[('Contact Us', None)],
                schema=[{'@context': 'https://schema.org', '@type': 'ContactPage', 'name': 'Contact Playback Media & Events Hub', 'url': SITE['url'] + '/contact-us/'}, ORG_SCHEMA])

def quote_page():
    primary = ['Photography', 'Video Production', 'Digital Marketing', 'Event Management']
    general = (field('name', 'Name', required=True) + field('company', 'Company / Organization') + field('email', 'Email', 'email', required=True)
               + field('mobile', 'Mobile', 'tel', required=True)
               + field('primary_service', 'Primary Service', 'select', required=True, options=primary, attrs=' data-quote-switch')
               + field('location', 'Location', required=True) + field('start_date', 'Preferred Start Date', 'date')
               + field('budget', 'Approximate Budget', 'select', options=['Under ₹50,000', '₹50,000 – ₹1,00,000', '₹1,00,000 – ₹5,00,000', '₹5,00,000 – ₹10,00,000', 'Above ₹10,00,000', 'Not sure yet']))
    dyn = {
        'Photography': (field('shoot_type', 'Shoot Type', 'select', options=['Corporate', 'Product & Commercial', 'Portfolio & Headshots', 'Event & Conference', 'Healthcare', 'Other'])
                        + field('shoot_date', 'Shoot Date', 'date') + field('shoot_location', 'Shoot Location') + field('duration', 'Duration', placeholder='e.g. half day, 4 hours')
                        + field('days', 'Number of Days', 'number', attrs=' min="1"') + field('deliverables', 'Photography Deliverables', placeholder='e.g. 50 edited images, same-day selects')),
        'Video Production': (field('video_category', 'Video Category', 'select', options=['Corporate Film', 'Advertising Film', 'TV / Documentary', 'Event Coverage / Highlights', 'Interview / Testimonial', 'Training / Educational', 'Reels / Short-Form', 'Video Editing Only', 'Other'])
                             + field('video_duration', 'Approximate Duration', placeholder='e.g. 2–3 minutes') + field('filming_dates', 'Filming Dates')
                             + field('script', 'Script Requirements', 'select', options=['We have a script', 'We need a script', 'Interview-based / unscripted', 'Not sure'])
                             + field('filming_locations', 'Locations') + field('editing', 'Editing Requirements', placeholder='Graphics, subtitles, versions…')
                             + field('platform', 'Intended Platform', placeholder='YouTube, Instagram, website, events…')),
        'Digital Marketing': (field('business_name', 'Business Name') + field('website', 'Website', 'url', placeholder='https://')
                              + field('social_links', 'Social Links', placeholder='Instagram, LinkedIn…', full=True)
                              + field('dm_services', 'Services Needed', placeholder='Social media, SEO, ads, website…', full=True)
                              + field('objectives', 'Marketing Objectives', 'textarea', full=True)
                              + field('dm_budget', 'Approximate Monthly Budget') + field('dm_start', 'Proposed Start Date', 'date')),
        'Event Management': (field('event_name', 'Event Name') + field('event_category', 'Category', 'select', options=['Corporate Conference / Summit', 'Medical Conference / CME', 'Product Launch', 'Awards / Celebration', 'Exhibition / Trade Event', 'Workshop / Seminar', 'Other'])
                             + field('event_date', 'Event Date', 'date') + field('venue', 'Venue') + field('delegates', 'Number of Delegates', 'number', attrs=' min="1"')
                             + field('halls', 'Number of Halls', 'number', attrs=' min="1"')
                             + '<fieldset class="field field--full checkset"><legend>Requirements</legend>' + ''.join(
                                 f'<label class="check check--sm"><input type="checkbox" name="event_requirements" value="{r}"><span>{r}</span></label>'
                                 for r in ['Required AV', 'Stage Production', 'Photography', 'Videography', 'Booths', 'Branding', 'Live Streaming', 'Printing & Delegate Kits']) + '</fieldset>'
                             + field('additional', 'Additional Requirements', 'textarea', full=True)),
    }
    dyn_html = ''.join(f'<fieldset class="dyn" data-when="{k}" hidden><legend>{k} details</legend><div class="pb-form__grid">{v}</div></fieldset>' for k, v in dyn.items())
    tail = field('description', 'Project Description', 'textarea', required=True, full=True) + field('reference', 'Reference Link', 'url', full=True, placeholder='https://')
    qform = form('quote', general, 'Request a Custom Proposal', extra=dyn_html + f'<div class="pb-form__grid">{tail}</div>',
                 success=('Thank You! Your Project Brief Has Been Received.', 'Our team will review your brief and contact you to discuss the most suitable production or service approach for your project.'),
                 error=("We Couldn't Submit Your Brief.", f"Please check your information and try again. You can also contact us directly at {SITE['phone1']}."))
    nexts = [('bi-inbox-fill', 'We review your brief', 'Our team studies your requirements and may contact you for clarifications.'),
             ('bi-chat-dots-fill', 'We discuss the approach', 'We recommend the most suitable production or service approach.'),
             ('bi-file-earmark-text-fill', 'You receive a proposal', 'A clear scope, timeline and quote for your approval.')]
    body = '\n'.join([
        phero(eyebrow='Get a quote', title='Tell Us About Your <span class="serif grad-text">Project.</span>', sub='Every Great Project Begins With a Conversation.',
              lead='Share your photography, video production, digital marketing, or event management requirements. Our team will review your brief and discuss the most suitable production or service approach for your project.',
              crumbs=[('Get a Quote', None)], compact=True),
        f'''    <section class="section quote-sec">
      <div class="container-x">
        <div class="split split--quote">
          <div class="form-card reveal">{qform}</div>
          <aside class="quote__aside">
            <div class="glass glance reveal"><h2 class="glance__h">What happens next?</h2>
              <ol class="nexts">{''.join(f'<li><span class="icon-tile xs"><i class="bi {i}"></i></span><div><b>{t}</b><small>{d}</small></div></li>' for i, t, d in nexts)}</ol>
            </div>
            <div class="glass glance reveal mt-3"><h2 class="glance__h">Prefer to talk?</h2>
              <p><a href="tel:{SITE['phone1_tel']}">{SITE['phone1_disp']}</a><br><a href="tel:{SITE['phone2_tel']}">{SITE['phone2_disp']}</a><br><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
              {btn('Chat on WhatsApp', wa_link(), 'dark', 'bi-whatsapp', ext=True)}
            </div>
          </aside>
        </div>
      </div>
    </section>''',
    ])
    return page('get-a-quote/', title='Get a Quote | Playback Media & Events Hub',
                desc='Request a custom proposal for photography, video production, digital marketing or event management from Playback Media & Events Hub.',
                body=body, active='', crumbs=[('Get a Quote', None)])

# ---------------------------------------------------------------------------
# LEGAL & 404
# ---------------------------------------------------------------------------
def legal(slug, title, html_):
    body = '\n'.join([
        phero(eyebrow='Legal', title=title, sub=f'Last updated: {fmt_date("2026-10-21")}', crumbs=[(title, None)], compact=True),
        f'''    <section class="section">
      <div class="container-x"><div class="prose prose--legal">{html_}</div></div>
    </section>''',
    ])
    return page(slug + '/', title=f'{title} | Playback Media & Events Hub', desc=f'{title} for the Playback Media & Events Hub website.', body=body, crumbs=[(title, None)])

PRIVACY = f'''
<p>This Privacy Policy explains how {SITE['name']} (&ldquo;Playback&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) collects, uses and protects personal information when you visit <a href="{SITE['url']}">www.playbackmedia.in</a>, contact us, request a quote, apply for a job or register as a freelancer.</p>
<h2>Information we collect</h2>
<ul><li><strong>Enquiries and quotes:</strong> name, email address, mobile number, company or organisation, location, service requirements and any details you include in your message or brief.</li>
<li><strong>Job applications and freelancer registrations:</strong> contact details, city, experience, skills, equipment, availability, portfolio links, resumes or profiles you upload, and any additional information you provide.</li>
<li><strong>Technical information:</strong> the page from which you submitted a form, campaign (UTM) parameters, and standard information collected by our hosting and analytics providers, such as browser type and approximate location.</li></ul>
<h2>How we use your information</h2>
<ul><li>To respond to enquiries and prepare proposals and quotations.</li><li>To deliver the services you engage us for and communicate about your project.</li>
<li>To review job applications and freelancer profiles for suitable opportunities.</li><li>To improve our website and understand which pages and campaigns are useful.</li>
<li>To comply with legal obligations.</li></ul>
<p>We do not sell your personal information.</p>
<h2>Legal basis and consent</h2>
<p>We process personal data with your consent, which you provide when submitting our forms, and where necessary to respond to your request or perform a contract with you, in accordance with applicable Indian law, including the Digital Personal Data Protection Act, 2023.</p>
<h2>Sharing</h2>
<p>We share information only with service providers who help us operate our website, forms, email and customer-relationship systems, and only as needed for those purposes, or where required by law.</p>
<h2>Retention</h2>
<p>We keep enquiry records for as long as needed to respond and maintain business records. Job applications and freelancer profiles are retained for future opportunities unless you ask us to delete them.</p>
<h2>Your rights</h2>
<p>You may ask to access, correct or delete your personal information, or withdraw consent, by emailing <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
<h2>Photographs and videos</h2>
<p>Images and videos shown on this website are from Playback projects. If you appear in our work and would like an image reviewed or removed, please contact us.</p>
<h2>Third-party content</h2>
<p>Videos on this website are embedded from YouTube and load only when you choose to play them. YouTube&rsquo;s own privacy policy applies to those players.</p>
<h2>Contact</h2>
<p>{SITE['name']}, {SITE['location']}. Email: <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Phone: <a href="tel:{SITE['phone1_tel']}">{SITE['phone1']}</a>.</p>
<p><em>We may update this policy from time to time. The latest version will always be available on this page.</em></p>'''

TERMS = f'''
<p>These Terms &amp; Conditions govern your use of the {SITE['name']} website. By using this website you agree to these terms.</p>
<h2>Use of the website</h2>
<p>This website provides information about our photography, video production, digital marketing and event management services. You agree to use it lawfully and not to attempt to disrupt or misuse it or its forms.</p>
<h2>Intellectual property</h2>
<p>Unless stated otherwise, the photographs, videos, text, graphics and logos on this website are owned by or licensed to Playback, or belong to our clients and are shown with permission. They may not be copied, reproduced or used without written consent.</p>
<h2>Enquiries and quotations</h2>
<p>Submitting an enquiry or quote request does not create a contract. Services are confirmed only through a written proposal or agreement accepted by both parties, which will set out the scope, deliverables, timelines, fees and payment terms.</p>
<h2>Careers and freelancer registration</h2>
<p>Submitting an application or registering as a freelancer does not guarantee work, engagement or employment.</p>
<h2>Accuracy of information</h2>
<p>We aim to keep information accurate and up to date but do not guarantee that all content is complete or current. Service details may change without notice.</p>
<h2>External links</h2>
<p>This website links to external platforms such as YouTube, Instagram, LinkedIn, Facebook and WhatsApp. We are not responsible for the content or policies of those websites.</p>
<h2>Limitation of liability</h2>
<p>To the extent permitted by law, Playback is not liable for any loss arising from the use of this website or reliance on its content.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of India. Disputes are subject to the jurisdiction of the courts of Ghaziabad, Uttar Pradesh.</p>
<h2>Contact</h2>
<p>Questions about these terms can be sent to <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>'''

def not_found():
    body = '\n'.join([
        phero(eyebrow='Error 404', title='This page took a <span class="serif grad-text">different take.</span>',
              sub='The page you are looking for may have moved. Here are some useful places to continue.',
              actions=btn('Back to Home', '', 'grad', 'bi-house-fill') + btn('Our Services', 'services/', 'ghost') + btn('Contact Us', 'contact-us/', 'ghost', 'bi-envelope-fill')),
    ])
    return page('404/', title='Page Not Found | Playback Media & Events Hub', desc='The page you requested could not be found.', body=body)
