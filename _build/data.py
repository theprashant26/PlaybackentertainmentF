"""Site-wide facts and content data for Playback Media & Events Hub.

Everything here comes from the Final Website Development Handover (v2.0, Oct 2026),
the Video Links document, the client's Drive photo library and the current site.
Edit content here, then run `python _build/build.py`.
"""

# Preview mode: while the design is reviewed on GitHub Pages, keep it out of search engines.
# Set to False for the live launch on www.playbackmedia.in (removes noindex and opens robots.txt).
PREVIEW = True

SITE = {
    'name': 'Playback Media & Events Hub',
    'short': 'Playback',
    'tagline': 'Create, Connect, and Grow.',
    'positioning': 'We Create. We Capture. We Connect.',
    'url': 'https://www.playbackmedia.in',
    'email': 'mail@playbackmedia.in',
    'phone1': '+91 9999104399', 'phone1_tel': '+919999104399', 'phone1_disp': '+91 99991 04399',
    'phone2': '+91 9555304101', 'phone2_tel': '+919555304101', 'phone2_disp': '+91 95553 04101',
    'whatsapp': '919999104399',
    'location': 'Ghaziabad, Delhi NCR, India',
    'region': 'Delhi NCR & North India',
    'registered': 2016,
    'digital_since': 2018,
    'socials': [
        ('Instagram', 'bi-instagram', 'https://www.instagram.com/playbackmediaofficial/'),
        ('YouTube', 'bi-youtube', 'https://www.youtube.com/@PlaybackEntertainmentandMedia'),
        ('LinkedIn', 'bi-linkedin', 'https://www.linkedin.com/company/playback-entertainment-and-media-pvt.-ltd/'),
        ('Facebook', 'bi-facebook', 'https://www.facebook.com/mediaplayback/'),
    ],
    'instagram_handle': '@playbackmediaofficial',
}

def wa_link(text='Hi Playback, I would like to discuss a project.'):
    from urllib.parse import quote
    return f"https://api.whatsapp.com/send?phone={SITE['whatsapp']}&text={quote(text)}"


# ---------------------------------------------------------------------------
# Service divisions (mega menu, footer, services hub)
# ---------------------------------------------------------------------------
DIVISIONS = [
    {
        'key': 'photography', 'name': 'Photography', 'menu': 'Photography', 'slug': 'photography',
        'all': 'All Photography Services', 'icon': 'bi-camera-fill', 'tile': 'rose',
        'blurb': 'Professional corporate, product, portfolio, event, healthcare, and commercial photography.',
        'image': 'assets/img/portrait-fashion.webp',
        'subs': [
            ('corporate-photography', 'Corporate Photography'),
            ('product-photography', 'Product & Commercial Photography'),
            ('portfolio-photography', 'Portfolio & Headshot Photography'),
            ('event-photography', 'Event & Conference Photography'),
        ],
    },
    {
        'key': 'video', 'name': 'Videography & Film Production', 'menu': 'Videography & Film Production', 'slug': 'video-production',
        'all': 'All Video Production Services', 'icon': 'bi-camera-reels-fill', 'tile': 'violet',
        'blurb': 'Corporate films, advertising videos, TV production, documentaries, interviews, promotional films, reels, and editing.',
        'image': 'assets/img/greenscreen.webp',
        'subs': [
            ('corporate-films', 'Corporate Films'),
            ('advertising-films', 'Advertising Films'),
            ('television-production', 'TV & Documentary Production'),
            ('video-editing', 'Video Editing & Post-Production'),
            ('promotional-videos', 'Interviews, Testimonials & Reels'),
        ],
    },
    {
        'key': 'digital', 'name': 'Digital Marketing', 'menu': 'Digital Marketing', 'slug': 'digital-marketing',
        'all': 'All Digital Marketing Services', 'icon': 'bi-graph-up-arrow', 'tile': 'violet',
        'blurb': 'Social media marketing, SEO, digital advertising, websites, healthcare marketing, and online content.',
        'image': 'assets/img/concert-crowd.webp',
        'subs': [
            ('social-media-marketing', 'Social Media Marketing'),
            ('seo-services', 'SEO & Local SEO'),
            ('performance-marketing', 'Google Ads & Meta Ads'),
            ('website-development', 'Website Development'),
            ('healthcare-digital-marketing', 'Healthcare Digital Marketing'),
            ('influencer-marketing', 'Influencer Marketing'),
        ],
    },
    {
        'key': 'events', 'name': 'Event Management', 'menu': 'Events & Production', 'slug': 'event-management',
        'all': 'All Event Management Services', 'icon': 'bi-stars', 'tile': '',
        'blurb': 'Corporate events, medical conferences, CME programs, AV production, stage setups, exhibitions, and event branding.',
        'image': 'assets/img/milestones.webp',
        'subs': [
            ('corporate-events', 'Corporate Events'),
            ('medical-conference-management', 'Medical Conferences & CMEs'),
            ('audio-visual-production', 'AV & Stage Production'),
            ('exhibition-stalls-branding', 'Exhibition Stalls & Branding'),
            ('live-streaming', 'Live Streaming & Webinars'),
        ],
    },
]

SUPPORTING = [
    ('bi-display', 'LED walls', 'is-grad'), ('bi-speaker-fill', 'Sound systems', ''), ('bi-easel-fill', 'Stage production', ''),
    ('bi-lightbulb-fill', 'Event lighting', 'is-outline'), ('bi-shop', 'Exhibition stalls', ''), ('bi-palette-fill', 'Event branding', 'is-outline'),
    ('bi-broadcast-pin', 'Live streaming', ''), ('bi-camera-video-fill', 'Webinar production', 'is-grad'),
    ('bi-printer-fill', 'Printing', ''), ('bi-gift-fill', 'Corporate gifting', ''), ('bi-trophy-fill', 'Awards & trophies', 'is-outline'),
    ('bi-person-badge-fill', 'Badges, lanyards & delegate kits', ''), ('bi-megaphone-fill', 'Influencer marketing', 'is-grad'),
    ('bi-magic', 'Motion graphics', ''), ('bi-mic-fill', 'Lecture recording', 'is-outline'), ('bi-whatsapp', 'WhatsApp & email marketing', ''),
]

# ---------------------------------------------------------------------------
# Clients & testimonials
# ---------------------------------------------------------------------------
CLIENTS = [
    ('flipkart', 'Flipkart'), ('fortis', 'Fortis C-DOC Hospital'), ('india-post', 'India Post'), ('grant-thornton', 'Grant Thornton'),
    ('esri-india', 'Esri India'), ('justdial', 'Justdial'), ('liugong', 'LiuGong India'), ('engineer-ply', 'Engineers Ply'),
    ('lifecare', 'LifeCare Centre'), ('aastha-healthcare', 'Aastha Healthcare'), ('anti-ageing', 'Anti-Ageing Foundation'),
    ('dsgmc', 'Delhi Sikh Gurdwara Management Committee'), ('rashi', 'Aao Baniye Gursikh Pyara'), ('engineering-college', 'I.T.S Engineering College'),
    ('aci', 'ACI'), ('caf', 'Charities Aid Foundation'), ('city-book-leaders', 'City Book Leaders'), ('bjp', 'BJP'),
]

