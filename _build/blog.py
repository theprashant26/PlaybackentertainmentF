"""Blog posts (handover section 18: recommended initial topics).
Each post: slug, title, category, date (ISO), image, excerpt, body (HTML).
"""

BLOG_CATS = [
    ('all', 'All'), ('photography', 'Photography'), ('video-production', 'Video Production'), ('video-editing', 'Video Editing'),
    ('digital-marketing', 'Digital Marketing'), ('website-development', 'Website Development'), ('corporate-events', 'Corporate Events'),
    ('medical-conferences', 'Medical Conferences'), ('av-technology', 'AV & Technology'), ('company-updates', 'Company Updates'),
]
BLOG_CAT_LABEL = dict(BLOG_CATS)

POSTS = [
    dict(slug='choosing-a-corporate-photographer-delhi-ncr', cat='photography', date='2026-10-16',
         title='Choosing a Corporate Photographer in Delhi NCR',
         image='assets/img/work/studio-portrait-interior-shoots/01.webp',
         excerpt='Portfolio, planning, lighting and delivery: what to look for before you book a corporate photographer.',
         related_service=('corporate-photography', 'Corporate Photography'),
         body='''
<p>Corporate photographs travel further than most businesses expect. The same leadership portrait appears on your website, LinkedIn, press releases, proposals and annual report, often for years. Choosing the right photographer is therefore less about a single shoot and more about how your organisation will be seen.</p>
<h2>1. Look for corporate work, not just beautiful pictures</h2>
<p>Many photographers have impressive portfolios, but corporate photography has specific demands: consistent lighting across dozens of headshots, flattering portraits of people who are not used to the camera, and office or factory images that look professional without feeling staged. Ask to see corporate assignments similar to yours.</p>
<h2>2. Ask how they plan the shoot</h2>
<p>A good corporate shoot is organised before anyone picks up a camera. Your photographer should ask how the images will be used, which people and locations are involved, what your brand guidelines require and how much time each person can spare. A simple shot list and schedule saves hours on the day.</p>
<h2>3. Check that they can work on location</h2>
<p>Most organisations prefer the photographer to come to them. That means portable lighting, backdrops and the experience to turn a meeting room into a temporary studio. For manufacturing or healthcare clients, the photographer should also understand site safety and privacy requirements.</p>
<h2>4. Understand editing and delivery</h2>
<p>Ask what editing is included, how many images you will receive, in what formats and how quickly. Corporate teams often need a few images urgently for a press release or social post, with the full set following later.</p>
<h2>5. Consider a partner who can do more</h2>
<p>If you also need corporate films, event coverage or a new website, working with a team that offers photography, video and digital services keeps your visuals consistent and reduces coordination.</p>
<h3>A quick checklist</h3>
<ul><li>Relevant corporate portfolio</li><li>Clear planning and shot list</li><li>Portable lighting for on-location work</li><li>Agreed editing, formats and timelines</li><li>Usage rights confirmed in writing</li></ul>
<p>At Playback Media &amp; Events Hub, corporate photography is one of our foundational services. We photograph leadership teams, offices, factories and events across Delhi NCR, and can combine the shoot with video or website work when needed.</p>'''),

    dict(slug='what-makes-an-effective-corporate-film', cat='video-production', date='2026-10-13',
         title='What Makes an Effective Corporate Film?',
         image='assets/img/keynote.webp',
         excerpt='Clarity of purpose, a real story, good sound and the right length: the ingredients of a corporate film people actually watch.',
         related_service=('corporate-films', 'Corporate Films'),
         body='''
<p>A corporate film is often the first time a potential client, partner or employee sees inside your organisation. The most effective films are not the longest or the most expensive. They are the clearest.</p>
<h2>Start with one purpose</h2>
<p>Is the film introducing your company to new clients, recruiting talent, explaining a process or supporting a sales meeting? Each purpose leads to a different structure, tone and length. Trying to do everything in one film usually means doing nothing well.</p>
<h2>Tell a story, not a list</h2>
<p>Viewers remember people and situations, not lists of capabilities. Show a customer problem being solved, a product being made, or a team member explaining why their work matters. Facts become more convincing when they are part of a story.</p>
<h2>Let real people speak</h2>
<p>Leadership messages, engineer interviews and client testimonials add credibility. A good production team prepares questions in advance and helps people relax on camera so they sound like themselves.</p>
<h2>Do not neglect sound</h2>
<p>Audiences forgive slightly imperfect pictures far more readily than poor audio. Professional microphones, a quiet location and careful mixing make a significant difference.</p>
<h2>Keep it the right length</h2>
<p>For websites and social media, two to three minutes is often enough. Longer versions can work for presentations and events. Many organisations commission one main film and several short cut-downs for different platforms.</p>
<h2>Plan for distribution</h2>
<p>Think about where the film will be watched before filming begins: landscape for YouTube and presentations, vertical for Instagram, subtitles for viewers watching without sound.</p>
<p>Playback has produced corporate and institutional films for manufacturers, hospitals, colleges and service companies, in multiple languages. If you are planning a corporate film, we would be happy to discuss your objectives.</p>'''),

    dict(slug='why-video-content-matters-for-business-communication', cat='video-production', date='2026-10-09',
         title='Why Video Content Matters for Business Communication',
         image='assets/img/greenscreen.webp',
         excerpt='Video explains faster, builds trust and works across every channel. Here is how businesses use it well.',
         related_service=('video-production', 'Video Production'),
         body='''
<p>Customers, employees and partners increasingly expect to see and hear from businesses, not just read about them. Video has become a practical communication tool for organisations of every size.</p>
<h2>Video explains complex ideas quickly</h2>
<p>A two-minute demonstration can show how a product works more clearly than several pages of text. Motion graphics can simplify processes, data and services that are difficult to describe in words.</p>
<h2>Video builds trust</h2>
<p>Seeing the people behind a business, whether a doctor explaining a treatment or a founder describing the company's values, creates a sense of familiarity and credibility before the first meeting.</p>
<h2>One production, many uses</h2>
<p>Well-planned footage can become a website film, social media reels, presentation videos, recruitment content and advertising. Planning these uses at the start makes production more cost-effective.</p>
<h2>Practical types of business video</h2>
<ul><li><strong>Corporate films</strong> introduce your organisation.</li><li><strong>Product demonstrations</strong> show features and benefits.</li><li><strong>Testimonials</strong> let satisfied clients speak for you.</li><li><strong>Training videos</strong> standardise knowledge across teams.</li><li><strong>Event highlights</strong> extend the life of conferences and launches.</li><li><strong>Reels and shorts</strong> keep your social channels active.</li></ul>
<h2>Quality still matters</h2>
<p>Smartphones are excellent for quick updates, but videos that represent your brand benefit from professional planning, lighting, sound and editing.</p>
<p>From television production to corporate films and reels, video production is central to Playback's work. Explore our showreel to see examples.</p>'''),

    dict(slug='corporate-video-production-concept-to-delivery', cat='video-editing', date='2026-10-05',
         title='Corporate Video Production From Concept to Delivery',
         image='assets/img/work/azad-bhawan-seminar/04.webp',
         excerpt='A step-by-step look at how a professional corporate video is planned, filmed, edited and delivered.',
         related_service=('video-editing', 'Video Editing & Post-Production'),
         body='''
<p>Understanding the production process helps you plan realistic timelines, prepare your team and get the most value from your investment. Here is how a typical corporate video moves from idea to final file.</p>
<h2>1. Discovery</h2>
<p>We begin by understanding the message, audience, platforms, timeline and budget. This conversation shapes every later decision.</p>
<h2>2. Pre-production</h2>
<p>The concept becomes a script or interview plan, a shot list and a schedule. Locations, people, permissions, equipment and crew are confirmed. Good pre-production prevents most problems on the shoot day.</p>
<h2>3. Filming</h2>
<p>The crew records interviews, activities, facilities and supporting visuals using professional cameras, lighting and sound. A well-organised shoot respects your team's time and keeps work disruption to a minimum.</p>
<h2>4. Post-production</h2>
<p>Editing is where the story takes shape. The editor assembles the strongest material, adds music, graphics and subtitles, corrects colour and refines audio. You review a draft and share feedback before the final version is completed.</p>
<h2>5. Delivery</h2>
<p>Final files are delivered in the formats you need: high-resolution masters, web versions, vertical edits and subtitled versions.</p>
<h3>How to help your project run smoothly</h3>
<ul><li>Nominate one person to coordinate approvals</li><li>Share brand guidelines and logos early</li><li>Confirm who will appear on camera and when</li><li>Consolidate feedback into a single list per review round</li></ul>
<p>Playback manages every stage in-house, from scripting and filming to editing, motion graphics and delivery.</p>'''),

    dict(slug='seo-and-social-media-for-business-growth', cat='digital-marketing', date='2026-10-01',
         title='SEO and Social Media for Business Growth',
         image='assets/img/concert-crowd.webp',
         excerpt='Search brings people who are looking for you; social media keeps you in front of people who should know you. Here is how they work together.',
         related_service=('digital-marketing', 'Digital Marketing'),
         body='''
<p>Search engine optimisation and social media marketing are often treated as separate activities. In practice, they work best together, each strengthening the other.</p>
<h2>What SEO does</h2>
<p>SEO helps your business appear when people search for the services you provide. Because these people are already looking, search traffic often leads to high-quality enquiries. For local businesses, an optimised Google Business Profile and accurate local listings are especially important.</p>
<h2>What social media does</h2>
<p>Social media keeps your brand visible to people who may not be searching yet. Consistent, original content builds familiarity, shows your work and gives potential clients reasons to trust you.</p>
<h2>How they support each other</h2>
<ul><li>Useful website content can be shared on social channels, bringing visitors and engagement.</li><li>Social posts and videos raise awareness, leading more people to search for your brand name.</li><li>Photography and video produced for social media can improve your website pages too.</li></ul>
<h2>Start with the basics</h2>
<p>Before investing in advertising, make sure your website is fast, mobile-friendly and clearly describes your services and location. Then plan a realistic social media calendar you can maintain consistently.</p>
<h2>Measure what matters</h2>
<p>Followers and impressions are useful, but enquiries, calls and appointments show whether marketing is working for your business.</p>
<p>Since 2018, Playback has combined its photography and video production background with digital marketing, so clients get strategy and original content from one team.</p>'''),

    dict(slug='digital-marketing-for-healthcare-organisations', cat='digital-marketing', date='2026-09-26',
         title='Digital Marketing for Healthcare Organizations',
         image='assets/img/work/orange-klinic-healthcare-workshop/05.webp',
         excerpt='Patients research online before they choose a doctor. Here is how hospitals and clinics can communicate responsibly and effectively.',
         related_service=('healthcare-digital-marketing', 'Healthcare Digital Marketing'),
         body='''
<p>Most patients now look for information online before choosing a doctor, clinic or hospital. Healthcare digital marketing is about being present, helpful and credible at that moment, without exaggerated claims.</p>
<h2>Educate before you promote</h2>
<p>Patient-education content performs well because it answers real questions. Short videos in which doctors explain conditions, procedures and preventive care help patients and demonstrate expertise at the same time.</p>
<h2>Show your people and facilities</h2>
<p>Professional portraits of doctors, photographs of facilities and introductions to care teams make an organisation feel approachable. They also improve the quality of your website and Google Business Profile.</p>
<h2>Get local search right</h2>
<p>Patients usually search for nearby care. Accurate addresses, timings, services and specialities across your website and local listings are essential.</p>
<h2>Communicate responsibly</h2>
<p>Healthcare communication carries responsibility. Content should be medically accurate, reviewed by the treating doctors, respectful of patient privacy and free of misleading promises.</p>
<h2>Use conferences and CMEs</h2>
<p>Medical conferences and CMEs offer valuable content opportunities: speaker interviews, session highlights and photographs that support professional reputation among peers.</p>
<p>Playback produces YouTube content for doctors, hospital training films and healthcare photography, and supports more than 50 medical conference assignments.</p>'''),

    dict(slug='corporate-event-production-checklist', cat='corporate-events', date='2026-09-22',
         title='Corporate Event Production Checklist',
         image='assets/img/work/commvault-partner-summit/01.webp',
         excerpt='A practical checklist covering objectives, venue, AV, branding, people, media and post-event follow-up.',
         related_service=('corporate-events', 'Corporate Events'),
         body='''
<p>Whether you are planning a conference, product launch, town hall or awards evening, a structured checklist helps you avoid last-minute surprises. Use this as a starting point.</p>
<h2>Objectives and audience</h2>
<ul><li>What should guests know, feel or do after the event?</li><li>Who is attending, and how many?</li><li>What does success look like?</li></ul>
<h2>Venue and schedule</h2>
<ul><li>Hall capacity, ceiling height and power availability</li><li>Setup and rehearsal time before guests arrive</li><li>Detailed run-of-show with timings and responsibilities</li></ul>
<h2>AV and stage</h2>
<ul><li>LED wall or projection sized for the room</li><li>Sound system and enough microphones for panels</li><li>Confidence monitors and presentation control</li><li>Stage platforms, lighting and backup equipment</li></ul>
<h2>Branding</h2>
<ul><li>Stage backdrop and digital branding</li><li>Entrance, registration and directional signage</li><li>Sponsor displays and standees</li><li>Badges, lanyards and delegate kits</li></ul>
<h2>People and coordination</h2>
<ul><li>Single point of contact on the production side</li><li>Speaker briefings and presentation collection deadline</li><li>Technical operators for every hall</li></ul>
<h2>Media coverage</h2>
<ul><li>Photography shot list including group photographs</li><li>Video recording, interviews and highlight film</li><li>Live streaming for remote audiences</li></ul>
<h2>After the event</h2>
<ul><li>Photograph and video delivery timelines</li><li>Thank-you communication and social media posts</li><li>Review of what worked and what to improve</li></ul>
<p>Playback combines event production, AV, branding, photography and videography, so one partner can coordinate the whole experience.</p>'''),

    dict(slug='planning-av-for-medical-conferences', cat='medical-conferences', date='2026-09-18',
         title='Planning AV for Medical Conferences',
         image='assets/img/work/apccsm-medical-workshop/04.webp',
         excerpt='Multi-hall programmes, e-podiums, speaker timers and recordings: planning audiovisual support for scientific meetings.',
         related_service=('medical-conference-management', 'Medical Conferences & CMEs'),
         body='''
<p>Medical conferences place particular demands on audiovisual systems. Scientific sessions run to tight schedules, many speakers share the stage, and presentations often contain detailed images and video. Careful AV planning protects the quality of the scientific programme.</p>
<h2>Map the programme</h2>
<p>Start with the scientific programme: how many halls run in parallel, how many speakers each session has, and whether there are panel discussions, live demonstrations or workshops. This determines equipment and staffing for each hall.</p>
<h2>Presentation management</h2>
<p>Collect presentations in advance and load them onto a central system. A speaker preview room allows faculty to check slides before their sessions. Confidence monitors and speaker timers help sessions run to time.</p>
<h2>E-podiums and audio</h2>
<p>E-podiums simplify presentation control. Plan enough microphones for chairpersons and panels, with lapel microphones for speakers who move around.</p>
<h2>Screens and visibility</h2>
<p>LED walls and projection must be bright and large enough for medical images to be seen clearly from the back of the hall.</p>
<h2>Recording and streaming</h2>
<p>Many associations record sessions for members or stream them to remote delegates. Plan camera positions, presentation capture and internet connectivity well in advance.</p>
<h2>Workshops and hands-on sessions</h2>
<p>Live demonstrations may need close-up cameras relayed to screens so every participant can see the technique.</p>
<p>Playback provides medical conference AV, scientific session support, e-podiums, LED walls, stalls, branding, photography, videography and live streaming for healthcare events across Delhi NCR.</p>'''),

    dict(slug='choosing-led-displays-for-conferences', cat='av-technology', date='2026-09-14',
         title='Choosing LED Displays for Conferences',
         image='assets/img/stage-spiral.webp',
         excerpt='Size, pixel pitch, brightness and content format: how to choose the right LED wall for your venue.',
         related_service=('audio-visual-production', 'AV & Stage Production'),
         body='''
<p>LED walls have become the centrepiece of modern conference stages. Bright, seamless and flexible, they display presentations, videos and branding in one large canvas. Choosing the right configuration makes a significant difference to how your event looks.</p>
<h2>Size for the room</h2>
<p>The display should be large enough for delegates at the back to read slides comfortably. Consider the hall depth, ceiling height and seating layout before deciding dimensions.</p>
<h2>Pixel pitch</h2>
<p>Pixel pitch is the distance between LED pixels. A smaller pitch provides a sharper image at closer viewing distances. For most conference halls, the right pitch balances clarity with budget.</p>
<h2>Brightness and lighting</h2>
<p>LED walls are bright enough for well-lit venues, but brightness should be adjusted for the room and for camera recording so faces and slides look natural on video.</p>
<h2>Content format</h2>
<p>LED walls are often wider than standard 16:9 presentations. Prepare branding and backgrounds for the full wall, and plan how speaker slides will sit within the layout.</p>
<h2>Technical support</h2>
<p>A trained operator should manage switching between presentations, videos and camera feeds. Rehearsals help catch format issues before the audience arrives.</p>
<p>Playback coordinates LED walls, projection, sound, lighting and technical operators for conferences, launches and corporate events.</p>'''),

    dict(slug='professional-photography-for-conferences-and-events', cat='photography', date='2026-09-10',
         title='Professional Photography for Conferences and Events',
         image='assets/img/work/hcl-domino-jams/06.webp',
         excerpt='Why professional event photography matters, and how to brief your photographer for complete coverage.',
         related_service=('event-photography', 'Event & Conference Photography'),
         body='''
<p>Event photographs serve many purposes after the event ends: social media posts, sponsor reports, press releases, newsletters, websites and promotion for the next edition. Professional coverage ensures you have the images you need.</p>
<h2>Prepare a shot list</h2>
<p>Share the programme and list the must-have moments: keynote speakers, chief guests, award presentations, sponsor stalls, group photographs and networking. This helps the photographer plan their position for every important moment.</p>
<h2>Plan for multiple halls</h2>
<p>For conferences with parallel sessions, assign photographers to halls or agree a rotation so no important session is missed.</p>
<h2>Stage lighting matters</h2>
<p>Modern stages use LED walls and coloured lighting that can be challenging to photograph. Experienced event photographers know how to expose correctly for speakers and screens.</p>
<h2>Organise group photographs</h2>
<p>Group photographs take longer than expected. Schedule them in the run-of-show and have someone help gather participants.</p>
<h2>Agree delivery timelines</h2>
<p>Social media teams often need images during the event. Agree same-day selections in advance, followed by the complete edited set.</p>
<h2>Combine with video</h2>
<p>Coordinating photography and videography through one team ensures complete coverage without duplicated effort or crowded camera positions.</p>
<p>Playback has photographed corporate conferences, medical workshops, listing ceremonies, award evenings and sporting events across Delhi NCR.</p>'''),
]

POST_BY_SLUG = {p['slug']: p for p in POSTS}
