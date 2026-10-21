"""Service division pages and specialised service pages (handover sections 12–15)."""
from core import (page, phero, shead, icon_card, img_card, steps, faq, faq_schema, gallery, vgrid, chips, checklist,
                  cta_band, enquiry_form, btn, esc)
from data import SITE, DIVISIONS, PROJECT_BY_SLUG, project_images, wa_link, SUPPORTING

def imgs_from(*slugs, per=3):
    out = []
    for s in slugs:
        out += project_images(PROJECT_BY_SLUG[s])[:per]
    return out

DIV_BY_KEY = {d['key']: d for d in DIVISIONS}
SUB_TO_DIV = {s: d for d in DIVISIONS for s, _ in d['subs']}
NAME = {s: n for d in DIVISIONS for s, n in d['subs']}
NAME.update({d['slug']: d['name'] for d in DIVISIONS})

PHOTO_PROCESS = [('Brief', 'We understand the purpose, audience, locations and the images you need.'),
                 ('Planning', 'Shot lists, schedules, styling, lighting and logistics are agreed in advance.'),
                 ('Shoot', 'Our photographers work efficiently and professionally on the day.'),
                 ('Editing', 'Selection, colour correction and retouching to a consistent standard.'),
                 ('Delivery', 'Final images delivered in the formats your platforms need.')]
VIDEO_PROCESS = [('Discover', 'Message, audience, platform, timeline and budget.'),
                 ('Pre-Production', 'Script, storyboard, locations, crew and schedules.'),
                 ('Filming', 'Professional cameras, lighting and sound on set.'),
                 ('Post-Production', 'Editing, colour, sound, graphics and subtitles.'),
                 ('Delivery', 'Final versions for every platform you need.')]
DIGITAL_PROCESS = [('Discover', 'Your business, audience, competitors and goals.'),
                   ('Plan', 'Channels, content calendar, budgets and measures of success.'),
                   ('Create', 'Photography, video, design and copy produced in-house.'),
                   ('Launch', 'Campaigns, posts and pages published and managed.'),
                   ('Review', 'Regular reporting and improvements based on results.')]
EVENT_PROCESS = [('Understand the Brief', 'Objectives, programme, venue, audience and budget.'),
                 ('Develop the Scope', 'A clear proposal covering production and services.'),
                 ('Coordinate Resources', 'Vendors, crew, equipment and schedules aligned.'),
                 ('Technical Setup', 'Stage, AV, LED, branding and rehearsals at the venue.'),
                 ('Event Execution', 'Our team on the floor managing every session.'),
                 ('Post-Event Deliverables', 'Photographs, recordings, highlight films and reports.')]

S = {}

# ---------------------------------------------------------------------------
# PHOTOGRAPHY
# ---------------------------------------------------------------------------
S['photography'] = dict(
    div='photography', kind='division', seo='Professional Photography Services in Delhi NCR | Playback Media & Events Hub',
    meta='Corporate, product, portfolio, event, conference and healthcare photography in Delhi NCR by Playback Media & Events Hub.',
    eyebrow='Photography Division', h1='Professional Photography Services in <span class="serif grad-text">Delhi NCR</span>',
    sub='Capturing People, Products, Brands &amp; Experiences With Purpose.',
    image='assets/img/portrait-fashion.webp',
    intro=['Photography is one of the foundational strengths of Playback Media &amp; Events Hub.',
           'We provide professional photography solutions for businesses, brands, healthcare organizations, institutions, events, and individuals.',
           "From corporate portraits and commercial product shoots to event documentation, portfolios, and professional branding imagery, our photography services are developed around each client's purpose and requirements.",
           'Our approach combines creative composition, technical understanding, production planning, and professional image processing.'],
    cards=[('bi-briefcase-fill', 'Corporate Photography', 'Executive portraits, professional headshots, office photography, team photographs, workplace visuals, and corporate communication.', 'corporate-photography/', 'Explore Corporate Photography'),
           ('bi-box-seam-fill', 'Product &amp; Commercial Photography', 'Product images, catalogue photographs, e-commerce content, lifestyle product photography, and advertising visuals.', 'product-photography/', 'Explore Product Photography'),
           ('bi-person-bounding-box', 'Portfolio &amp; Headshots', 'Professional portfolio photography, personal branding, professional portraits, commercial portfolios, and fashion-related assignments.', 'portfolio-photography/', 'Explore Portfolio Photography'),
           ('bi-people-fill', 'Event &amp; Conference Photography', 'Corporate events, medical conferences, scientific seminars, exhibitions, awards, professional gatherings, and institutional programs.', 'event-photography/', 'Explore Event Photography'),
           ('bi-heart-pulse-fill', 'Healthcare Photography', "Doctors' portraits, hospital facilities, healthcare teams, medical events, and permitted professional healthcare photography.", 'medical-conference-management/', 'See Healthcare Work')],
    card_images=['assets/img/work/studio-portrait-interior-shoots/01-sm.webp', 'assets/img/work/product-commercial-photography/01-sm.webp',
                 'assets/img/portrait-fashion.webp', 'assets/img/work/nse-emerge-listing/01-sm.webp', 'assets/img/work/apccsm-medical-workshop/01-sm.webp'],
    gallery=imgs_from('nse-emerge-listing', 'product-commercial-photography', 'first-birthday-shoot', 'apccsm-medical-workshop', 'northern-india-polo-championship', 'stage-performance-shoot', per=2),
    process=PHOTO_PROCESS, process_title='Photography Production <span class="serif grad-text">Process.</span>',
    cta=('Book a Photography Shoot', 'Photography'),
    faqs=[('Do you travel outside Delhi NCR for shoots?', 'Yes. We are based in Ghaziabad and work across Delhi NCR and North India, and we can plan assignments in other locations depending on the scope.'),
          ('How quickly will we receive our photographs?', 'Timelines depend on the volume and editing involved. We agree delivery dates during planning, and urgent selections for social media or press can be prioritised.'),
          ('Can you photograph at our office or factory?', 'Yes. We bring portable lighting and backdrops for on-location corporate portraits, team photographs and workplace or industrial photography.'),
          ('Do you provide edited and retouched images?', 'Every assignment includes professional selection and editing. Detailed retouching for portraits, products or advertising can be included as needed.')],
    related=['video-production', 'event-management', 'social-media-marketing'],
)

S['corporate-photography'] = dict(
    div='photography', seo='Corporate Photography in Delhi NCR | Playback Media & Events Hub',
    meta='Executive portraits, headshots, team photographs and workplace photography for websites, brochures and annual reports in Delhi NCR.',
    h1='Corporate <span class="serif grad-text">Photography</span>', sub='Professional images that represent your organisation with confidence.',
    image='assets/img/work/studio-portrait-interior-shoots/01.webp',
    intro=['Playback creates professional portraits, office images, team photographs, and business visuals for websites, brochures, company profiles, annual reports, and corporate communications.',
           'We plan each shoot around how the images will be used, so your leadership, people and workplace are presented consistently across every platform.'],
    included=['Executive portraits &amp; leadership photographs', 'Professional headshots for teams', 'Office, factory &amp; workplace photography', 'Team and group photographs',
              'Green-screen and studio portraits', 'Images for annual reports, brochures &amp; websites'],
    cards=[('bi-person-badge-fill', 'Leadership portraits', 'Confident, well-lit portraits for profiles, press releases and annual reports.'),
           ('bi-buildings-fill', 'Workplace visuals', 'Offices, facilities, production lines and people at work, photographed authentically.'),
           ('bi-people-fill', 'Team photographs', 'Consistent headshots and group photographs organised efficiently on site.')],
    gallery=imgs_from('studio-portrait-interior-shoots', 'nse-emerge-listing', 'india-post-postal-congress', per=3),
    process=PHOTO_PROCESS, cta=('Book a Corporate Shoot', 'Photography'),
    faqs=[('Can you shoot headshots for our whole team in one day?', 'Yes. We set up a portable studio at your office and photograph team members in short, scheduled sessions with consistent lighting.'),
          ('Do you photograph factories and industrial facilities?', 'Yes. We regularly photograph manufacturing units, equipment and processes, following your site safety requirements.'),
          ('Will the images be consistent with our brand?', 'We agree backgrounds, framing and colour treatment in advance so every image matches your brand guidelines.')],
    related=['portfolio-photography', 'corporate-films', 'website-development'],
)