TESTIMONIALS = [
    {'name': 'Mayank Kaushik', 'role': 'CEO & AMD', 'org': 'Ashirwad Group of Companies', 'photo': 'mayank-kaushik',
     'text': 'The team at Playback Media has been doing our work and they are absolutely flawless. They work well and we are totally satisfied with their work. They have done our corporate production for us, and they have also done our trainee production.'},
    {'name': 'Sardar Kulmohan Singh', 'role': 'Member', 'org': 'Delhi Sikh Gurdwara Management Committee', 'photo': 'sardar-kulmohan-singh',
     'text': 'In short, and in the best possible way, I want to say: you and your team are really a gem.'},
    {'name': 'Dr. Sharda Jain', 'role': 'Director & CEO', 'org': 'Life Care Hospital', 'photo': 'sharda-jain',
     'text': 'It was really awesome being served by the team. Hard-working, energetic, decent and well-mannered. I wish you all a better future, and hope we will have a long-term bond.'},
    {'name': 'K P Singh', 'role': 'Assistant Professor', 'org': 'ITS Management & IT Institute, Ghaziabad', 'photo': 'k-p-singh',
     'text': 'It was really a nice experience to work with Playback Media and the team involved in this entire video production. We didn’t find any trouble at any point whenever we needed changes or modifications.'},
    {'name': 'Dr. Sunil Kumar Pandey', 'role': 'Director-IT', 'org': 'ITS Management & IT Institute, Ghaziabad', 'photo': 'sunil-kumar-pandey',
     'text': 'We have taken services from Playback Media in making our corporate videos, for better socialisation, a better future and to increase our business opportunities.'},
    {'name': 'Pradeep Mittal', 'role': 'HR & Marketing', 'org': 'Fortis C-DOC Hospital, Chirag Enclave', 'photo': None,
     'text': 'Working with Playback Media and the team was really good. The team did their job well and in the best possible time.'},
]

VIDEO_TESTIMONIALS = [
    ('eL_tfSYYU1A', 'Dr. Harjinder Singh', 'Aao Baniye Gursikh Pyara'),
    ('VjsDp0_WojQ', 'Sardar Kulmohan Singh', 'Delhi Sikh Gurdwara Management Committee'),
    ('WbbhtxML6gs', 'Kuldip Singh', 'Client feedback'),
]

# ---------------------------------------------------------------------------
# Team (from the existing /meet-the-team/ page, copy from the handover)
# ---------------------------------------------------------------------------
TEAM = [
    {'slug': 'raushan-s-kumar', 'name': 'Raushan S Kumar', 'role': 'Founder & Director', 'group': 'lead',
     'bio': ['Raushan S Kumar leads Playback Media & Events Hub with extensive experience in photography, videography, television production, filmmaking, and business development.',
             'His journey began in media production, across corporate films, commercial shoots, television assignments, and professional photography. He later expanded the business into digital marketing and event management, particularly medical conferences and corporate events.',
             'His vision is to build Playback into an integrated creative, digital, and event production company known for professional execution and strong client relationships.']},
    {'slug': 'neha-singh', 'name': 'Neha Singh', 'role': 'Director', 'group': 'lead',
     'bio': ['Neha Singh contributes to the leadership and creative development of Playback Media & Events Hub.',
             'With a background in digital marketing and creative communication, she brings an understanding of branding, digital engagement, and organizational development.',
             "Her involvement supports the company's approach to creative thinking, communication, and long-term business growth."]},
    {'slug': 'aman-singh', 'name': 'Aman Singh', 'role': 'Manager & Photographer', 'group': 'production',
     'bio': ['Aman Singh contributes to photography assignments and production coordination at Playback Media & Events Hub.',
             'His work includes supporting project requirements, coordinating photography-related activities, and contributing to the delivery of professional visual content.']},
    {'slug': 'tarun-roy', 'name': 'Tarun Roy', 'role': 'Photographer', 'group': 'production',
     'bio': ["Tarun Roy contributes to Playback's photography assignments with a focus on visual storytelling, composition, and the documentation of important moments.",
             'His work supports photography requirements across professional and creative projects.']},
    {'slug': 'pritam-kumar', 'name': 'Pritam Kumar', 'role': 'Cinematographer & Videographer', 'group': 'production',
     'bio': ["Pritam Kumar contributes to the company's videography and cinematography assignments.",
             'His expertise includes camera operation, visual composition, and professional filming for corporate, commercial, and event-related productions.']},
    {'slug': 'qumar-khan', 'name': 'Qumar Khan', 'role': 'Cinematographer', 'group': 'production',
     'bio': ['Qumar Khan contributes to cinematography and professional visual production.',
             'His work includes camera composition, lighting awareness, and filming techniques that support professional video assignments.']},
    {'slug': 'anuj-chaturvedi', 'name': 'Anuj Chaturvedi', 'role': 'Digital Marketing Professional', 'group': 'digital',
     'bio': ['Anuj Chaturvedi brings experience in digital communication, online marketing, and creative problem-solving.',
             'He contributes to activities associated with digital projects, brand communication, and online marketing requirements.']},
    {'slug': 'priya-singh', 'name': 'Priya Singh', 'role': 'Social Media Manager', 'group': 'digital',
     'bio': ['Priya Singh contributes to social media management, digital content planning, brand communication, and online audience engagement.',
             'Her work supports digital content and communication requirements for professional and business clients.']},
]

# ---------------------------------------------------------------------------
# Videos (from the Video Links document; titles cleaned from YouTube)
# ---------------------------------------------------------------------------
VIDEO_CATS = [
    ('showreel', 'Playback Reels'), ('corporate', 'Corporate Films'), ('advertising', 'Advertising & Product'),
    ('tv', 'TV Production'), ('documentary', 'Documentaries'), ('events', 'Events & Conferences'),
    ('healthcare', 'Healthcare & Doctors'), ('education', 'Educational & Training'), ('motion', 'Motion Graphics'),
    ('social', 'Reels & Social'), ('profiles', 'Profiles & Interviews'), ('testimonials', 'Client Testimonials'),
    ('public', 'Public Affairs'),
]

