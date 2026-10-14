/* =========================================================
   Playback Entertainment & Media — Homepage interactions
   ========================================================= */
(() => {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  const yearEl = $('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Fail-safe: if GSAP did not load, show everything and stop here.
  if (!window.gsap) {
    document.documentElement.classList.remove('js');
    document.body.classList.remove('is-loading');
    $('.preloader')?.remove();
    return;
  }

  gsap.registerPlugin(ScrollTrigger);
  // Don't recalculate every trigger when the mobile address bar shows/hides (avoids jumps)
  ScrollTrigger.config({ ignoreMobileResize: true });

  /* ---------------------------------------------------------
     Smooth scroll (Lenis) wired into GSAP's ticker
  --------------------------------------------------------- */
  let lenis = null;
  if (window.Lenis && !reduceMotion) {
    lenis = new Lenis({ duration: 1.15, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    lenis.stop();
  }

  const scrollToTarget = (target) => {
    if (!target) return;
    if (lenis) lenis.scrollTo(target, { offset: -10, duration: 1.4 });
    else target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
  };

  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = $(id);
      if (!target) return;
      e.preventDefault();
      closeMenu();
      scrollToTarget(target);
    });
  });

  /* ---------------------------------------------------------
     Marquees: duplicate tracks so the loop is seamless
  --------------------------------------------------------- */
  $$('.marquee').forEach(m => {
    const track = $('.marquee__track', m);
    for (let i = 0; i < 2; i++) {
      const clone = track.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      m.appendChild(clone);
    }
  });

  /* ---------------------------------------------------------
     Glass ribbon — the signature motif
     Rounded glass panes arranged on an arc, coloured along an
     orange → red → pink → violet ramp, with a travelling wave.
  --------------------------------------------------------- */
  // A page can supply its own colours (optiontwo.html uses the logo palette)
  const RAMP = window.PB_RIBBON_RAMP || [
    [255, 176, 32], [255, 92, 32], [255, 52, 72], [236, 40, 138],
    [176, 52, 214], [139, 61, 255], [214, 40, 160], [255, 52, 72]
  ];
  const lerp = (a, b, t) => a + (b - a) * t;
  const rampAt = (t) => {
    const p = Math.min(.9999, Math.max(0, t)) * (RAMP.length - 1);
    const i = Math.floor(p), f = p - i;
    return RAMP[i].map((v, k) => Math.round(lerp(v, RAMP[i + 1][k], f)));
  };

  const ribbonPresets = () => {
    const w = window.innerWidth;
    const mobile = w < 768, tablet = w < 992;
    return {
      hero:   { count: mobile ? 20 : 26, size: mobile ? 92 : tablet ? 118 : Math.min(190, w * .12), radius: mobile ? Math.min(140, w * .36) : tablet ? 215 : Math.min(360, w * .24), from: 150, to: 395, fade: 6, ramp: [0, 1] },
      cta:    { count: mobile ? 14 : 22, size: mobile ? 90 : 150, radius: mobile ? 140 : 260, from: 165, to: 345, fade: 3, ramp: [.25, .95] },
      'side-l': { count: mobile ? 10 : 14, size: mobile ? 100 : 150, radius: mobile ? 170 : 260, from: 262, to: 358, fade: 3, ramp: [0, .45] },
      'side-r': { count: mobile ? 10 : 14, size: mobile ? 100 : 150, radius: mobile ? 170 : 260, from: 82, to: 178, fade: 3, ramp: [.4, .9] },
      'voice-l': { count: 12, size: 120, radius: 190, from: -60, to: 40, fade: 4, ramp: [0, .35] },
      'voice-r': { count: 12, size: 120, radius: 190, from: 140, to: 240, fade: 4, ramp: [.2, .5], reverse: true }
    };
  };

  const ribbons = [];
  const buildRibbon = (el) => {
    const cfg = ribbonPresets()[el.dataset.ribbon];
    if (!cfg) return;
    el.innerHTML = '';
    const ring = document.createElement('div');
    ring.className = 'ribbon__ring';
    el.appendChild(ring);
    const panes = [];
    for (let i = 0; i < cfg.count; i++) {
      const t = i / (cfg.count - 1);
      const k = cfg.reverse ? 1 - t : t;
      const c = rampAt(lerp(cfg.ramp[0], cfg.ramp[1], k));
      const c2 = rampAt(lerp(cfg.ramp[0], cfg.ramp[1], k) + .12);
      const fadeIdx = cfg.reverse ? cfg.count - 1 - i : i;
      const o = fadeIdx < cfg.fade ? .12 + (fadeIdx / cfg.fade) * .75 : 1;
      const p = document.createElement('i');
      p.className = 'pane';
      p.style.cssText = `--s:${cfg.size}px;--a:${lerp(cfg.from, cfg.to, t)}deg;--r:${cfg.radius}px;--c:${c.join(',')};--c2:${c2.join(',')};--o:${o};--tilt:62deg;z-index:${i}`;
      ring.appendChild(p);
      panes.push(p);
    }
    const item = { el, ring, panes, cfg, tweens: [] };
    ribbons.push(item);
    return item;
  };

  const animateRibbon = (item) => {
    if (reduceMotion) return;
    const { panes, ring } = item;
    item.tweens.push(gsap.fromTo(panes,
      { '--tilt': '50deg' },
      { '--tilt': '70deg', duration: 2.6, ease: 'sine.inOut', yoyo: true, repeat: -1, stagger: { each: .09, from: 'start' } }
    ));
    item.tweens.push(gsap.fromTo(panes,
      { '--twist': '-10deg' },
      { '--twist': '10deg', duration: 3.4, ease: 'sine.inOut', yoyo: true, repeat: -1, stagger: { each: .07, from: 'end' } }
    ));
    item.tweens.push(gsap.to(ring, { rotation: 8, duration: 9, ease: 'sine.inOut', yoyo: true, repeat: -1 }));
    // Only animate while on screen
    item.st = ScrollTrigger.create({
      trigger: item.el.parentElement, start: 'top bottom', end: 'bottom top',
      onToggle: self => item.tweens.forEach(tw => self.isActive ? tw.resume() : tw.pause())
    });
  };

  // On small screens the hero ribbon frames the reel card instead of the headline
  const placeHeroRibbon = () => {
    const el = $('[data-ribbon="hero"]');
    const host = window.innerWidth < 992 ? $('.hero__visual') : $('.hero');
    if (el && host && el.parentElement !== host) host.prepend(el);
  };
  placeHeroRibbon();

  $$('[data-ribbon]').forEach(el => {
    const r = buildRibbon(el);
    if (r && el.dataset.ribbon !== 'hero') animateRibbon(r);
  });
  const heroRibbon = ribbons.find(r => r.el.dataset.ribbon === 'hero');

  let lastW = window.innerWidth;
  window.addEventListener('resize', () => {
    if (Math.abs(window.innerWidth - lastW) < 80) return;
    lastW = window.innerWidth;
    placeHeroRibbon();
    if (window.innerWidth >= 992) closeMenu();
    ribbons.splice(0).forEach(r => { r.tweens.forEach(t => t.kill()); r.st?.kill(); });
    $$('[data-ribbon]').forEach(el => { const r = buildRibbon(el); if (r) animateRibbon(r); });
  });

  /* ---------------------------------------------------------
     Hero reel card (auto-advancing story)
  --------------------------------------------------------- */
  const reel = $('.reel-card');
  const startReel = () => {
    if (!reel) return;
    const imgs = $$('img', reel);
    const bars = $$('.reel-card__progress i', reel);
    const cat = $('[data-reel-cat]', reel);
    const title = $('[data-reel-title]', reel);
    const labels = [
      ['Live show', 'Stage & spectacle'],
      ['Celebrity night', 'Flipkart Seller Hub'],
      ['Corporate summit', 'Tata Tele · Milestones'],
      ['Portraits', 'Editorial photography']
    ];
    let idx = 0;
    const DURATION = 3.6;
    const play = () => {
      const img = imgs[idx];
      gsap.set(imgs, { zIndex: 0 });
      gsap.set(img, { zIndex: 1 });
      gsap.fromTo(img, { opacity: 0, scale: 1.18 }, { opacity: 1, scale: 1.02, duration: 1.4, ease: 'power3.out' });
      imgs.forEach((im, i) => i !== idx && im.classList.remove('is-active'));
      img.classList.add('is-active');
      cat.textContent = labels[idx][0];
      title.textContent = labels[idx][1];
      gsap.fromTo([cat, title], { y: 14, opacity: 0 }, { y: 0, opacity: 1, duration: .7, stagger: .06, ease: 'power3.out' });
      bars.forEach((b, i) => gsap.set(b, { '--p': i < idx ? 1 : 0 }));
      gsap.fromTo(bars[idx], { '--p': 0 }, {
        '--p': 1, duration: DURATION, ease: 'none',
        onComplete: () => { idx = (idx + 1) % imgs.length; if (idx === 0) bars.forEach(b => gsap.set(b, { '--p': 0 })); play(); }
      });
    };
    play();
  };

  /* ---------------------------------------------------------
     Preloader → hero intro
  --------------------------------------------------------- */
  const heroIntro = () => {
    const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
    tl.from('.hero__title .line > span', { yPercent: 115, rotate: 4, duration: 1.4, stagger: .1 })
      .from('[data-hero-fade]', { y: 30, opacity: 0, duration: 1.1, stagger: .08 }, '-=1.1')
      .from('.reel-card', { clipPath: 'inset(18% 18% 18% 18% round 32px)', scale: .9, duration: 1.6 }, '-=1.3')
      .from('[data-float]', { y: 40, opacity: 0, scale: .9, duration: 1.1, stagger: .12 }, '-=1.1')
      .from('.nav__bar', { y: -30, opacity: 0, duration: 1, clearProps: 'transform,opacity' }, '-=1.4');
    if (heroRibbon) {
      tl.from(heroRibbon.panes, { opacity: 0, scale: .4, duration: 1.2, stagger: .035, ease: 'back.out(1.6)' }, '-=1.8');
      tl.add(() => animateRibbon(heroRibbon), '-=0.4');
    }
    // count the floating chip
    $$('.hero [data-count]').forEach(countUp);
    startReel();
  };

  const runPreloader = () => {
    const pre = $('.preloader');
    const finish = () => {
      document.body.classList.remove('is-loading');
      pre?.remove();
      lenis?.start();
      ScrollTrigger.refresh();
    };
    if (!pre || reduceMotion) { finish(); heroIntro(); return; }
    const counter = { v: 0 };
    const countEl = $('.preloader__count', pre);
    const tl = gsap.timeline();
    tl.to('.preloader__word span', { y: 0, duration: .9, ease: 'expo.out' })
      .to(counter, { v: 100, duration: 1.1, ease: 'power2.inOut', onUpdate: () => (countEl.textContent = Math.round(counter.v)) }, 0.1)
      .to('.preloader__bar', { scaleX: 1, duration: 1.1, ease: 'power2.inOut' }, 0.1)
      .to('.preloader__word span', { y: '-110%', duration: .6, ease: 'expo.in' }, '+=0.05')
      .to(pre, { yPercent: -100, duration: 1, ease: 'expo.inOut' }, '-=0.15')
      .add(heroIntro, '-=0.65')
      .add(finish);
  };

  // Wait for fonts (max 2.5s) so the type does not jump mid-animation
  const fontsReady = document.fonts ? Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 1800))]) : Promise.resolve();
  fontsReady.then(runPreloader);

  /* ---------------------------------------------------------
     Hero pointer parallax
  --------------------------------------------------------- */
  if (finePointer && !reduceMotion) {
    const hero = $('.hero');
    const ringX = heroRibbon ? gsap.quickTo(heroRibbon.el, 'x', { duration: 1.2, ease: 'power3' }) : null;
    const ringY = heroRibbon ? gsap.quickTo(heroRibbon.el, 'y', { duration: 1.2, ease: 'power3' }) : null;
    const chips = $$('[data-float]').map((el, i) => ({
      x: gsap.quickTo(el, 'x', { duration: 1, ease: 'power3' }),
      y: gsap.quickTo(el, 'y', { duration: 1, ease: 'power3' }),
      depth: (i + 1) * 10
    }));
    hero.addEventListener('pointermove', e => {
      const nx = e.clientX / window.innerWidth - .5;
      const ny = e.clientY / window.innerHeight - .5;
      ringX?.(nx * -40); ringY?.(ny * -30);
      chips.forEach(c => { c.x(nx * c.depth * 2); c.y(ny * c.depth * 2); });
    });
  }

  // Hero exit on scroll: content drifts up, ribbon sinks (desktop only — the mobile hero is taller than the screen)
  if (!reduceMotion && window.matchMedia('(min-width: 992px)').matches) {
    gsap.to('.hero__content', { yPercent: -12, opacity: .2, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    if (heroRibbon) gsap.to(heroRibbon.el, { rotation: -16, scale: .88, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
  }

  /* ---------------------------------------------------------
     Navigation: hide on scroll down, show on scroll up
  --------------------------------------------------------- */
  const nav = $('.nav');
  ScrollTrigger.create({
    start: 'top top', end: 'max',
    onUpdate: self => {
      if (document.body.classList.contains('menu-open')) return;
      nav.classList.toggle('is-hidden', self.direction === 1 && self.scroll() > 240);
    }
  });

  const burger = $('.burger');
  const menu = $('.mobile-menu');
  function closeMenu() {
    if (!document.body.classList.contains('menu-open')) return;
    document.body.classList.remove('menu-open');
    burger.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-hidden', 'true');
    lenis?.start();
  }
  burger?.addEventListener('click', () => {
    const open = !document.body.classList.contains('menu-open');
    if (!open) return closeMenu();
    document.body.classList.add('menu-open');
    burger.setAttribute('aria-expanded', 'true');
    menu.setAttribute('aria-hidden', 'false');
    lenis?.stop();
    gsap.fromTo('.mobile-menu li a', { yPercent: 100 }, { yPercent: 0, duration: 1, stagger: .05, ease: 'expo.out', delay: .2 });
  });
  window.addEventListener('keydown', e => e.key === 'Escape' && closeMenu());

  /* ---------------------------------------------------------
     Generic reveals
  --------------------------------------------------------- */
  if (reduceMotion) {
    gsap.set('.reveal', { opacity: 1, y: 0 });
  } else {
    ScrollTrigger.batch('.reveal', {
      start: 'top 88%',
      onEnter: batch => gsap.to(batch, { opacity: 1, y: 0, duration: 1.2, stagger: .1, ease: 'expo.out', overwrite: true })
    });
  }

  /* ---------------------------------------------------------
     Intro photo wall: duplicate each column for a seamless loop
  --------------------------------------------------------- */
  $$('.wall__track').forEach(track => {
    [...track.children].forEach(fig => {
      const clone = fig.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
  });

  /* ---------------------------------------------------------
     Responsive scroll scenes
  --------------------------------------------------------- */
  const mm = gsap.matchMedia();

  // Service cards stack and recede (desktop)
  mm.add('(min-width: 992px) and (prefers-reduced-motion: no-preference)', () => {
    const cards = $$('.svc-card');
    cards.forEach((card, i) => {
      const next = cards[i + 1];
      if (!next) return;
      gsap.to(card, {
        scale: .94 - (cards.length - i) * .006, ease: 'none',
        scrollTrigger: { trigger: next, start: 'top bottom', end: 'top 25%', scrub: true }
      });
    });
  });

  // Image parallax inside service media
  mm.add('(prefers-reduced-motion: no-preference)', () => {
    $$('[data-parallax]').forEach(img => {
      gsap.fromTo(img, { yPercent: -6 }, { yPercent: 6, ease: 'none', scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
    });
    gsap.fromTo('.dash__line', { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 2, ease: 'power2.out', scrollTrigger: { trigger: '.dash', start: 'top 85%' } });
    gsap.fromTo('[data-wall="up"]', { y: 50 }, { y: -50, ease: 'none', scrollTrigger: { trigger: '.wall', start: 'top bottom', end: 'bottom top', scrub: true } });
    gsap.fromTo('[data-wall="down"]', { y: -50 }, { y: 50, ease: 'none', scrollTrigger: { trigger: '.wall', start: 'top bottom', end: 'bottom top', scrub: true } });
    gsap.fromTo('.footer__word', { yPercent: 45 }, { yPercent: 0, ease: 'none', scrollTrigger: { trigger: '.footer', start: 'top bottom', end: 'bottom bottom', scrub: true } });
  });

  // Horizontal work gallery: pinned scroll with a mouse/trackpad, native swipe carousel on touch or reduced motion
  const work = $('.work');
  mm.add({
    pin: '(min-width: 768px) and (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)',
    swipe: '(max-width: 767.98px), (hover: none), (pointer: coarse), (prefers-reduced-motion: reduce)'
  }, ctx => {
    if (!ctx.conditions.pin) {
      work.classList.add('work--swipe');
      return () => work.classList.remove('work--swipe');
    }
    const track = $('.work__track');
    const distance = () => Math.max(0, track.scrollWidth - window.innerWidth + parseFloat(getComputedStyle(track).paddingLeft));
    const tween = gsap.to(track, {
      x: () => -distance(), ease: 'none',
      scrollTrigger: {
        trigger: '.work', start: 'top top', end: () => '+=' + distance(), pin: true, scrub: 1, invalidateOnRefresh: true, anticipatePin: 1,
        onUpdate: self => gsap.set('.work__progress i', { scaleX: self.progress })
      }
    });
    $$('.work-card img').forEach(img => {
      gsap.fromTo(img, { xPercent: -6 }, { xPercent: 6, ease: 'none', scrollTrigger: { trigger: img.parentElement, containerAnimation: tween, start: 'left right', end: 'right left', scrub: true } });
    });
  });

  // Journey line (horizontal on desktop, vertical on mobile)
  mm.add({ desktop: '(min-width: 992px)', mobile: '(max-width: 991.98px)', reduce: '(prefers-reduced-motion: reduce)' }, ctx => {
    const { desktop, reduce } = ctx.conditions;
    const prop = desktop ? 'scaleX' : 'scaleY';
    if (reduce) { gsap.set('.journey__line i', { [prop]: 1 }); return; }
    gsap.fromTo('.journey__line i', { [prop]: 0 }, {
      [prop]: 1, ease: 'none',
      scrollTrigger: { trigger: '.journey', start: desktop ? 'top 75%' : 'top 70%', end: desktop ? 'bottom 60%' : 'bottom 60%', scrub: true }
    });
  });

  /* ---------------------------------------------------------
     Counters
  --------------------------------------------------------- */
  function countUp(el) {
    const end = parseFloat(el.dataset.count);
    const dec = parseInt(el.dataset.decimals || '0', 10);
    const obj = { v: 0 };
    gsap.to(obj, {
      v: end, duration: reduceMotion ? 0 : 2.2, ease: 'power3.out',
      onUpdate: () => (el.textContent = dec ? obj.v.toFixed(dec) : Math.round(obj.v).toLocaleString('en-IN'))
    });
  }
  $$('.stats [data-count]').forEach(el => {
    ScrollTrigger.create({ trigger: el, start: 'top 90%', once: true, onEnter: () => countUp(el) });
  });

  /* ---------------------------------------------------------
     Testimonials
  --------------------------------------------------------- */
  if (window.Swiper) {
    new Swiper('.voices .swiper', {
      loop: true, speed: 900, autoHeight: true, grabCursor: true,
      effect: 'fade', fadeEffect: { crossFade: true },
      autoplay: reduceMotion ? false : { delay: 6000, disableOnInteraction: false, pauseOnMouseEnter: true },
      pagination: { el: '.voices .swiper-pagination', clickable: true },
      navigation: { prevEl: '.voices__prev', nextEl: '.voices__next' },
      a11y: { enabled: true }
    });
  }

  /* ---------------------------------------------------------
     Cursor + magnetic buttons (fine pointers only)
  --------------------------------------------------------- */
  if (finePointer && !reduceMotion) {
    const cursor = $('.cursor');
    const dot = $('.cursor-dot');
    const cx = gsap.quickTo(cursor, 'x', { duration: .35, ease: 'power3' });
    const cy = gsap.quickTo(cursor, 'y', { duration: .35, ease: 'power3' });
    const dx = gsap.quickTo(dot, 'x', { duration: .1 });
    const dy = gsap.quickTo(dot, 'y', { duration: .1 });
    window.addEventListener('pointermove', e => { document.body.classList.add('has-cursor'); cx(e.clientX); cy(e.clientY); dx(e.clientX); dy(e.clientY); });

    document.addEventListener('pointerover', e => {
      const view = e.target.closest('[data-cursor="view"]');
      const hov = e.target.closest('a, button, .cap');
      cursor.classList.toggle('is-view', !!view && !e.target.closest('.btn-x'));
      cursor.dataset.label = view ? (view.dataset.cursorLabel || 'View') : '';
      cursor.classList.toggle('is-hover', !view && !!hov);
      dot.style.visibility = view ? 'hidden' : 'visible';
    });

    $$('.btn-x').forEach(btn => {
      const mx = gsap.quickTo(btn, 'x', { duration: .6, ease: 'elastic.out(1, .4)' });
      const my = gsap.quickTo(btn, 'y', { duration: .6, ease: 'elastic.out(1, .4)' });
      btn.addEventListener('pointermove', e => {
        const r = btn.getBoundingClientRect();
        mx((e.clientX - r.left - r.width / 2) * .25);
        my((e.clientY - r.top - r.height / 2) * .35);
      });
      btn.addEventListener('pointerleave', () => { mx(0); my(0); });
    });

    // Sectors: floating photo preview that follows the pointer and leans with its speed
    const preview = $('.sector-preview');
    const list = $('.sector-list');
    if (preview && list) {
      const pImgs = $$('img', preview);
      const px = gsap.quickTo(preview, 'x', { duration: .6, ease: 'power3' });
      const py = gsap.quickTo(preview, 'y', { duration: .6, ease: 'power3' });
      const pr = gsap.quickTo(preview, 'rotation', { duration: .8, ease: 'power3' });
      let lastX = 0;
      list.addEventListener('pointerenter', e => {
        gsap.set(preview, { x: e.clientX, y: e.clientY });
        gsap.to(preview, { opacity: 1, scale: 1, duration: .5, ease: 'power3.out', overwrite: 'auto' });
      });
      list.addEventListener('pointerleave', () => gsap.to(preview, { opacity: 0, scale: .6, duration: .4, ease: 'power3.in', overwrite: 'auto' }));
      list.addEventListener('pointermove', e => {
        px(e.clientX); py(e.clientY);
        pr(gsap.utils.clamp(-12, 12, (e.clientX - lastX) * .6));
        lastX = e.clientX;
      });
      $$('.sector a', list).forEach(a => a.addEventListener('pointerenter', () => {
        pImgs.forEach((im, i) => im.classList.toggle('is-active', i === +a.dataset.img));
      }));
      // hide if the page scrolls out from under a still pointer
      ScrollTrigger.create({ trigger: list, start: 'top bottom', end: 'bottom top', onLeave: () => gsap.set(preview, { opacity: 0 }), onLeaveBack: () => gsap.set(preview, { opacity: 0 }) });
    }

    // Subtle 3D tilt on the reel card
    if (reel) {
      const rx = gsap.quickTo(reel, 'rotationX', { duration: .8, ease: 'power3' });
      const ry = gsap.quickTo(reel, 'rotationY', { duration: .8, ease: 'power3' });
      gsap.set(reel, { transformPerspective: 900 });
      reel.addEventListener('pointermove', e => {
        const r = reel.getBoundingClientRect();
        ry(((e.clientX - r.left) / r.width - .5) * 10);
        rx(((e.clientY - r.top) / r.height - .5) * -10);
      });
      reel.addEventListener('pointerleave', () => { rx(0); ry(0); });
    }
  }

  window.addEventListener('load', () => ScrollTrigger.refresh());
})();