S['product-photography'] = dict(
    div='photography', seo='Product Photography in Delhi NCR | E-commerce & Catalogue | Playback',
    meta='Product, catalogue, e-commerce and advertising photography for brands and manufacturers in Delhi NCR.',
    h1='Product &amp; Commercial <span class="serif grad-text">Photography</span>', sub='Clear, attractive images that help your products sell.',
    image='assets/img/work/product-commercial-photography/02.webp',
    intro=['Our product photography services help businesses present products clearly and professionally for catalogues, digital stores, websites, and promotional campaigns.',
           'From small packaged goods to furniture, industrial equipment and construction machinery, we plan lighting, angles and styling to match each platform.'],
    included=['Studio photography on white or styled backgrounds', 'E-commerce images to marketplace specifications', 'Catalogue &amp; brochure photography',
              'Lifestyle and in-use product setups', 'Industrial equipment &amp; machinery', 'Retouching and colour accuracy'],
    cards=[('bi-bag-fill', 'E-commerce ready', 'Consistent angles, clean backgrounds and correct sizes for online stores and marketplaces.'),
           ('bi-lamp-fill', 'Lifestyle setups', 'Products photographed in context to help customers imagine using them.'),
           ('bi-gear-wide-connected', 'Industrial products', 'Large equipment photographed on location with controlled lighting.')],
    gallery=project_images(PROJECT_BY_SLUG['product-commercial-photography']),
    process=PHOTO_PROCESS, cta=('Book a Product Shoot', 'Photography'),
    faqs=[('Can you photograph products for Amazon or Flipkart listings?', 'Yes. We follow marketplace image requirements, including white backgrounds, angles and sizes.'),
          ('Do you shoot large products on location?', 'Yes. Furniture, machinery and installations can be photographed at your showroom, factory or site.'),
          ('Can you also produce a product video?', 'Yes. Our video team can create product demonstrations and advertising films alongside the photography.')],
    related=['advertising-films', 'social-media-marketing', 'website-development'],
)

S['portfolio-photography'] = dict(
    div='photography', seo='Portfolio & Headshot Photography in Delhi NCR | Playback',
    meta='Professional portfolio, personal branding and headshot photography for professionals, models and creators in Delhi NCR.',
    h1='Portfolio &amp; Headshot <span class="serif grad-text">Photography</span>', sub='Portraits that reflect who you are and where you are going.',
    image='assets/img/portrait-fashion.webp',
    intro=["We create professional portfolios, portraits, and personal branding photographs with attention to the individual's style, intended use, and creative requirements.",
           'Whether you need headshots for LinkedIn, a model portfolio, images for a personal brand or portraits for a family milestone, we plan the look, locations and styling with you.'],
    included=['Professional headshots', 'Personal branding photographs', 'Model &amp; actor portfolios', 'Fashion-related assignments', 'Indoor studio and outdoor locations', 'Family and celebration portraits'],
    cards=[('bi-linkedin', 'Professional headshots', 'Clean, approachable portraits for LinkedIn, websites and speaker profiles.'),
           ('bi-stars', 'Personal branding', 'A set of images for creators and consultants to use across platforms.'),
           ('bi-camera2', 'Portfolios', 'Varied looks and locations for models, actors and creative professionals.')],
    gallery=imgs_from('intogain-razzmatazz', 'first-birthday-shoot', 'anniversary-celebration', 'studio-portrait-interior-shoots', per=3),
    process=PHOTO_PROCESS, cta=('Book a Portrait Session', 'Photography'),
    faqs=[('How should I prepare for a portfolio shoot?', 'We share a short preparation guide covering outfits, grooming and references, and discuss the looks you want before the session.'),
          ('Can we shoot outdoors?', 'Yes. We can combine studio portraits with outdoor locations in and around Delhi NCR.'),
          ('Do you photograph family celebrations?', 'Yes. We photograph birthdays, anniversaries and family portraits with the same planning and care as our professional assignments.')],
    related=['corporate-photography', 'promotional-videos', 'social-media-marketing'],
)

S['event-photography'] = dict(
    div='photography', seo='Event & Conference Photography in Delhi NCR | Playback',
    meta='Professional photography for corporate events, medical conferences, seminars, exhibitions and award ceremonies in Delhi NCR.',
    h1='Event &amp; Conference <span class="serif grad-text">Photography</span>', sub='Every speaker, delegate and important moment, professionally documented.',
    image='assets/img/work/hcl-domino-jams/01.webp',
    intro=['From keynote speakers and delegates to exhibitions, awards, and networking, our event photography documents important professional experiences.',
           'Our photographers understand conference programmes, multi-hall sessions and stage lighting, so we are in the right place for every key moment without disturbing the proceedings.'],
    included=['Keynote, speaker &amp; panel photography', 'Delegate, networking &amp; candid coverage', 'Award &amp; felicitation moments', 'Exhibition &amp; sponsor stall coverage',
              'Multi-hall coverage with multiple photographers', 'Same-day selections for social media'],
    cards=[('bi-mic-fill', 'Speakers &amp; sessions', 'Clear photographs of every speaker and session, including LED stages and low light.'),
           ('bi-award-fill', 'Awards &amp; ceremonies', 'Every presentation captured, with group photographs organised quickly.'),
           ('bi-shop', 'Exhibitions &amp; sponsors', 'Sponsor stalls and branding photographed for sponsor reports.')],
    gallery=imgs_from('hcl-domino-jams', 'flipkart-seller-hub-night', 'apccsm-medical-workshop', 'tata-milestones-2023', 'commvault-partner-summit', per=2),
    process=PHOTO_PROCESS, cta=('Book Event Photography', 'Photography'),
    faqs=[('Can you cover multiple halls at a conference?', 'Yes. We assign photographers to each hall and coordinate coverage of keynotes, workshops and exhibitions.'),
          ('Can we get photographs during the event?', 'Yes. We can deliver selected edited images during or at the end of each day for social media and press.'),
          ('Do you also provide event videography?', 'Yes. Our video team can provide session recordings, interviews and highlight films alongside photography.')],
    related=['event-management', 'video-production', 'live-streaming'],
)

# ---------------------------------------------------------------------------
# VIDEO
# ---------------------------------------------------------------------------
S['video-production'] = dict(
    div='video', kind='division', seo='Videography & Film Production in Delhi NCR | Playback Media & Events Hub',
    meta='Corporate films, advertising films, TV production, documentaries, interviews, training videos and editing in Delhi NCR.',
    eyebrow='Videography & Film Production', h1='Professional Videography &amp; Film Production in <span class="serif grad-text">Delhi NCR</span>',
    sub='Powerful Stories. Professional Production. Lasting Impact.',
    image='assets/img/greenscreen.webp',
    intro=['At Playback Media &amp; Events Hub, filmmaking and video production are central to our creative identity.',
           'Our work spans television productions, corporate films, advertising films, documentaries, promotional content, interviews, testimonials, training videos, conference recordings, and digital media.',
           'From creative planning and filming to editing, motion graphics, sound processing, and final delivery, our services are designed to create videos that communicate clearly and professionally.',
           'We develop each production according to the message, audience, distribution platform, timeline, and approved creative requirements.'],
    cards=[('bi-building', 'Corporate Films', 'Company profiles, corporate presentations, leadership videos, infrastructure films, CSR stories, and business communication.', 'corporate-films/', 'Explore Corporate Films'),
           ('bi-megaphone-fill', 'Advertising Films', 'Product advertisements, promotional campaigns, branded video content, and commercial productions.', 'advertising-films/', 'Explore Advertising Films'),
           ('bi-tv-fill', 'Television Production', 'Studio and field production, television programming, multi-camera filming, and associated post-production.', 'television-production/', 'Explore TV Production'),
           ('bi-journal-richtext', 'Documentaries &amp; Profile Films', 'Professional profiles, biographies, institutional documentaries, and narrative visual content.', 'television-production/', 'See Documentaries'),
           ('bi-people-fill', 'Event &amp; Conference Videography', 'Medical conferences, corporate events, seminars, exhibitions, speaker recordings, and highlight films.', 'live-streaming/', 'Event Video &amp; Streaming'),
           ('bi-chat-quote-fill', 'Interviews &amp; Testimonials', 'Doctor interviews, client testimonials, leadership messages, employee interviews, and educational conversations.', 'promotional-videos/', 'Explore Interviews'),
           ('bi-mortarboard-fill', 'Educational &amp; Training Videos', 'Training programs, professional lectures, online learning, webinars, and educational course videos.', 'corporate-films/', 'See Training Films'),
           ('bi-phone-fill', 'Reels &amp; Short-Form Content', 'Instagram Reels, YouTube Shorts, LinkedIn videos, promotional clips, and social media content.', 'promotional-videos/', 'Explore Reels'),
           ('bi-scissors', 'Video Editing &amp; Post-Production', 'Video editing, color correction, audio refinement, subtitles, motion graphics, and versioning for different platforms.', 'video-editing/', 'Explore Editing')],
    videos=['dOcs6BJY2QE', 'L6uL6tO5wFY', 'eKAqUBHCgos', 'z51spm2RWTw', '3YBUpojm99g', 'XKGHE9YKoiY'],
    process=VIDEO_PROCESS, process_title='Our Production <span class="serif grad-text">Process.</span>',
    cta=('Start Your Video Project', 'Videography & Film Production'),
    faqs=[('How long does a corporate film take to produce?', 'A typical corporate film takes two to four weeks from script approval to delivery, depending on locations, interviews and graphics.'),
          ('Do you write scripts?', 'Yes. We develop concepts and scripts with you, or work from your approved script.'),
          ('Can you deliver versions for social media?', 'Yes. We deliver landscape, square and vertical versions, short cut-downs and subtitled versions as required.'),
          ('Do you have television production experience?', 'Yes. Our leadership has directed more than 500 television episodes, including the quiz show Aao Baniye Gursikh Pyara.')],
    related=['photography', 'digital-marketing', 'event-management'],
)