VIDEOS = [
    # Playback reels
    ('dOcs6BJY2QE', 'Playback Showreel', ['showreel']),
    ('5lR20IvMiww', 'Playback Showreel 2021', ['showreel', 'events']),
    ('o4XkwdavgMY', 'Playback Highlight Reel', ['showreel']),
    ('EMIl3Sk-qGg', 'Playback Portfolio Reel', ['showreel']),
    ('qcSjiX7-V8s', 'Corporate Event & Conference Shoots', ['showreel', 'events']),
    ('jQX4BoyA5dA', 'Playback Video Brochure', ['showreel', 'motion']),
    # Corporate films
    ('L6uL6tO5wFY', 'Engineers Ply — Corporate Film', ['corporate']),
    ('ijX6yQVmzx4', 'Engineers Ply — Corporate Shoot', ['corporate']),
    ('pOEIfgYN9gg', 'VGLD — Corporate Film', ['corporate']),
    ('VvQF5U4B3zw', 'ITS Dental College, Muradnagar — Corporate Video (English)', ['corporate', 'education']),
    ('KRkjp2Hqy8U', 'ITS Dental College, Muradnagar — Corporate Video (Hindi)', ['corporate', 'education']),
    ('Bm9mO081wGQ', 'Shri Lal Bahadur Shastri Rashtriya Sanskrit Vidyapeetha — Corporate Video', ['corporate', 'education']),
    ('ObVF1SlWBa0', 'Lifecare IVF Hospital — Corporate Shoot', ['corporate', 'healthcare']),
    ('ZC__7UGjz0U', 'LiuGong India — Promotional Video', ['corporate', 'advertising']),
    ('N5aez0KxaQU', 'Berry Shirts — Company Profile', ['corporate']),
    ('Xw2yhG007mY', 'Manufacturing Unit — Promotional Video', ['corporate']),
    # Advertising & product
    ('1xodV0zYdSg', 'Study Khazana — Launch Video', ['advertising']),
    ('2tshq6aLFSg', 'Study Khazana — Promotional Film', ['advertising']),
    ('XKGHE9YKoiY', 'Woodage Sofa-cum-Bed — Advertisement', ['advertising']),
    ('WROTocdoMUs', 'Woodage — Promotional Video', ['advertising', 'corporate']),
    ('top-_Te4Qmk', 'Product Demonstration Video', ['advertising']),
    ('R77Nuh54I8M', 'Building Highlight — Real Estate Promo', ['advertising']),
    ('fBadLshype0', 'Chroma (Green Screen) Shoot — Yoga', ['advertising', 'social']),
    # TV production
    ('eKAqUBHCgos', 'Aao Baniye Gursikh Pyara — Season 27, Episode 12', ['tv']),
    ('8JFiPOTUG7A', 'Aao Baniye Gursikh Pyara — Season 26, Episode 7', ['tv']),
    ('xjLGlZwkn8Y', 'Aao Baniye Gursikh Pyara — Season 22, Episode 7', ['tv']),
    ('lJ1J2VMFae0', 'Aao Baniye Gursikh Pyara — Season 18, Episode 13', ['tv']),
    ('XfOrxmAFvT4', 'Aao Baniye Gursikh Pyara — Season 18, Episode 6', ['tv']),
    ('uMFihpW4xnE', 'Aao Baniye Gursikh Pyara — Season 16, Episode 11', ['tv']),
    ('IVtwVGCJJXE', 'Aao Baniye Gursikh Pyara — Season 11, Episode 10', ['tv']),
    ('p6J_J6dj1XE', 'Sikh Yodhe — Episode 1: Baba Banda Singh Bahadur', ['tv']),
    ('SOcLlJF221M', 'Sikh Yodhe — Episode 4: Baba Banda Singh Bahadur', ['tv']),
    # Documentaries
    ('z51spm2RWTw', 'Documentary on Bhai Vir Singh', ['documentary', 'tv']),
    ('1_dhhKhAAzs', 'Documentary Film on Pooja & Budhya', ['documentary']),
    ('3C_8eSLBT8g', 'Delhi The Dump — Documentary', ['documentary']),
    # Events & conferences
    ('3YBUpojm99g', 'IASRM Medical Conference Highlight — Jim Corbett', ['events', 'healthcare']),
    ('WW15w_4Z2FI', 'Conference Highlight Video', ['events']),
    ('oW6TOICFIbA', 'Flipkart — Dance Event Shoot', ['events']),
    ('XoU_KWkLU2I', 'Flipkart — Event Shoot', ['events']),
    ('NIDHO0DOaKM', 'Multi-Camera Live Editing — Dance Event', ['events']),
    ('GheD8nXvi0E', 'Musical Event Shoot', ['events']),
    ('qEPQBeXxoi0', 'Khelo India School Games', ['events']),
    ('wdmT-hcO0Vk', 'Ras Ras Banaras — Event Highlight', ['events']),
    ('rdLm2_g-EMs', 'Andaz-e-Agra — Event Highlight', ['events']),
    ('dN-I2Zeggrw', 'TL Power Performance — Event Film', ['events']),
    # Healthcare & doctors
    ('G85HUWhz9zw', 'YouTube Video for Dr. Garima Srivastav', ['healthcare', 'social']),
    ('XmEt5BASW74', 'Dr. Ragini Agarwal — Doctor Video', ['healthcare', 'social']),
    ('7FdQpF8KXbw', 'Vaginal Rejuvenation by HIFU — Patient Education', ['healthcare']),
    ('FmptUJXA0so', 'Anomaly Scan — Patient Education', ['healthcare']),
    ('pG0NPg5AuyY', 'Leg Cramps in Pregnancy', ['healthcare', 'social']),
    ('Wd6rnvPwNzk', 'Best Food for Healthy Weight Loss', ['healthcare', 'social']),
    ('MBmDHusiQ5g', "Understanding India's New Surrogacy Law", ['healthcare', 'education']),
    ('ctuFU9lKO6s', 'Anaemia QI Project — Facility Level', ['healthcare', 'education']),
    ('kWPETX0Rs8k', 'Demonstration of Brace Sutures', ['healthcare', 'education']),
    # Educational & training
    ('ONGK-4ZsNBg', 'Safdarjung Hospital — Educational Video', ['education', 'healthcare']),
    ('Ar5lBCxAHYg', 'Ventilator — Clinical Training Video', ['education', 'healthcare']),
    ('O_kybAUxtuM', 'Use of Monitors in HDU — Training Video', ['education', 'healthcare']),
    ('SU6GFLvVZI0', 'Medical Training Video — Dr. Siva', ['education', 'healthcare']),
    ('9nqxekBVL7Q', 'Training Video — Jyotsna Suri', ['education']),
    ('y5agKakj_4E', 'Educational Video for VGLD & 88 Learn', ['education']),
    ('WLY6PrlnXw8', 'Educational Video for EPG (Government Project)', ['education']),
    # Motion graphics
    ('4qPeOYxBEUQ', 'BitGreen — Promotional Video', ['motion', 'advertising']),
    ('STDvW4bSBqM', 'Motion Graphic Video (Hindi)', ['motion']),
    ('sKIqCyvVWTA', 'Mobile App Tutorial — Motion Graphics (English)', ['motion']),
    ('5TprRxt_ZpE', 'Profile Film with Motion Graphics', ['motion', 'profiles']),
    # Reels & social
    ('1l6g1eW-p3w', 'Reel Shoot for a Client — 1', ['social']),
    ('MU3q9bkSXnQ', 'Reel Shoot for a Client — 2', ['social']),
    ('1pIDhO-cPIU', 'Reel Shoot for a Client — 3', ['social']),
    ('b4MptEtHXBc', 'YouTube Video Promotion', ['social']),
    # Profiles, interviews, testimonials
    ('SMiSt3EFImM', 'Arun Maira — Video Profile', ['profiles']),
    ('kWEsJZ8CEuk', 'Testimonial Video Shoot', ['profiles']),
    ('_UOuYyotD2c', 'Video Resume Shoot', ['profiles']),
    ('O8eWLmn6yyo', 'Video Resume & Video Profile', ['profiles']),
    ('xc106L2Pj0w', 'India Post — Testimonial Video', ['profiles', 'testimonials']),
    ('eL_tfSYYU1A', 'Client Feedback — Dr. Harjinder Singh, Aao Baniye Gursikh Pyara', ['testimonials']),
    ('VjsDp0_WojQ', 'Client Feedback — Sardar Kulmohan Singh', ['testimonials']),
    ('WbbhtxML6gs', 'Client Feedback — Kuldip Singh', ['testimonials']),
    # Public affairs
    ('sF65eXM30aE', 'Shri Ganesh Singh, MP (Satna) — Interview', ['public', 'profiles']),
    ('W-L5Dc8_j3I', 'Election Campaign — Testimonial Video', ['public']),
]
VIDEO_BY_ID = {v[0]: v for v in VIDEOS}
SHOWREEL_ID = 'dOcs6BJY2QE'