S['corporate-films'] = dict(
    div='video', seo='Corporate Film Production in Delhi NCR | Playback Media & Events Hub',
    meta='Corporate films, company profiles, institutional and training videos produced in Delhi NCR by Playback.',
    h1='Corporate <span class="serif grad-text">Films</span>', sub='Introduce your organisation, its people and its purpose.',
    image='assets/img/keynote.webp',
    intro=['Playback produces corporate videos that introduce businesses, communicate brand values, document facilities and processes, and support professional marketing and organizational communication.',
           'We have produced corporate and institutional films for manufacturers, hospitals, colleges, universities and service companies, in English, Hindi and other language versions.'],
    included=['Company profile films', 'Leadership &amp; corporate messages', 'Infrastructure &amp; facility films', 'CSR and impact stories', 'Institutional &amp; campus films', 'Training and educational videos'],
    cards=[('bi-building', 'Company profiles', 'A clear introduction to who you are, what you do and why it matters.'),
           ('bi-gear-wide-connected', 'Facility &amp; process films', 'Manufacturing, quality and infrastructure filmed with care and accuracy.'),
           ('bi-mortarboard-fill', 'Training videos', 'Structured learning content for staff, hospitals and institutions.')],
    videos=['L6uL6tO5wFY', 'VvQF5U4B3zw', 'ObVF1SlWBa0', 'Bm9mO081wGQ', 'pOEIfgYN9gg', 'ONGK-4ZsNBg'],
    process=VIDEO_PROCESS, cta=('Plan Your Corporate Film', 'Videography & Film Production'),
    faqs=[('Can you film at multiple locations?', 'Yes. We plan multi-location shoots across offices, factories and sites, and coordinate permissions in advance.'),
          ('Can the film be produced in two languages?', 'Yes. We can produce separate language versions or add subtitles and voice-overs.'),
          ('Do you provide voice-over and music?', 'Yes. We arrange professional voice-over artists and licensed music as part of post-production.')],
    related=['corporate-photography', 'video-editing', 'website-development'],
)

S['advertising-films'] = dict(
    div='video', seo='Advertising Film Production in Delhi NCR | Ad Films | Playback',
    meta='Product advertisements, promotional films and branded video content for brands in Delhi NCR.',
    h1='Advertising <span class="serif grad-text">Films</span>', sub='Video that presents your product and moves your audience.',
    image='assets/img/work/product-commercial-photography/03.webp',
    intro=['We develop advertising and promotional video content designed to present products, communicate brand messages, and engage target audiences across suitable platforms.',
           'From concept and casting to filming, product demonstration and final edit, we produce advertisements for digital platforms, events and broadcast.'],
    included=['Product advertisements', 'Promotional &amp; launch films', 'Product demonstration videos', 'Branded content for social media', 'Chroma (green screen) productions', 'Real estate &amp; property promos'],
    cards=[('bi-lightbulb-fill', 'Concept &amp; script', 'A clear idea built around your product and your audience.'),
           ('bi-camera-reels-fill', 'Production', 'Professional crew, lighting and direction in studio or on location.'),
           ('bi-collection-play-fill', 'Platform versions', 'Edits sized for Instagram, YouTube, OTT pre-roll and events.')],
    videos=['XKGHE9YKoiY', '1xodV0zYdSg', 'top-_Te4Qmk', 'ZC__7UGjz0U', '4qPeOYxBEUQ', 'R77Nuh54I8M'],
    process=VIDEO_PROCESS, cta=('Discuss Your Advertising Film', 'Videography & Film Production'),
    faqs=[('What budget do I need for an advertising film?', 'Budgets depend on the concept, cast, locations and duration. Share your objective and we will propose options to suit your budget.'),
          ('Can you combine the film with product photography?', 'Yes. We often photograph products during the same production to save time and keep visuals consistent.'),
          ('Do you help with running the ads?', 'Yes. Our digital marketing team can plan and manage Google and Meta advertising campaigns.')],
    related=['product-photography', 'performance-marketing', 'promotional-videos'],
)

S['television-production'] = dict(
    div='video', seo='TV & Documentary Production in Delhi NCR | Playback Media & Events Hub',
    meta='Television programming, multi-camera studio and field production, documentaries and biography films by Playback.',
    h1='TV &amp; Documentary <span class="serif grad-text">Production</span>', sub='Long-format storytelling with broadcast discipline.',
    image='assets/img/greenscreen.webp',
    intro=['Our media production experience includes television-related assignments, professional filming, studio and field production, and long-format content.',
           'Our leadership has directed more than 500 episodes of the Punjabi television quiz show <em>Aao Baniye Gursikh Pyara</em> and special series such as <em>Sikh Yodhe</em>, and has produced biographical and social documentaries.'],
    included=['Multi-camera studio production', 'Field production', 'Television programming &amp; series', 'Documentaries &amp; biographies', 'Institutional documentaries', 'Broadcast-standard post-production'],
    cards=[('bi-tv-fill', '500+ TV episodes', 'Production and direction experience on a long-running television quiz show.'),
           ('bi-camera-video-fill', 'Multi-camera', 'Studio and field setups with switching, recording and live editing.'),
           ('bi-journal-richtext', 'Documentaries', 'Research-led biographies and social documentaries told with care.')],
    videos=['eKAqUBHCgos', '8JFiPOTUG7A', 'p6J_J6dj1XE', 'z51spm2RWTw', '1_dhhKhAAzs', '3C_8eSLBT8g'],
    process=VIDEO_PROCESS, cta=('Discuss Your Production', 'Videography & Film Production'),
    faqs=[('Can you produce a full television series?', 'Yes. We plan and produce episodic content, including multi-camera studio production, direction and post-production.'),
          ('Do you produce documentaries for institutions?', 'Yes. We produce institutional, biographical and social documentaries, including research, interviews and narrative editing.')],
    related=['video-editing', 'live-streaming', 'corporate-films'],
)

S['video-editing'] = dict(
    div='video', seo='Video Editing & Post-Production Services in Delhi NCR | Playback',
    meta='Professional video editing, colour correction, sound, subtitles and motion graphics by Playback Media & Events Hub.',
    h1='Video Editing &amp; <span class="serif grad-text">Post-Production</span>', sub='Turning footage into polished, purposeful films.',
    image='assets/img/work/azad-bhawan-seminar/04.webp',
    intro=['Our editing services transform recorded footage into polished videos through storytelling, sound refinement, color correction, graphics, captions, and final processing.',
           'We edit our own productions and footage supplied by clients, from conference recordings and highlight films to motion graphic explainers and multi-language versions.'],
    included=['Story-led editing', 'Colour correction &amp; grading', 'Audio cleanup &amp; mixing', 'Subtitles &amp; captions', 'Motion graphics &amp; titles', 'Versions for every platform', 'Live multi-camera editing at events'],
    cards=[('bi-scissors', 'Editing', 'Structure, pace and story shaped around your message.'),
           ('bi-palette-fill', 'Colour &amp; sound', 'Consistent colour and clear, balanced audio.'),
           ('bi-magic', 'Motion graphics', 'Titles, lower thirds, animations and explainer videos.')],
    videos=['WW15w_4Z2FI', 'NIDHO0DOaKM', 'STDvW4bSBqM', 'sKIqCyvVWTA', 'wdmT-hcO0Vk', 'jQX4BoyA5dA'],
    process=[('Brief', 'Purpose, audience, length and references.'), ('Assembly', 'Footage reviewed and a first cut prepared.'),
             ('Refinement', 'Your feedback incorporated into the edit.'), ('Finishing', 'Colour, sound, graphics and subtitles.'), ('Delivery', 'Final files for every platform.')],
    cta=('Send Us Your Footage', 'Video Editing'),
    faqs=[('Can you edit footage we have already shot?', 'Yes. Share your footage and requirements, and we will advise on what is possible and the timeline.'),
          ('How many revisions are included?', 'We agree the number of review rounds in the proposal; most projects include two rounds of changes.'),
          ('Can you add subtitles in Hindi and English?', 'Yes. We create subtitles and captions in English, Hindi and other languages on request.')],
    related=['promotional-videos', 'social-media-marketing', 'corporate-films'],
)

S['promotional-videos'] = dict(
    div='video', seo='Interviews, Testimonials & Reels Production in Delhi NCR | Playback',
    meta='Doctor interviews, client testimonials, video profiles, product demos and Instagram Reels produced in Delhi NCR.',
    h1='Interviews, Testimonials &amp; <span class="serif grad-text">Reels</span>', sub='Authentic voices and short-form stories for every platform.',
    image='assets/img/work/orange-klinic-healthcare-workshop/06.webp',
    intro=['We create professional interviews, testimonials, educational videos, product demonstrations, and short-form promotional content for brands and businesses.',
           'Our crews make speakers comfortable on camera, light and record them professionally, and edit content for YouTube, Instagram, LinkedIn and websites.'],
    included=['Doctor &amp; expert interviews', 'Client testimonials', 'Leadership messages', 'Video profiles &amp; video resumes', 'Instagram Reels &amp; YouTube Shorts', 'Product demonstrations'],
    cards=[('bi-chat-quote-fill', 'Testimonials', 'Real clients speaking naturally about their experience.'),
           ('bi-person-video3', 'Profiles', 'Video profiles for professionals, leaders and public figures.'),
           ('bi-phone-fill', 'Reels', 'Vertical short-form content designed for social engagement.')],
    videos=['SMiSt3EFImM', 'kWEsJZ8CEuk', 'VjsDp0_WojQ', '1l6g1eW-p3w', 'G85HUWhz9zw', 'xc106L2Pj0w'],
    process=VIDEO_PROCESS, cta=('Plan Your Video Content', 'Videography & Film Production'),
    faqs=[('Can you produce a batch of reels in one shoot?', 'Yes. We plan several reels and short videos for a single shoot day to make content production efficient.'),
          ('We are nervous on camera. Can you help?', 'Absolutely. We prepare questions in advance, keep the setup relaxed and guide speakers throughout the interview.')],
    related=['social-media-marketing', 'healthcare-digital-marketing', 'video-editing'],
)

# ---------------------------------------------------------------------------
# DIGITAL MARKETING
# ---------------------------------------------------------------------------
S['digital-marketing'] = dict(
    div='digital', kind='division', seo='Digital Marketing Agency in Delhi NCR | Playback Media & Events Hub',
    meta='Social media marketing, SEO, Google and Meta Ads, websites, healthcare digital marketing and influencer marketing in Delhi NCR.',
    eyebrow='Digital Marketing Division', h1='Digital Marketing Agency in <span class="serif grad-text">Delhi NCR</span>',
    sub='Creative Content. Strategic Communication. Digital Growth.',
    image='assets/img/concert-crowd.webp', mock=True,
    intro=['Playback Media &amp; Events Hub combines media production expertise with digital marketing services to help businesses strengthen their online communication and visibility.',
           'Since expanding into digital services in 2018, our capabilities have included social media marketing, SEO, website development, digital advertising, content production, and online campaign support.',
           'Our approach brings creative content and digital strategy together so that businesses can communicate consistently with their intended audiences.'],
    cards=[('bi-instagram', 'Social Media Marketing', 'Content strategy, social media creatives, reels, account management, publishing calendars, and promotional communication.', 'social-media-marketing/', 'Explore Social Media'),
           ('bi-search', 'Search Engine Optimization', 'SEO audits, keyword planning, on-page optimization, local SEO, technical recommendations, and content improvement.', 'seo-services/', 'Explore SEO'),
           ('bi-google', 'Google Ads &amp; Meta Ads', 'Advertising campaign planning, creative production, targeting, campaign management, and performance review.', 'performance-marketing/', 'Explore Ads'),
           ('bi-window-sidebar', 'Website Development', 'Business websites, professional landing pages, service websites, responsive design, and content management.', 'website-development/', 'Explore Websites'),
           ('bi-heart-pulse-fill', 'Healthcare Digital Marketing', 'Digital marketing and professional content support for doctors, hospitals, clinics, healthcare organizations, and medical associations.', 'healthcare-digital-marketing/', 'Explore Healthcare Marketing'),
           ('bi-camera-fill', 'Content Marketing', 'Professional photography, video production, articles, social media content, and promotional campaigns.', 'promotional-videos/', 'See Content Production'),
           ('bi-whatsapp', 'WhatsApp &amp; Email Marketing', 'Permission-based customer communications, email campaigns, newsletters, and suitable WhatsApp platform integrations.', None, None),
           ('bi-megaphone-fill', 'Influencer Marketing', 'Brand collaborations, influencer campaign coordination, and promotional content production, including family-oriented campaign opportunities.', 'influencer-marketing/', 'Explore Influencer Marketing')],
    videos=['G85HUWhz9zw', '1l6g1eW-p3w', '4qPeOYxBEUQ'],
    process=DIGITAL_PROCESS, process_title='How We Approach <span class="serif grad-text">Digital.</span>',
    cta=('Discuss Your Digital Marketing Goals', 'Digital Marketing'),
    faqs=[('Do you create the content as well as manage the accounts?', 'Yes. Because we are a production company, our photographers, videographers and designers create content in-house for your campaigns.'),
          ('How do you report on results?', 'We agree measures of success at the start and share regular reports on reach, engagement, enquiries and campaign performance.'),
          ('Do you work with doctors and hospitals?', 'Yes. Healthcare digital marketing is a specialisation, supported by our experience with medical conferences and doctor content.')],
    related=['website-development', 'promotional-videos', 'photography'],
)

S['social-media-marketing'] = dict(
    div='digital', seo='Social Media Marketing Agency in Delhi NCR | Playback',
    meta='Social media strategy, creatives, reels, account management and content calendars for brands and professionals in Delhi NCR.',
    h1='Social Media <span class="serif grad-text">Marketing</span>', sub='Consistent, creative content that builds your audience.',
    image='assets/img/work/flipkart-seller-hub-night/05.webp', mock=True,
    intro=['We plan, create and publish social media content that keeps your brand visible and consistent across Instagram, Facebook, LinkedIn and YouTube.',
           'Our in-house photography and video teams mean your feed is filled with original images, reels and short videos rather than generic stock content.'],
    included=['Content strategy &amp; monthly calendars', 'Social media creatives &amp; carousels', 'Reels &amp; short-form video', 'Account management &amp; publishing', 'Community engagement guidelines', 'Monthly performance reports'],
    cards=[('bi-calendar3', 'Planning', 'Monthly calendars aligned to your launches, events and campaigns.'),
           ('bi-camera-reels-fill', 'Original content', 'Photographs, reels and videos produced by our own teams.'),
           ('bi-bar-chart-line-fill', 'Reporting', 'Clear monthly insights and recommendations.')],
    videos=['1l6g1eW-p3w', 'MU3q9bkSXnQ', 'Wd6rnvPwNzk'],
    process=DIGITAL_PROCESS, cta=('Grow Your Social Presence', 'Digital Marketing'),
    faqs=[('Which platforms do you manage?', 'We manage Instagram, Facebook, LinkedIn and YouTube, and advise on the platforms best suited to your audience.'),
          ('How many posts will we get each month?', 'The posting frequency is agreed in your plan based on your goals and budget.'),
          ('Can you shoot content at our office or clinic?', 'Yes. We schedule regular content shoots so your feed features real people and places.')],
    related=['influencer-marketing', 'promotional-videos', 'performance-marketing'],
)

S['seo-services'] = dict(
    div='digital', seo='SEO & Local SEO Services in Delhi NCR | Playback Media & Events Hub',
    meta='SEO audits, keyword planning, on-page optimisation, local SEO and Google Business Profile support in Delhi NCR.',
    h1='SEO &amp; Local <span class="serif grad-text">SEO</span>', sub='Be found by the people already searching for you.',
    image='assets/img/work/cloud-service-providers-symposium/03.webp', mock=True,
    intro=['Search engine optimisation helps potential customers find your business when they search for your services.',
           'Our SEO services include audits, keyword planning, on-page optimisation, local SEO, technical recommendations and content improvement, with a particular focus on businesses serving Delhi NCR.'],
    included=['SEO audits', 'Keyword research &amp; planning', 'On-page optimisation', 'Local SEO &amp; Google Business Profile', 'Technical recommendations', 'Content improvement &amp; blogs'],
    cards=[('bi-clipboard-data-fill', 'Audit', 'A clear picture of what is helping and holding back your visibility.'),
           ('bi-geo-alt-fill', 'Local SEO', 'Stronger presence in local search and maps for Delhi NCR customers.'),
           ('bi-file-earmark-text-fill', 'Content', 'Useful pages and articles built around what your customers search.')],
    process=DIGITAL_PROCESS, cta=('Request an SEO Review', 'Digital Marketing'),
    faqs=[('How long does SEO take to show results?', 'SEO is a long-term activity. Improvements usually build over several months, depending on competition and the current state of your website.'),
          ('Do you guarantee first-page rankings?', 'No responsible agency can guarantee rankings. We focus on proven improvements and report progress transparently.'),
          ('Can you help with our Google Business Profile?', 'Yes. Local SEO includes optimising your Google Business Profile and local listings.')],
    related=['website-development', 'performance-marketing', 'social-media-marketing'],
)