def yt_thumb(vid, q='hqdefault'):
    return f'https://i.ytimg.com/vi/{vid}/{q}.jpg'


# ---------------------------------------------------------------------------
# Portfolio
# ---------------------------------------------------------------------------
PORTFOLIO_CATS = [
    ('all', 'All Projects'), ('photography', 'Photography'), ('video', 'Films & Video'),
    ('corporate-films', 'Corporate Films'), ('advertising-tv', 'Advertising & TV'), ('video-editing', 'Video Editing'),
    ('digital', 'Digital Marketing'), ('events', 'Events & Conferences'), ('medical', 'Medical Conferences'),
    ('corporate-events', 'Corporate Events'), ('av', 'AV & Exhibitions'),
]
CAT_LABEL = dict(PORTFOLIO_CATS)
HOME_FILTERS = [('all', 'All'), ('photography', 'Photography'), ('video', 'Video'), ('digital', 'Digital'), ('events', 'Events'), ('av', 'AV & Exhibitions')]

def _p(slug, title, cats, **kw):
    cats = list(cats)
    if any(c in cats for c in ('corporate-films', 'advertising-tv', 'video-editing')) and 'video' not in cats:
        cats.append('video')
    if any(c in cats for c in ('medical', 'corporate-events')) and 'events' not in cats:
        cats.append('events')
    d = {'slug': slug, 'title': title, 'cats': cats, 'client': None, 'location': None, 'year': None,
         'images': 0, 'videos': [], 'requirement': '', 'description': '', 'scope': [], 'services': [], 'excerpt': '',
         'cover': None, 'featured': False, 'note': None}
    d.update(kw)
    return d