S['performance-marketing'] = dict(
    div='digital', seo='Google Ads & Meta Ads Management in Delhi NCR | Playback',
    meta='Google Ads and Meta (Facebook & Instagram) Ads campaign planning, creatives, targeting and management for lead generation.',
    h1='Google Ads &amp; <span class="serif grad-text">Meta Ads</span>', sub='Advertising campaigns built to generate genuine enquiries.',
    image='assets/img/concert-crowd.webp', mock=True,
    intro=['We plan and manage advertising campaigns on Google, Facebook and Instagram, combining careful targeting with creative made by our own production teams.',
           'Every campaign begins with a clear objective, budget and measure of success, and is reviewed regularly so spend is directed to what works.'],
    included=['Campaign planning &amp; budgeting', 'Search, display &amp; video campaigns', 'Facebook &amp; Instagram campaigns', 'Ad creative: images, video &amp; copy', 'Audience targeting &amp; retargeting', 'Performance review &amp; reporting'],
    cards=[('bi-bullseye', 'Targeting', 'Reach the right people by location, interest and intent.'),
           ('bi-play-btn-fill', 'Creative', 'Ad images and videos produced in-house.'),
           ('bi-graph-up-arrow', 'Optimisation', 'Regular review of results and budgets.')],
    process=DIGITAL_PROCESS, cta=('Plan Your Ad Campaign', 'Digital Marketing'),
    faqs=[('What budget should we start with?', 'It depends on your market and objectives. We recommend a test budget, then scale what performs.'),
          ('Is the ad budget included in your fee?', 'No. Ad spend is paid directly to the platforms; our fee covers planning, creative and management.')],
    related=['social-media-marketing', 'seo-services', 'advertising-films'],
)

S['website-development'] = dict(
    div='digital', seo='Website Development Company in Delhi NCR | Playback Media & Events Hub',
    meta='Business websites, landing pages and service websites with responsive design and content management, built in Delhi NCR.',
    h1='Website <span class="serif grad-text">Development</span>', sub='Fast, responsive websites that represent your brand beautifully.',
    image='assets/img/portrait-fashion.webp', browser=True,
    intro=['We design and build business websites, professional landing pages and service websites that look as good as your brand films and work on every device.',
           'Each site is built for speed and search from the start, with content management so your team can keep it up to date, and enquiry forms that connect visitors to your business.'],
    included=['Business &amp; corporate websites', 'Landing pages for campaigns', 'Service &amp; portfolio websites', 'Responsive design for every device', 'Content management', 'SEO-ready structure &amp; speed', 'Enquiry forms &amp; WhatsApp integration'],
    cards=[('bi-phone-fill', 'Responsive', 'Designed for mobile first, refined for desktop.'),
           ('bi-lightning-charge-fill', 'Fast &amp; findable', 'Optimised for speed and search engines.'),
           ('bi-pencil-square', 'Easy to manage', 'Update pages, posts and portfolios yourself.')],
    process=[('Discover', 'Goals, audience, pages and content.'), ('Design', 'Visual direction and page layouts for approval.'),
             ('Build', 'Development, content entry and integrations.'), ('Test', 'Devices, speed, forms and SEO checks.'), ('Launch', 'Go live, training and ongoing support.')],
    cta=('Discuss Your Website', 'Website Development'),
    faqs=[('Can you write and photograph the content for our website?', 'Yes. Our photography, video and content teams can create everything your website needs.'),
          ('Will we be able to update the website ourselves?', 'Yes. We build with content management and provide training for your team.'),
          ('Do you provide hosting and maintenance?', 'We can recommend hosting and offer ongoing maintenance and support plans.')],
    related=['seo-services', 'corporate-photography', 'social-media-marketing'],
)

S['healthcare-digital-marketing'] = dict(
    div='digital', seo='Healthcare Digital Marketing for Doctors & Hospitals | Playback',
    meta='Digital marketing, patient-education videos, social media and SEO for doctors, hospitals, clinics and medical associations.',
    h1='Healthcare Digital <span class="serif grad-text">Marketing</span>', sub='Credible, responsible communication for healthcare professionals.',
    image='assets/img/work/orange-klinic-healthcare-workshop/01.webp',
    intro=['We provide digital marketing and professional content support for doctors, hospitals, clinics, healthcare organizations, and medical associations.',
           "Our experience producing YouTube content for doctors, hospital training films and more than 50 medical conference assignments helps us communicate healthcare topics accurately and responsibly."],
    included=['Patient-education videos for YouTube', "Doctors' portraits &amp; clinic photography", 'Social media for doctors &amp; hospitals', 'Healthcare SEO &amp; Google Business Profile', 'Websites for clinics &amp; hospitals', 'Conference &amp; CME promotion'],
    cards=[('bi-youtube', 'Doctor videos', 'Clear patient-education content filmed with doctors.'),
           ('bi-hospital-fill', 'Hospital content', 'Facility, team and service communication.'),
           ('bi-shield-check', 'Responsible', 'Content prepared with medical accuracy and appropriate approvals.')],
    videos=['G85HUWhz9zw', '7FdQpF8KXbw', 'MBmDHusiQ5g', 'pG0NPg5AuyY', 'FmptUJXA0so', 'XmEt5BASW74'],
    process=DIGITAL_PROCESS, cta=('Discuss Healthcare Marketing', 'Digital Marketing'),
    faqs=[('Do you follow medical advertising guidelines?', 'We prepare content responsibly and avoid misleading claims. Doctors review and approve all medical information before publishing.'),
          ('Can you film at our clinic?', 'Yes. We film discreetly, respecting patient privacy and obtaining permissions where needed.')],
    related=['medical-conference-management', 'promotional-videos', 'seo-services'],
)

S['influencer-marketing'] = dict(
    div='digital', seo='Influencer Marketing Agency in Delhi NCR | Playback Media & Events Hub',
    meta='Influencer collaborations, campaign coordination and promotional content production, including family-oriented campaigns.',
    h1='Influencer <span class="serif grad-text">Marketing</span>', sub='Authentic collaborations that put your brand in trusted hands.',
    image='assets/img/host-pink.webp',
    intro=['We coordinate brand collaborations with influencers and creators, from identifying suitable profiles to managing campaigns and producing promotional content.',
           'Our campaigns include family-oriented opportunities and creator content shot by our own production teams, so your collaborations look professional and stay on brand.'],
    included=['Influencer identification &amp; outreach', 'Campaign planning &amp; coordination', 'Content production with creators', 'Family-oriented campaign opportunities', 'Usage rights &amp; approvals', 'Campaign reporting'],
    cards=[('bi-people-fill', 'Right partners', 'Creators whose audiences match your customers.'),
           ('bi-camera-reels-fill', 'Professional content', 'Shoots produced by our photography and video teams.'),
           ('bi-clipboard-check-fill', 'Managed end to end', 'Briefs, approvals, schedules and reporting handled for you.')],
    videos=['1l6g1eW-p3w', 'MU3q9bkSXnQ', '1pIDhO-cPIU'],
    process=DIGITAL_PROCESS, cta=('Plan an Influencer Campaign', 'Digital Marketing'),
    faqs=[('Do you work with micro-influencers?', 'Yes. We recommend creators based on audience fit and campaign goals, not only follower counts.'),
          ('Can you produce the content for influencers?', 'Yes. We can produce professional photos and videos with creators for use on their channels and yours.')],
    related=['social-media-marketing', 'promotional-videos', 'performance-marketing'],
)

# ---------------------------------------------------------------------------
# EVENTS
# ---------------------------------------------------------------------------
S['event-management'] = dict(
    div='events', kind='division', seo='Event Management & Event Production in Delhi NCR | Playback Media & Events Hub',
    meta='Event management and production for medical conferences, corporate events, exhibitions, seminars and workshops in Delhi NCR.',
    eyebrow='Event & Conference Management', h1='Professional Event Management &amp; Event Production in <span class="serif grad-text">Delhi NCR</span>',
    sub='From Creative Concepts to Professional Execution.',
    image='assets/img/milestones.webp',
    intro=['Events connect people, businesses, ideas, and opportunities.',
           'Playback Media &amp; Events Hub provides event management and production solutions for medical conferences, corporate events, scientific meetings, seminars, workshops, exhibitions, and business gatherings.',
           'Our background in media production and audiovisual services enables us to combine technical coordination, creative presentation, event branding, photography, and videography.',
           'We work with clients to understand the event objectives, program, venue, production requirements, and budget before developing a suitable proposal.'],
    cards=[('bi-buildings-fill', 'Corporate Events', 'Conferences, product launches, awards, annual meetings, business summits and professional gatherings.', 'corporate-events/', 'Explore Corporate Events'),
           ('bi-heart-pulse-fill', 'Medical Conferences &amp; CMEs', 'Audiovisual systems, scientific presentation support, branding, stalls and media for healthcare events.', 'medical-conference-management/', 'Explore Medical Conferences'),
           ('bi-display', 'AV &amp; Stage Production', 'LED walls, sound, microphones, projection, stage platforms, lighting and technical operators.', 'audio-visual-production/', 'Explore AV Production'),
           ('bi-shop', 'Exhibition Stalls &amp; Branding', 'Sponsor stalls, booths, branded counters, backdrops, signage, printing and delegate kits.', 'exhibition-stalls-branding/', 'Explore Exhibitions'),
           ('bi-broadcast-pin', 'Live Streaming &amp; Webinars', 'Multi-camera streaming, webinar production, hybrid conferences and lecture recording.', 'live-streaming/', 'Explore Live Streaming')],
    card_images=['assets/img/work/commvault-partner-summit/01-sm.webp', 'assets/img/work/apccsm-medical-workshop/01-sm.webp', 'assets/img/stage-spiral.webp',
                 'assets/img/work/exhibition-stalls-sponsor-booths/01-sm.webp', 'assets/img/work/azad-bhawan-seminar/04-sm.webp'],
    gallery=imgs_from('commvault-partner-summit', 'tata-time-to-do-big-forum', 'exhibition-stalls-sponsor-booths', 'hcl-domino-jams', 'tata-milestones-2023', 'apccsm-medical-workshop', per=2),
    process=EVENT_PROCESS, process_title='Production <span class="serif grad-text">Workflow.</span>',
    cta=('Request an Event Proposal', 'Corporate Events'),
    faqs=[('Do you manage the complete event or individual services?', 'Both. We can manage the complete production or provide specific services such as AV, stalls, branding, photography or streaming.'),
          ('How early should we contact you?', 'For conferences and large corporate events, four to eight weeks ahead is ideal, although we can support shorter timelines depending on scope.'),
          ('Do you work outside Delhi NCR?', 'Yes. We serve Delhi NCR and North India, and can support events in other locations depending on requirements.')],
    related=['photography', 'video-production', 'live-streaming'],
)

S['corporate-events'] = dict(
    div='events', seo='Corporate Event Management Company in Delhi NCR | Playback',
    meta='Corporate conferences, product launches, AGMs, town halls, awards and dealer meets: planning, AV, branding and media in Delhi NCR.',
    h1='Corporate Event Management Company in <span class="serif grad-text">Delhi NCR</span>', sub='Corporate Events Designed With Purpose. Produced With Precision.',
    image='assets/img/work/commvault-partner-summit/01.webp',
    intro=['Corporate events provide businesses with an opportunity to communicate, engage, recognize achievements, launch initiatives, and strengthen professional relationships.',
           'Playback provides corporate event management and production services combining audiovisual technology, stage arrangements, event branding, technical coordination, and professional media coverage.',
           'Our solutions can support corporate conferences, product launches, awards, annual meetings, business summits, exhibitions, and professional gatherings.'],
    cards=[('bi-clipboard-check-fill', 'Planning &amp; Production Coordination', 'Event production planning, technical discussions, schedules, venue-related coordination, and on-site technical support.'),
           ('bi-display', 'AV &amp; Stage Production', 'LED walls, PA systems, microphones, projectors, stage platforms, lighting, presentation support, and switching systems.'),
           ('bi-palette-fill', 'Corporate Branding', 'Stage backdrops, sponsor displays, digital branding, signage, banners, standees, and registration areas.'),
           ('bi-shop', 'Exhibitions &amp; Displays', 'Branded booths, sponsor stalls, exhibition displays, counters, and related production elements.'),
           ('bi-trophy-fill', 'Merchandise &amp; Printing', 'Awards, trophies, delegate materials, corporate gifts, brochures, badges, and lanyards.'),
           ('bi-camera-fill', 'Photography &amp; Videography', 'Professional event coverage, interviews, video highlights, recordings, and promotional media.')],
    categories=['Corporate Conferences &amp; Summits', 'Product Launches', 'Annual General Meetings', 'Town Halls', 'Dealer &amp; Partner Meetings',
                'Awards &amp; Recognition Programs', 'Corporate Celebrations', 'Exhibitions &amp; Trade Events'],
    why=['Integrated creative and technical services', 'Established media production experience', 'Customized event solutions',
         'Professional audiovisual coordination', 'Photography and video production capabilities', 'Support for branding and exhibition requirements'],
    gallery=imgs_from('commvault-partner-summit', 'tata-time-to-do-big-forum', 'hcl-domino-jams', 'tata-milestones-2023', 'nse-emerge-listing', 'intogain-razzmatazz', per=2),
    showreel=('See Our Corporate Productions in <span class="serif grad-text">Action.</span>', ['qcSjiX7-V8s', 'WW15w_4Z2FI', 'XoU_KWkLU2I']),
    process=EVENT_PROCESS, process_title='Production <span class="serif grad-text">Workflow.</span>',
    cta=('Request a Corporate Event Proposal', 'Corporate Events'),
    cta_title="Let's Create a Corporate Event Worth <span class=\"serif grad-text\">Remembering.</span>",
    faqs=[('Can you handle both the event production and media coverage?', 'Yes. We coordinate AV, stage and branding, and our photography and video teams cover the event, so everything is managed by one partner.'),
          ('Do you provide branded merchandise and printing?', 'Yes. We arrange awards, trophies, delegate kits, badges, lanyards, brochures and corporate gifts.')],
    related=['audio-visual-production', 'exhibition-stalls-branding', 'event-photography'],
)

S['medical-conference-management'] = dict(
    div='events', seo='Medical Conference & CME Management in Delhi NCR | Playback',
    meta='Medical conference AV, scientific session support, LED walls, e-podiums, exhibition stalls, sponsor branding and live streaming for CMEs.',
    h1='Medical Conference &amp; CME Management in <span class="serif grad-text">Delhi NCR</span>', sub='Professional Production for Healthcare Organizations.',
    image='assets/img/work/apccsm-medical-workshop/01.webp', chip=('bi-heart-pulse-fill', '50+', 'medical conference assignments'),
    intro=['Medical conferences require organized production, technical precision, clear presentations, and effective coordination.',
           'Playback supports medical associations, hospitals, healthcare organizations, and conference organizers with audiovisual systems, scientific presentation support, conference branding, exhibition stalls, photography, videography, and production coordination.',
           'Our healthcare conference experience helps us understand speaker presentations, multi-hall scientific programs, panel discussions, technical arrangements, and sponsor visibility requirements.'],
    included=['Medical Conference AV', 'Scientific Session Technical Support', 'Main Hall &amp; Workshop Hall Production', 'LED Walls &amp; Projection', 'E-Podiums &amp; Speaker Audio',
              'Exhibition Stalls', 'Sponsor Branding', 'Photography &amp; Videography', 'Live Streaming', 'Conference Recording', 'Highlight &amp; Post-Event Videos'],
    included_title='Conference <span class="serif grad-text">Services.</span>', included_cols=2,
    cards=[('bi-easel2-fill', 'Scientific sessions', 'Presentation control, speaker timers and confidence monitors in every hall.'),
           ('bi-collection-fill', 'Multi-hall programmes', 'Main hall and workshop halls produced and coordinated together.'),
           ('bi-award-fill', 'Sponsor visibility', 'Stalls, branding and recognition that sponsors value.')],
    featured_projects=['iasrm-world-congress-2026', 'pelvic-floor-summit-2026', 'apccsm-medical-workshop', 'exhibition-stalls-sponsor-booths'],
    gallery=imgs_from('apccsm-medical-workshop', 'ageing-foundation-conference', 'orange-klinic-healthcare-workshop', 'exhibition-stalls-sponsor-booths', per=3),
    videos=['3YBUpojm99g', 'ONGK-4ZsNBg', 'Ar5lBCxAHYg'],
    process=EVENT_PROCESS, cta=('Request a Conference Proposal', 'Medical Conferences'),
    cta_title='Plan Your Medical Conference With <span class="serif grad-text">Playback.</span>',
    faqs=[('Can you manage AV across multiple halls?', 'Yes. We plan and operate AV for main halls, parallel sessions and workshop halls, with technical operators in each.'),
          ('Do you provide e-podiums and speaker timers?', 'Yes. E-podiums, confidence monitors, timers and presentation control are part of our scientific session support.'),
          ('Can you live stream and record the sessions?', 'Yes. We provide multi-camera streaming, session recording and post-event highlight videos.'),
          ('Do you build sponsor stalls?', 'Yes. We design and fabricate sponsor stalls, registration counters and conference branding.')],
    related=['audio-visual-production', 'exhibition-stalls-branding', 'live-streaming'],
)