PROJECTS = [
    _p('iasrm-world-congress-2026', 'IASRM World Congress 2026', ['medical', 'av', 'photography', 'video-editing'],
       location='New Delhi', year='2026', category_label='Medical Conference & Production', featured=True, type_icon='bi-heart-pulse-fill',
       excerpt='Conference audiovisual production, stage arrangements, LED displays, sound systems, technical support, photography and videography.',
       requirement='A multi-session international medical congress needing dependable conference production, clear scientific presentations and complete media coverage.',
       description='Playback supported the IASRM World Congress 2026 in New Delhi with conference audiovisual production, stage arrangements, LED displays, sound systems, technical support, photography, videography, and associated media production services.',
       scope=['Conference audiovisual production', 'Stage arrangements', 'LED displays', 'Sound systems', 'Technical support', 'Photography', 'Videography', 'Associated media production'],
       services=['medical-conference-management', 'audio-visual-production', 'event-photography', 'video-production'],
       videos=['3YBUpojm99g'], note='Photographs from the 2026 congress will be added once approved. The video shows an earlier IASRM conference highlight produced by Playback.'),
    _p('pelvic-floor-summit-2026', 'Pelvic Floor Summit 2026', ['medical', 'av', 'photography'],
       location='Gurugram', year='2026', category_label='Medical Conference, AV & Exhibition', featured=True, type_icon='bi-easel2-fill',
       excerpt='Audiovisual production, conference stage setup, sponsor booths, exhibition branding and photography.',
       requirement='A specialist medical summit requiring a professional conference stage, sponsor visibility and an organised exhibition area.',
       description='For the Pelvic Floor Summit 2026 in Gurugram, Playback provided audiovisual production, the conference stage setup, sponsor booths, exhibition branding, photography, and related event services.',
       scope=['Audiovisual production', 'Conference stage setup', 'Sponsor booths', 'Exhibition branding', 'Photography', 'Related event services'],
       services=['medical-conference-management', 'audio-visual-production', 'exhibition-stalls-branding', 'event-photography'],
       note='Photographs from the summit will be added once approved.'),
    _p('flipkart-seller-hub-night', 'Flipkart Seller Hub Celebration Night', ['corporate-events', 'photography', 'video-editing'],
       client='Flipkart', images=9, featured=True, videos=['oW6TOICFIbA', 'XoU_KWkLU2I'],
       excerpt='Stage performances, celebrity moments and a packed auditorium, captured in photographs and multi-camera film.',
       requirement='Cover a high-energy celebration evening with dance performances, celebrity appearances and audience interaction, for both internal communication and social media.',
       description='Our crew documented the Flipkart Seller Hub celebration from the first performance to the final applause. Stage photographers worked alongside a multi-camera video team so that every performance, speech and audience moment was available for highlight films and social content.',
       scope=['Stage & performance photography', 'Multi-camera event videography', 'Celebrity & audience moments', 'Highlight film editing'],
       services=['event-photography', 'video-production', 'corporate-events']),
    _p('nse-emerge-listing', 'NSE Emerge Listing Ceremony', ['corporate-events', 'photography'],
       client='Creative Graphics', year='2024', images=8, featured=True,
       excerpt='The bell-ringing, felicitations and team moments of a listing ceremony on NSE Emerge.',
       requirement="Document a milestone day for the company: its listing ceremony on NSE Emerge, including the traditional bell-ringing, speeches and felicitations.",
       description='Playback photographed the listing ceremony held on 9 April 2024, covering the ceremonial bell, leadership speeches, felicitations, guests and complete team portraits for investor communication and social media.',
       scope=['Ceremony photography', 'Leadership & speaker coverage', 'Felicitation & award moments', 'Group photographs', 'Edited photo delivery'],
       services=['event-photography', 'corporate-photography', 'corporate-events']),
    _p('tata-time-to-do-big-forum', 'Do Big Forum — #TimeToDoBig', ['corporate-events', 'av', 'photography'],
       client='Tata Tele Business Services', images=11, featured=True,
       excerpt='A branded business forum with welcome standees, product displays, conference seating and stage presentations.',
       requirement='A professional business forum with consistent brand presence, product display areas, delegate registration and full photographic coverage.',
       description='At the Do Big Forum, branding carried the #TimeToDoBig message from the welcome standees to the product display counters and the presentation stage. Playback covered the venue setup, speakers, delegates and branded displays.',
       scope=['Event branding & standees', 'Product display counters', 'Delegate registration area', 'Speaker & delegate photography'],
       services=['corporate-events', 'exhibition-stalls-branding', 'event-photography']),
    _p('hcl-domino-jams', 'HCL Software — Domino Jams', ['corporate-events', 'av', 'photography'],
       client='HCL Software', year='2022', images=8, featured=True,
       excerpt='A product community event with branded registration, keynote sessions and Q&A on stage.',
       requirement='Photograph a technology community event with international speakers, branded registration and interactive sessions.',
       description='For HCL Software’s Domino Jams, Playback captured the branded registration area, keynote presentations, panel and Q&A sessions, and networking moments between the product team and its community.',
       scope=['Keynote & speaker photography', 'Branded registration coverage', 'Q&A and panel sessions', 'Group & networking photographs'],
       services=['event-photography', 'corporate-events', 'audio-visual-production']),
    _p('commvault-partner-summit', 'Commvault Partner Summit — Forward Together', ['corporate-events', 'av', 'photography'],
       client='Commvault', images=8, featured=True,
       excerpt='A partner summit with LED stage visuals, branded registration, presentations and partner recognition.',
       requirement='Cover a partner summit combining presentations, partner recognition and an outdoor team moment under the "Forward Together" theme.',
       description='The summit brought partners together for presentations, panel conversations and recognition on an LED-lit stage. Playback documented the setup, sessions, awards and the large outdoor group photograph.',
       scope=['Stage & LED presentation coverage', 'Partner recognition photography', 'Panel discussions', 'Outdoor group photograph'],
       services=['corporate-events', 'audio-visual-production', 'event-photography']),
    _p('tata-milestones-2023', 'Milestones 2023 — Annual Team Meet', ['corporate-events', 'photography'],
       client='Tata', year='2023', images=8,
       excerpt='An annual team celebration with leadership addresses, live music, performances and an energised audience.',
       requirement='Capture the energy of a large annual team meet, from leadership addresses to live performances and audience participation.',
       description='Milestones 2023 celebrated a year of achievement under the theme “Let’s scale new heights of success together.” Our photographers covered the leadership addresses, live band, cultural performances and the audience’s involvement throughout the day.',
       scope=['Leadership & stage photography', 'Live music & performances', 'Audience & candid coverage', 'Team photographs'],
       services=['corporate-events', 'event-photography']),
    _p('cloud-service-providers-symposium', 'Cloud Service Providers Symposium', ['corporate-events', 'photography'],
       images=7,
       excerpt='A boutique technology symposium at a heritage venue: panels, speakers, partners and the group photograph.',
       requirement='Document an invitation-only technology symposium with panel discussions, partner presentations and the venue experience.',
       description='Held at a heritage hotel, the symposium combined a branded stage, panel discussions and networking. Playback captured the venue, the speakers and the complete delegate group.',
       scope=['Venue & setup photography', 'Speaker and panel coverage', 'Delegate group photograph', 'Edited photo delivery'],
       services=['event-photography', 'corporate-events']),
    _p('apccsm-medical-workshop', 'APCCSM Comprehensive Workshop', ['medical', 'photography'],
       client='APCCSM', images=8, featured=True,
       excerpt='A hands-on medical training workshop with live demonstrations, faculty sessions and certificate presentations.',
       requirement='Photograph a hands-on medical training workshop, covering faculty lectures, live demonstrations and certificate presentations.',
       description='This workshop combined faculty lectures with practical demonstrations using training mannequins and equipment. Playback documented the teaching sessions, hands-on stations, faculty and delegates, and the certificate ceremony.',
       scope=['Faculty & lecture photography', 'Hands-on demonstration coverage', 'Certificate presentations', 'Delegate & faculty group photographs'],
       services=['medical-conference-management', 'event-photography']),
    _p('ageing-foundation-conference', 'Anti-Ageing Foundation Conference', ['medical', 'photography'],
       client='Anti-Ageing Foundation (India)', images=6,
       excerpt='A medical conference with expert talks, panel discussions and award presentations.',
       requirement='Cover a scientific conference with multiple speakers, panel discussions and award presentations.',
       description='Playback photographed the conference sessions, speakers, delegate interactions and felicitations, delivering a complete visual record for the foundation’s communication.',
       scope=['Speaker & session photography', 'Panel discussions', 'Awards & felicitations', 'Delegate coverage'],
       services=['medical-conference-management', 'event-photography']),
    _p('orange-klinic-healthcare-workshop', 'Healthcare Workshop & Faculty Coverage', ['medical', 'photography'],
       client='Orange Klinic', images=8,
       excerpt='Faculty talks, live sessions, sponsor displays and team portraits from a healthcare workshop.',
       requirement='Professional coverage of a healthcare training workshop, from faculty talks and live sessions to sponsor displays and team photographs.',
       description='Our photographers covered faculty presentations, interactive sessions, sponsor displays and the complete participant group, giving the organisers images for reporting, social media and future promotion.',
       scope=['Faculty presentations', 'Interactive sessions', 'Sponsor display coverage', 'Group photographs'],
       services=['medical-conference-management', 'event-photography', 'healthcare-digital-marketing']),
    _p('india-post-postal-congress', 'India Post — Postal Congress Coverage', ['corporate-events', 'photography', 'corporate-films'],
       client='India Post', year='2013', location='New Delhi', images=4, videos=['xc106L2Pj0w'],
       excerpt='Photography at the XI Asian-Pacific Postal Union Congress and a testimonial video for India Post.',
       requirement='Professional photography for international postal events and a testimonial video for India Post.',
       description='Playback photographed the XI Asian-Pacific Postal Union Congress (3–7 September 2013), along with official portraits and Universal Postal Union delegation moments, and produced a testimonial video for India Post.',
       scope=['Plenary & delegate photography', 'Official portraits', 'Delegation group photographs', 'Testimonial video production'],
       services=['event-photography', 'corporate-photography', 'promotional-videos']),
    _p('azad-bhawan-seminar', 'Programme at Azad Bhawan, New Delhi', ['corporate-events', 'photography', 'video-editing'],
       location='New Delhi', images=8,
       excerpt='Auditorium coverage with a full house, stage sessions, video recording and group photographs.',
       requirement='Photograph and record an auditorium programme with stage sessions and a full audience.',
       description='Playback covered the programme at Azad Bhawan with photography and video recording, documenting the stage, the audience and the participants’ group photographs.',
       scope=['Auditorium photography', 'Video recording', 'Stage & speaker coverage', 'Group photographs'],
       services=['event-photography', 'video-production']),
    _p('intogain-razzmatazz', 'Intogain International Razzmatazz', ['corporate-events', 'photography'],
       client='Intogain', year='2018', images=9,
       excerpt='An annual corporate celebration with hosted segments, awards and a red-carpet atmosphere.',
       requirement='Cover a corporate annual celebration with hosted segments, awards and team moments.',
       description='Playback photographed the hosts, award presentations, performances and team celebrations at Intogain’s International Razzmatazz, followed by an outdoor team photograph.',
       scope=['Host & stage photography', 'Awards coverage', 'Party & candid moments', 'Team photographs'],
       services=['corporate-events', 'event-photography']),
    _p('northern-india-polo-championship', 'Northern India Polo Championship 2017', ['photography', 'corporate-events'],
       year='2017', images=9,
       excerpt='Match action and premium hospitality at the BT Business Lounge.',
       requirement='Photograph match action and the premium hospitality lounge at a polo championship.',
       description='At the Northern India Polo Championship 2017, Playback photographed the matches, guests and the BT Business Lounge experience, combining sports action with hospitality coverage.',
       scope=['Sports action photography', 'Hospitality lounge coverage', 'Guest & VIP photographs', 'Brand presence documentation'],
       services=['event-photography', 'corporate-photography']),
    _p('exhibition-stalls-sponsor-booths', 'Exhibition Stalls & Sponsor Booths', ['av', 'medical'],
       images=9, featured=True,
       excerpt='Branded sponsor stalls, registration counters and exhibition areas for medical conferences and expos.',
       requirement='Design and build branded booths and registration areas for sponsors at conferences and expos.',
       description='A selection of the sponsor stalls, registration counters and exhibition displays produced and photographed by Playback for medical conferences and trade events, built to give each exhibitor clear visibility and a professional space to meet delegates.',
       scope=['Sponsor stall fabrication', 'Registration counters', 'Branded displays & signage', 'Exhibition photography'],
       services=['exhibition-stalls-branding', 'medical-conference-management']),
    _p('product-commercial-photography', 'Product & Commercial Photography', ['photography', 'advertising-tv'],
       images=9, featured=True,
       excerpt='Catalogue, e-commerce and advertising images for furniture, food, industrial equipment and more.',
       requirement='Clean, accurate product images for catalogues, websites, e-commerce listings and advertising.',
       description='From construction equipment and industrial chillers to furniture, packaged foods and lifestyle setups, Playback produces product images that present each item clearly and attractively for its intended platform.',
       scope=['Studio product photography', 'Lifestyle product setups', 'Industrial & equipment photography', 'Retouching & e-commerce delivery'],
       services=['product-photography', 'advertising-films']),
    _p('first-birthday-shoot', 'First Birthday Celebration', ['photography'],
       images=8,
       excerpt='Portraits, family moments and the celebration, captured with warmth.',
       requirement='Capture a child’s first birthday with styled portraits, family moments and the celebration.',
       description='A relaxed portrait session followed by complete coverage of the birthday celebration, from styled portraits and family photographs to the décor and cake cutting.',
       scope=['Styled portraits', 'Family photographs', 'Décor & celebration coverage', 'Edited album selection'],
       services=['portfolio-photography']),
    _p('anniversary-celebration', 'Anniversary Celebration', ['photography'],
       images=6,
       excerpt='Family portraits, guests and the joy of a milestone anniversary.',
       requirement='Photograph a family anniversary celebration with portraits, guests and candid moments.',
       description='Playback photographed the couple, family members, guests and the evening’s celebrations, producing a warm visual record of the occasion.',
       scope=['Portraits', 'Family & guest photographs', 'Candid celebration moments'],
       services=['portfolio-photography', 'event-photography']),
    _p('stage-performance-shoot', 'Stage Performance & Dance Shoot', ['photography', 'corporate-events'],
       images=7,
       excerpt='Dramatic stage lighting, choreography and solo performances, frozen at their peak.',
       requirement='Photograph live stage performances under complex concert lighting.',
       description='Shooting under LED walls, moving heads and haze, our photographers captured ensemble choreography and solo performances at their most expressive moments.',
       scope=['Performance photography', 'Low-light & stage lighting expertise', 'Ensemble and solo coverage'],
       services=['event-photography']),
    _p('studio-portrait-interior-shoots', 'Studio, Portrait & Interior Shoots', ['photography'],
       images=7,
       excerpt='Green-screen corporate portraits, personal portraits and architectural interior photography.',
       requirement='Professional studio portraits on green screen, personal portraits and interior photography for a property.',
       description='This collection brings together green-screen corporate portraits for compositing, personal portraits and evening interior photography that shows the spaces, lighting and finishes of a property.',
       scope=['Green-screen portraits', 'Personal portraits', 'Interior & architectural photography'],
       services=['corporate-photography', 'portfolio-photography']),
    # Video-led projects
    _p('aao-baniye-gursikh-pyara', 'Aao Baniye Gursikh Pyara — TV Quiz Show', ['advertising-tv'],
       client='Aao Baniye Gursikh Pyara (Gurmat Quiz)', featured=True,
       videos=['eKAqUBHCgos', '8JFiPOTUG7A', 'xjLGlZwkn8Y', 'lJ1J2VMFae0', 'IVtwVGCJJXE', 'p6J_J6dj1XE', 'SOcLlJF221M', 'eL_tfSYYU1A'],
       excerpt='A long-running Punjabi television quiz show: 500+ episodes of production and direction experience.',
       requirement='Studio-based television production for a long-running Punjabi quiz show and its special series.',
       description='Playback’s leadership has directed more than 500 episodes of the television quiz show Aao Baniye Gursikh Pyara, along with special series such as Sikh Yodhe. The work covers multi-camera studio production, direction, post-production and episode delivery.',
       scope=['Multi-camera studio production', 'Direction', 'Post-production & editing', 'Special series production'],
       services=['television-production', 'video-editing']),
    _p('engineers-ply-corporate-film', 'Engineers Ply — Corporate Film', ['corporate-films'],
       client='Engineers Ply', videos=['L6uL6tO5wFY', 'ijX6yQVmzx4'],
       excerpt='A corporate film and shoot presenting the company, its manufacturing and its products.',
       requirement='A corporate film introducing the company, its manufacturing capability and product range.',
       description='Playback filmed the facility, processes and people behind Engineers Ply and edited a corporate film for business presentations, the website and social media.',
       scope=['Corporate film production', 'Facility & process filming', 'Editing & graphics'], services=['corporate-films']),
    _p('its-dental-college-corporate-video', 'ITS Dental College — Corporate Video', ['corporate-films'],
       client='ITS Dental College, Muradnagar', videos=['VvQF5U4B3zw', 'KRkjp2Hqy8U'],
       excerpt='An institutional film produced in English and Hindi versions.',
       requirement='An institutional corporate video in English and Hindi to present the college, its facilities and academic environment.',
       description='The film presents the campus, clinical facilities, teaching environment and student life, delivered in two language versions for wider reach.',
       scope=['Institutional film', 'Campus & facility filming', 'English and Hindi versions'], services=['corporate-films']),
    _p('lifecare-ivf-corporate-film', 'Lifecare IVF Hospital — Corporate Shoot', ['corporate-films'],
       client='Lifecare IVF Hospital', videos=['ObVF1SlWBa0'],
       excerpt='A healthcare corporate shoot presenting the hospital, its team and its patient care.',
       requirement='A healthcare corporate video presenting the hospital’s facilities, team and approach to patient care.',
       description='Playback produced a corporate shoot for Lifecare IVF Hospital, filming the facilities, specialists and patient-care environment with the sensitivity healthcare settings require.',
       scope=['Healthcare corporate film', 'Facility filming', 'Doctor interviews'], services=['corporate-films', 'healthcare-digital-marketing']),
    _p('woodage-advertising-film', 'Woodage — Advertising Film & Product Shoot', ['advertising-tv', 'photography'],
       client='Woodage', videos=['XKGHE9YKoiY', 'WROTocdoMUs'],
       excerpt='An advertisement for the Woodage sofa-cum-bed, with promotional video and product photography.',
       requirement='An advertising film and promotional video demonstrating a convertible sofa-cum-bed, supported by product photography.',
       description='Playback produced a product advertisement and a promotional video for Woodage, demonstrating the sofa-cum-bed’s design and function, together with studio product photographs.',
       scope=['Advertising film', 'Promotional video', 'Product demonstration', 'Product photography'], services=['advertising-films', 'product-photography'],
       gallery_from=('product-commercial-photography', [2, 3])),
    _p('liugong-india-promotional-video', 'LiuGong India — Promotional Video', ['corporate-films', 'advertising-tv'],
       client='LiuGong India', videos=['ZC__7UGjz0U'],
       excerpt='A promotional video for a construction equipment manufacturer.',
       requirement='A promotional video presenting the company and its construction equipment.',
       description='Playback produced a promotional video for LiuGong India showcasing its machinery and brand for business and digital communication.',
       scope=['Promotional film', 'Equipment filming', 'Editing'], services=['corporate-films', 'advertising-films']),
    _p('vgld-corporate-educational-films', 'VGLD — Corporate & Educational Films', ['corporate-films'],
       client='VGLD', videos=['pOEIfgYN9gg', 'y5agKakj_4E'],
       excerpt='A corporate film and an educational video produced for VGLD and 88 Learn.',
       requirement='A corporate film plus educational video content for an online learning platform.',
       description='Playback produced VGLD’s corporate film and educational video content for VGLD and 88 Learn, combining presenter-led filming with clear, structured editing.',
       scope=['Corporate film', 'Educational video', 'Editing & graphics'], services=['corporate-films', 'video-production']),
    _p('study-khazana-launch-films', 'Study Khazana — Launch & Promotional Films', ['advertising-tv'],
       client='Study Khazana', videos=['1xodV0zYdSg', '2tshq6aLFSg'],
       excerpt='Launch and promotional films for an education brand.',
       requirement='Launch and promotional videos to introduce an education brand to its audience.',
       description='Playback produced a launch video and a promotional film for Study Khazana, created for digital promotion and launch communication.',
       scope=['Launch video', 'Promotional film', 'Editing'], services=['advertising-films', 'promotional-videos']),
    _p('sanskrit-vidyapeetha-corporate-video', 'Shri Lal Bahadur Shastri Rashtriya Sanskrit Vidyapeetha', ['corporate-films'],
       client='Shri Lal Bahadur Shastri Rashtriya Sanskrit Vidyapeetha', videos=['Bm9mO081wGQ'],
       excerpt='An institutional corporate video for a national university.',
       requirement='An institutional video presenting the university, its campus and its academic life.',
       description='Playback filmed and edited an institutional video for the university, presenting its campus, academic programmes and heritage.',
       scope=['Institutional film', 'Campus filming', 'Editing'], services=['corporate-films']),
    _p('berry-shirts-company-profile', 'Berry Shirts — Company Profile', ['corporate-films'],
       client='Berry Shirts', videos=['N5aez0KxaQU'],
       excerpt='A company profile film for an apparel brand.',
       requirement='A company profile film presenting the brand, its products and its manufacturing.',
       description='Playback produced a company profile film for Berry Shirts presenting its products, processes and brand story.',
       scope=['Company profile film', 'Product & facility filming', 'Editing'], services=['corporate-films']),
    _p('documentary-films', 'Documentary & Biography Films', ['advertising-tv'],
       videos=['z51spm2RWTw', '1_dhhKhAAzs', '3C_8eSLBT8g'],
       excerpt='Biographical and social documentaries, including a film on Bhai Vir Singh.',
       requirement='Narrative documentaries and biographies combining research, interviews and archival material.',
       description='Playback’s documentary work includes a biographical film on Bhai Vir Singh and social documentaries such as Delhi The Dump, combining interviews, location filming and narrative editing.',
       scope=['Research & scripting support', 'Interviews & location filming', 'Narrative editing'], services=['television-production', 'video-editing']),
    _p('event-highlight-films', 'Event & Conference Highlight Films', ['video-editing', 'corporate-events'],
       videos=['WW15w_4Z2FI', 'wdmT-hcO0Vk', 'rdLm2_g-EMs', 'GheD8nXvi0E', 'NIDHO0DOaKM'],
       excerpt='Highlight films that compress a conference or festival into a few memorable minutes.',
       requirement='Short, engaging highlight films for conferences, cultural festivals and live events.',
       description='From conference highlights to cultural festivals such as Ras Ras Banaras and Andaz-e-Agra, Playback edits multi-camera footage into highlight films for promotion, sponsors and social media, including live multi-camera editing on site.',
       scope=['Multi-camera coverage', 'Live editing', 'Highlight film editing', 'Music & graphics'], services=['video-editing', 'event-management']),
    _p('khelo-india-school-games', 'Khelo India School Games', ['video-editing', 'corporate-events'],
       videos=['qEPQBeXxoi0'],
       excerpt='Sports event production for the Khelo India School Games.',
       requirement='Video production for a national school sports event.',
       description='Playback contributed video production for the Khelo India School Games, capturing the athletes, competition and spirit of the event.',
       scope=['Sports event filming', 'Editing'], services=['video-production']),
    _p('healthcare-youtube-content', 'YouTube Content for Doctors', ['digital', 'video-editing'],
       videos=['G85HUWhz9zw', 'XmEt5BASW74', '7FdQpF8KXbw', 'FmptUJXA0so', 'pG0NPg5AuyY', 'Wd6rnvPwNzk', 'MBmDHusiQ5g'],
       featured=True,
       excerpt='Patient-education videos and YouTube content for gynaecologists, specialists and clinics.',
       requirement='Credible, easy-to-understand video content that helps doctors educate patients and build their online presence.',
       description='Playback films and edits patient-education videos and YouTube content for doctors, covering topics from pregnancy care and diagnostic scans to treatments and healthcare law, presented clearly for patients and families.',
       scope=['Doctor-led video filming', 'Patient-education scripting support', 'Editing & subtitles', 'YouTube publishing support'],
       services=['healthcare-digital-marketing', 'social-media-marketing', 'promotional-videos']),
    _p('medical-training-videos', 'Medical Training & Educational Videos', ['corporate-films', 'medical'],
       videos=['ONGK-4ZsNBg', 'Ar5lBCxAHYg', 'O_kybAUxtuM', 'kWPETX0Rs8k', 'ctuFU9lKO6s', 'SU6GFLvVZI0'],
       excerpt='Clinical training films for hospitals and healthcare programmes, including Safdarjung Hospital.',
       requirement='Clear clinical training videos for hospital staff and healthcare quality programmes.',
       description='Playback produces training and educational films for hospitals and health programmes, covering equipment use, clinical procedures and quality-improvement projects, filmed in working clinical environments.',
       scope=['Clinical training films', 'Procedure demonstrations', 'Quality-improvement documentation', 'Editing & graphics'],
       services=['corporate-films', 'medical-conference-management']),
    _p('social-media-reels', 'Reels & Short-Form Content', ['digital'],
       videos=['1l6g1eW-p3w', 'MU3q9bkSXnQ', '1pIDhO-cPIU', 'b4MptEtHXBc', 'fBadLshype0'],
       excerpt='Vertical reels, chroma shoots and short promotional clips for social media.',
       requirement='Short-form vertical content designed for Instagram Reels, YouTube Shorts and promotions.',
       description='Playback shoots and edits reels and short-form videos for brands and professionals, including green-screen (chroma) productions and YouTube promotion content.',
       scope=['Reel concepts', 'Vertical video shoots', 'Chroma production', 'Social editing'], services=['social-media-marketing', 'promotional-videos']),
    _p('motion-graphics-explainers', 'Motion Graphics & Explainer Videos', ['video-editing', 'digital'],
       videos=['4qPeOYxBEUQ', 'STDvW4bSBqM', 'sKIqCyvVWTA', 'jQX4BoyA5dA'],
       excerpt='Animated explainers, app tutorials and promotional motion graphics.',
       requirement='Animated videos that explain products, apps and services simply.',
       description='Playback creates motion graphic videos, app tutorials and promotional animations in multiple languages, including the BitGreen promotional video and Playback’s own video brochure.',
       scope=['Scripting & storyboards', 'Motion graphics', 'Voice-over & music', 'Language versions'], services=['video-editing', 'promotional-videos']),
]
PROJECT_BY_SLUG = {p['slug']: p for p in PROJECTS}