S['audio-visual-production'] = dict(
    div='events', seo='Audio-Visual & Stage Production Services in Delhi NCR | Playback',
    meta='LED video walls, sound systems, microphones, stage platforms, lighting, e-podiums, projectors and technical operators for events.',
    h1='Audio-Visual &amp; Stage <span class="serif grad-text">Production</span>', sub='Reliable technology so presenters are seen and heard clearly.',
    image='assets/img/stage-spiral.webp',
    intro=['Professional audiovisual systems help presenters communicate clearly and create a reliable event experience.',
           'Playback coordinates audiovisual and stage production arrangements for conferences, corporate events, exhibitions, workshops, and professional meetings.'],
    included=['LED Video Walls', 'Professional Sound Systems', 'Handheld &amp; Lapel Microphones', 'Stage Platforms &amp; Risers', 'Event Lighting', 'E-Podiums', 'Projectors',
              'Preview &amp; Confidence Monitors', 'Video Switching', 'Recording Systems', 'Technical Operators'],
    included_title='AV <span class="serif grad-text">Services.</span>', included_cols=2,
    cards=[('bi-display', 'LED &amp; projection', 'Bright, clear visuals sized to your venue and audience.'),
           ('bi-speaker-fill', 'Sound', 'Clear speech and music with professional mixing.'),
           ('bi-person-gear', 'Technical crew', 'Experienced operators running every session.')],
    gallery=imgs_from('commvault-partner-summit', 'tata-milestones-2023', 'stage-performance-shoot', 'hcl-domino-jams', per=3),
    process=EVENT_PROCESS, cta=('Request an AV Production Quote', 'Audio-Visual Production'),
    faqs=[('Do you provide technicians to run the equipment?', 'Yes. Our technical operators set up, test and run the AV for the duration of your event.'),
          ('Can you do a technical rehearsal before the event?', 'Yes. We schedule setup and rehearsal time to test presentations, videos and microphones before guests arrive.')],
    related=['corporate-events', 'medical-conference-management', 'live-streaming'],
)

S['exhibition-stalls-branding'] = dict(
    div='events', seo='Exhibition Stall Design, Event Branding & Printing in Delhi NCR | Playback',
    meta='Sponsor stalls, exhibition booths, branded counters, backdrops, signage, standees, delegate kits, badges, printing, gifting and trophies.',
    h1='Exhibition Stall, Event Branding &amp; <span class="serif grad-text">Printing Solutions</span>', sub='Visibility for sponsors. A professional welcome for delegates.',
    image='assets/img/work/exhibition-stalls-sponsor-booths/01.webp',
    intro=['Professional exhibition and event branding creates visibility and supports meaningful interaction between sponsors, exhibitors, and delegates.',
           'Playback coordinates booth production, event signage, sponsor displays, promotional printing, branded counters, and related exhibition services.'],
    included=['Sponsor Stalls', 'Exhibition Booths', 'Branded Counters', 'Stage Backdrops', 'Event Signage', 'Banners &amp; Standees', 'Delegate Kits', 'Badges &amp; Lanyards',
              'Brochures &amp; Printing', 'Corporate Gifting', 'Awards &amp; Trophies'],
    included_title='Branding <span class="serif grad-text">Services.</span>', included_cols=2,
    cards=[('bi-shop', 'Stalls &amp; booths', 'Shell schemes and custom stalls designed for interaction.'),
           ('bi-flag-fill', 'Signage &amp; backdrops', 'Consistent branding from entrance to stage.'),
           ('bi-gift-fill', 'Delegate materials', 'Kits, badges, lanyards, gifts and trophies.')],
    gallery=project_images(PROJECT_BY_SLUG['exhibition-stalls-sponsor-booths']) + imgs_from('tata-time-to-do-big-forum', per=3),
    process=EVENT_PROCESS, cta=('Request an Exhibition &amp; Branding Proposal', 'Exhibition & Branding'),
    faqs=[('Can you design the stall artwork too?', 'Yes. Our designers create stall graphics and branding based on your brand guidelines.'),
          ('Do you provide printing and delegate kits separately?', 'Yes. Printing, kits, badges, lanyards, gifts and trophies can be ordered as stand-alone services.')],
    related=['corporate-events', 'medical-conference-management', 'event-photography'],
)

S['live-streaming'] = dict(
    div='events', seo='Live Streaming & Webinar Production in Delhi NCR | Playback',
    meta='Professional live streaming, webinar production, multi-camera recording, hybrid conferences and lecture recording in Delhi NCR.',
    h1='Professional Live Streaming &amp; <span class="serif grad-text">Webinar Production</span>', sub='Your event, reaching audiences wherever they are.',
    image='assets/img/work/azad-bhawan-seminar/04.webp',
    intro=['Playback provides live streaming, webinar production, multi-camera recording, and online event support for educational, corporate, and healthcare-related projects.',
           'Our services can include camera production, audio recording, presentation integration, live switching, webinar support, editing, and final content delivery.'],
    included=['Medical Webinars', 'Corporate Webinars', 'Online Courses', 'Hybrid Conferences', 'Multi-Camera Streaming', 'Lecture Recording', 'Presentation Integration', 'Webinar Video Editing'],
    included_title='Streaming <span class="serif grad-text">Services.</span>', included_cols=2,
    cards=[('bi-camera-video-fill', 'Multi-camera', 'Professional cameras with live switching between speakers and slides.'),
           ('bi-broadcast-pin', 'Any platform', 'YouTube, Zoom, Facebook, LinkedIn or a private stream.'),
           ('bi-collection-play-fill', 'Recordings', 'Edited session recordings delivered after the event.')],
    videos=['NIDHO0DOaKM', 'ONGK-4ZsNBg', 'WW15w_4Z2FI'],
    process=EVENT_PROCESS, cta=('Discuss Your Live Streaming Requirement', 'Live Streaming'),
    faqs=[('Which platforms can you stream to?', 'We stream to YouTube, Facebook, LinkedIn, Zoom and other platforms, or to a private link for registered audiences.'),
          ('What internet connection do you need?', 'We assess the venue connection in advance and can arrange backup connectivity where required.'),
          ('Can you record and edit the sessions afterwards?', 'Yes. We deliver recordings of every session and can edit them for on-demand viewing.')],
    related=['medical-conference-management', 'audio-visual-production', 'video-editing'],
)


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------
def _crumbs(slug):
    s = S[slug]
    d = DIV_BY_KEY[s['div']]
    title = NAME.get(slug, slug)
    if s.get('kind') == 'division':
        return [('Services', 'services/'), (d['name'], None)]
    return [('Services', 'services/'), (d['name'], d['slug'] + '/'), (title, None)]

def _media_mock(s):
    """Decorative digital mockup reused from the homepage card."""
    if s.get('browser'):
        return '''<div class="mockwrap reveal"><div class="svc-card__media mock-media" style="background:linear-gradient(135deg,#ecebf6,#fbe7e4)">
              <div class="lighthouse"><span>98</span><span>100</span></div>
              <div class="browser"><div class="browser__bar"><i></i><i></i><i></i><span>yourbrand.in</span></div>
                <div class="browser__view"><div class="browser__copy"><b>Your brand,<br>beautifully online.</b><i class="sk"></i><i class="sk"></i><em></em></div>
                <img src="~/assets/img/portrait-fashion.webp" alt="" loading="lazy" decoding="async"></div></div>
              <div class="code-chip"><span class="c">// launch day</span><br><span class="k">const</span> site = <span class="s">'live'</span>;<br>leads.<span class="k">grow</span>();</div>
            </div></div>'''
    return f'''<div class="mockwrap reveal"><div class="svc-card__media mock-media">
              <img src="~/{s['image']}" alt="" loading="lazy" decoding="async">
              {dash_html()}
            </div></div>'''

def dash_html():
    return '''<div class="dash">
                <div class="dash__head"><b>Campaign overview</b><span class="dash__live">Live</span></div>
                <svg viewBox="0 0 400 110" preserveAspectRatio="none" aria-hidden="true">
                  <defs>
                    <linearGradient id="dl" x1="0" x2="1"><stop offset="0" stop-color="#3c3090"/><stop offset=".5" stop-color="#6c60a8"/><stop offset="1" stop-color="#cc1824"/></linearGradient>
                    <linearGradient id="df" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c60a8" stop-opacity=".28"/><stop offset="1" stop-color="#6c60a8" stop-opacity="0"/></linearGradient>
                  </defs>
                  <path d="M0 95 C40 90 60 78 90 80 S140 60 170 62 S220 40 250 44 S310 22 340 20 S380 8 400 6 V110 H0Z" fill="url(#df)"/>
                  <path class="dash__line" pathLength="1" d="M0 95 C40 90 60 78 90 80 S140 60 170 62 S220 40 250 44 S310 22 340 20 S380 8 400 6" fill="none" stroke="url(#dl)" stroke-width="3" stroke-linecap="round"/>
                </svg>
                <div class="dash__chips"><span><i class="bi bi-search"></i> SEO</span><span><i class="bi bi-instagram"></i> Social</span><span><i class="bi bi-google"></i> Ads</span><span><i class="bi bi-person-check"></i> Leads</span></div>
              </div>'''

def _related(slugs):
    from data import PROJECTS  # noqa
    cards = []
    for r in slugs:
        rs = S.get(r)
        img = rs['image'] if rs else 'assets/img/hero-dance.webp'
        img = img.replace('.webp', '-sm.webp') if '/work/' in img and '-sm' not in img else img
        cards.append(img_card(img, NAME.get(r, r), rs['sub'] if rs else '', r + '/', 'Explore'))
    return f'''    <section class="section related">
      <div class="container-x">
        {shead('Related services', 'You may also <span class="serif grad-text">need.</span>')}
        <div class="cgrid cgrid--3">{''.join(cards)}</div>
      </div>
    </section>'''

def _project_cards(slugs):
    from pages import project_card
    return '<div class="pgrid pgrid--4">' + ''.join(project_card(PROJECT_BY_SLUG[s]) for s in slugs) + '</div>'

def render_service(slug):
    s = S[slug]
    d = DIV_BY_KEY[s['div']]
    is_div = s.get('kind') == 'division'
    eyebrow = s.get('eyebrow') or d['name']
    cta_label, form_service = s['cta']
    actions = btn(cta_label, '#enquire', 'grad', 'bi-arrow-down-right') + btn('View Our Work', 'portfolio/?category=' + {'photography': 'photography', 'video': 'video', 'digital': 'digital', 'events': 'events'}[s['div']], 'ghost', 'bi-grid-1x2-fill')
    hero = phero(eyebrow=eyebrow, title=s['h1'], sub=s['sub'], actions=actions, media=s['image'], crumbs=_crumbs(slug), chip=s.get('chip'))
    out = [hero]

    # Introduction
    intro_p = ''.join(f'<p class="reveal">{p}</p>' for p in s['intro'])
    side = ''
    if s.get('included') and not s.get('included_title'):
        side = f'<aside class="glass glance reveal"><h3>What&rsquo;s included</h3>{checklist(s["included"])}</aside>'
    elif s.get('mock') or s.get('browser'):
        side = _media_mock(s)
    else:
        facts = [('bi-geo-alt-fill', SITE['region'], 'Service area'), ('bi-people-fill', '1,000+', 'Clients served'), ('bi-camera-reels-fill', '15+ years', 'Industry experience')]
        side = '<aside class="glass glance reveal"><h3>At a glance</h3><ul class="glance__facts">' + ''.join(
            f'<li><span class="icon-tile xs"><i class="bi {i}"></i></span><div><b>{a}</b><small>{b}</small></div></li>' for i, a, b in facts) + '</ul>' + \
            f'<a href="#enquire" class="btn-x btn-grad mt-3">{cta_label} <span class="ico"><i class="bi bi-arrow-down-right"></i></span></a></aside>'
    out.append(f'''    <section class="section svc-intro">
      <div class="container-x">
        <div class="split split--intro">
          <div class="prose-lead">
            <span class="eyebrow reveal">{'Introduction' if is_div else 'Overview'}</span>
            {intro_p}
          </div>
          {side}
        </div>
      </div>
    </section>''')

    # Main services / features
    if is_div:
        imgs = s.get('card_images')
        if imgs:
            cards = ''.join(img_card(imgs[i], c[1], c[2], c[3], c[4] or 'Explore') for i, c in enumerate(s['cards']))
            grid = f'<div class="cgrid cgrid--3">{cards}</div>'
        else:
            cards = ''.join(icon_card(c[0], c[1], c[2], c[3], 'violet' if i % 3 == 1 else ('rose' if i % 3 == 2 else ''), c[4] or 'Learn more') for i, c in enumerate(s['cards']))
            grid = f'<div class="cgrid cgrid--3">{cards}</div>'
        out.append(f'''    <section class="section svc-main">
      <div class="container-x">
        {shead('Main services', 'Everything you need, <span class="serif grad-text">under one roof.</span>', 'Choose a single service or combine several. Each is delivered by specialists who work together when your project needs them.')}
        {grid}
      </div>
    </section>''')
    else:
        if s.get('included_title'):
            out.append(f'''    <section class="section svc-included">
      <div class="container-x">
        <div class="split">
          <div>{shead('What we provide', s['included_title'])}</div>
          <div class="glass glance reveal">{checklist(s['included'], s.get('included_cols', 1))}</div>
        </div>
      </div>
    </section>''')
        cards = ''.join(icon_card(c[0], c[1], c[2], None, ['', 'violet', 'rose'][i % 3]) for i, c in enumerate(s['cards']))
        cols = 3 if len(s['cards']) % 3 == 0 else 2
        title = 'How we <span class="serif grad-text">help.</span>' if len(s['cards']) <= 3 else 'Corporate event <span class="serif grad-text">services.</span>'
        out.append(f'''    <section class="section svc-main">
      <div class="container-x">
        {shead('Why it works', title)}
        <div class="cgrid cgrid--{cols}">{cards}</div>
      </div>
    </section>''')

    # Event categories + why
    if s.get('categories'):
        why = ''.join(f'<div class="glass why-item reveal"><span class="icon-tile sm {["", "rose", "violet"][i % 3]}"><i class="bi bi-check2-circle"></i></span><div><h4>{w}</h4></div></div>' for i, w in enumerate(s['why']))
        out.append(f'''    <section class="why">
      <div class="container-x">
        <div class="why__panel">
          <div class="ribbon ribbon--l" data-ribbon="side-l"></div>
          <div class="ribbon ribbon--r" data-ribbon="side-r"></div>
          <h2 class="why__title reveal">Corporate Event <span class="serif grad-text">Categories.</span></h2>
          <div class="catwrap reveal">{chips([c.replace('&amp;', '&') for c in s['categories']])}</div>
          <h3 class="why__sub reveal">Why Choose Playback?</h3>
          <div class="why6">{why}</div>
        </div>
      </div>
    </section>''')

    # Featured projects (medical)
    if s.get('featured_projects'):
        out.append(f'''    <section class="section">
      <div class="container-x">
        {shead('Featured projects', 'Recent conference <span class="serif grad-text">work.</span>')}
        {_project_cards(s['featured_projects'])}
      </div>
    </section>''')

    # Gallery
    if s.get('gallery'):
        out.append(f'''    <section class="section svc-gallery">
      <div class="container-x">
        {shead('Gallery', 'A look at our <span class="serif grad-text">work.</span>', 'Selected photographs from real Playback assignments. Tap any image to view it larger.')}
        {gallery(s['gallery'], NAME.get(slug, 'Playback') + ' photograph')}
      </div>
    </section>''')

    # Showreel / videos
    vids = s.get('videos')
    if s.get('showreel'):
        t, vids2 = s['showreel']
        out.append(f'''    <section class="section svc-videos">
      <div class="container-x">
        {shead('Showreel', t, 'Approved footage of conference stages, corporate events, LED installations, sponsor booths, technical production and event coverage.')}
        {vgrid(vids2)}
      </div>
    </section>''')
    elif vids:
        out.append(f'''    <section class="section svc-videos">
      <div class="container-x">
        {shead('Watch', 'Real productions, <span class="serif grad-text">real clients.</span>', 'Selected videos produced by Playback. Click to play.')}
        {vgrid(vids)}
        <div class="center mt-5 reveal">{btn('Watch Our Showreel', 'showreel/', 'ghost', 'bi-play-fill')}</div>
      </div>
    </section>''')

    # Process
    out.append(f'''    <section class="section process">
      <div class="container-x">
        {shead('How we work', s.get('process_title', 'Our <span class="serif grad-text">process.</span>'), 'A clear, collaborative process with one point of contact from the first conversation to final delivery.')}
        {steps(s['process'])}
      </div>
    </section>''')

    # FAQs
    if s.get('faqs'):
        out.append(f'''    <section class="section faqs">
      <div class="container-x">
        <div class="split split--faq">
          <div>{shead('FAQs', 'Questions, <span class="serif grad-text">answered.</span>', 'Can&rsquo;t find what you need? Call or WhatsApp us and we will be happy to help.')}</div>
          {faq(s['faqs'])}
        </div>
      </div>
    </section>''')

    # Related
    out.append(_related(s['related']))

    # CTA + form
    ctitle = s.get('cta_title') or f'{cta_label.split(" Your ")[0] if False else "Let&rsquo;s discuss your"} <span class="serif grad-text">{NAME.get(slug, "project").lower() if not is_div else "project."}</span>'
    if not s.get('cta_title'):
        ctitle = 'Have a project in mind? <span class="serif grad-text">Let&rsquo;s make it happen.</span>'
    out.append(cta_band(ctitle, 'Share a few details and our team will review your requirement and contact you with the next steps.',
                        btn('Get a Quote', 'get-a-quote/?service=' + d['key'], 'grad') + btn('Chat on WhatsApp', wa_link(f'Hi Playback, I am interested in {NAME.get(slug, "your services")}.'), 'ghost', 'bi-whatsapp', ext=True),
                        enquiry_form(form_service), eyebrow=cta_label, id_='enquire'))

    schema = [{
        '@context': 'https://schema.org', '@type': 'Service', 'name': NAME.get(slug, slug),
        'serviceType': NAME.get(slug, slug), 'areaServed': SITE['region'],
        'provider': {'@type': 'Organization', 'name': SITE['name'], 'url': SITE['url']},
        'description': s['meta'],
    }]
    if s.get('faqs'):
        schema.append(faq_schema(s['faqs']))
    return page(slug + '/', title=s['seo'], desc=s['meta'], body='\n'.join(out), active='services',
                crumbs=_crumbs(slug), schema=schema, og_image=s['image'].replace('-sm', ''))

def render_all():
    return [render_service(k) for k in S]