def project_images(p, sm=True):
    if p.get('gallery_from'):
        src, idx = p['gallery_from']
        return [f"assets/img/work/{src}/{i:02d}{'-sm' if sm else ''}.webp" for i in idx]
    return [f"assets/img/work/{p['slug']}/{i:02d}{'-sm' if sm else ''}.webp" for i in range(1, p['images'] + 1)]

def project_cover(p, sm=True):
    imgs = project_images(p, sm)
    if imgs:
        return imgs[0]
    if p['videos']:
        return yt_thumb(p['videos'][0])
    return None

def cat_labels(p, limit=2):
    order = ['medical', 'corporate-events', 'corporate-films', 'advertising-tv', 'video-editing', 'digital', 'av', 'photography']
    labs = [CAT_LABEL[c] for c in order if c in p['cats']]
    return ' · '.join(labs[:limit])


# ---------------------------------------------------------------------------
# Industries (homepage section 10)
# ---------------------------------------------------------------------------
INDUSTRIES = [
    ('Healthcare & Medical', 'Conferences · CMEs · Doctor content', 'medical-conference-management', 'assets/img/work/apccsm-medical-workshop/01-sm.webp'),
    ('Corporate & Enterprise', 'Summits · Launches · Corporate films', 'corporate-events', 'assets/img/cloud-summit-sm.webp'),
    ('Advertising & Media', 'Ad films · TV production · Documentaries', 'advertising-films', 'assets/img/greenscreen-sm.webp'),
    ('Education & Training', 'Institutional films · Training · Webinars', 'video-production', 'assets/img/work/azad-bhawan-seminar/01-sm.webp'),
    ('Consumer Brands', 'Product shoots · Social · Influencers', 'product-photography', 'assets/img/product-cookies-sm.webp'),
    ('Events & Exhibitions', 'Stalls · Branding · AV production', 'exhibition-stalls-branding', 'assets/img/booth-tata-sm.webp'),
]

JOBS = []  # Add openings here: dict(title, department, location, type, experience, summary, details=[...])

CAREER_CATEGORIES = [
    ('bi-camera-fill', 'Photography & Cinematography', 'Photographers, cinematographers, camera operators, and photography assistants.'),
    ('bi-film', 'Video Production & Editing', 'Video editors, motion graphics artists, videographers, and production assistants.'),
    ('bi-graph-up-arrow', 'Digital Marketing', 'Social media executives, SEO professionals, digital marketing executives, content creators, and advertising specialists.'),
    ('bi-vector-pen', 'Graphics & Web Development', 'Graphic designers, website developers, UI/UX designers, and creative designers.'),
    ('bi-speaker-fill', 'Event & AV Production', 'Event coordinators, production managers, LED operators, sound engineers, lighting technicians, and technical support specialists.'),
    ('bi-briefcase-fill', 'Business Development', 'Client servicing, sales, business development, and account coordination.'),
]

SERVICE_OPTIONS = ['Photography', 'Videography & Film Production', 'Video Editing', 'Digital Marketing', 'Website Development',
                   'Corporate Events', 'Medical Conferences', 'Audio-Visual Production', 'Exhibition & Branding', 'Live Streaming', 'Other Enquiry']
