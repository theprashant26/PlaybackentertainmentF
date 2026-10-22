/* =========================================================
   Playback Media & Events Hub — site interactions
   One script for every page; each feature checks that its
   elements exist before running.
   ========================================================= */
(() => {
  'use strict';

  /* ---------------------------------------------------------
     Form submissions
     Set FORM_ENDPOINT to your CRM / form-handler URL (it must accept a
     multipart POST and return a 2xx status). Until it is set, forms are
     validated and visitors are offered prefilled email/WhatsApp to send.
  --------------------------------------------------------- */
  const FORM_ENDPOINT = window.PB_FORM_ENDPOINT || '';
  const CONTACT = { email: 'mail@playbackmedia.in', whatsapp: '919999104399', phone: '+91 9999104399' };

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const isHome = !!$('.hero');

  const yearEl = $('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Remember campaign parameters for the visit (attached to enquiries)
  try {
    const q = new URLSearchParams(location.search);
    const utm = {};
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid'].forEach(k => { if (q.get(k)) utm[k] = q.get(k); });
    if (Object.keys(utm).length) sessionStorage.setItem('pb_utm', JSON.stringify(utm));
  } catch (e) { /* storage unavailable */ }

  // Fail-safe: without GSAP, show everything, keep forms/menus working.
  const hasGsap = !!window.gsap;
  if (hasGsap) document.documentElement.classList.add('js-ready');
  if (!hasGsap) {
    document.documentElement.classList.remove('js');
    document.body.classList.remove('is-loading');
    $('.preloader')?.remove();
  }

  // Below-the-fold photo groups (logo strip, photo wall) use data-src and load only when the
  // group comes near the screen, so the first paint isn't competing with dozens of images.
  const showImg = img => { if (img.dataset.srcset) img.srcset = img.dataset.srcset; img.src = img.dataset.src; img.removeAttribute('data-src'); };
  const deferGroups = [...new Set($$('img[data-src]').map(i => i.closest('.marquee, .wall, .reel-card') || i))].filter(g => !g.classList.contains('reel-card'));
  if ('IntersectionObserver' in window) {
    const imgIO = new IntersectionObserver(entries => entries.forEach(e => {
      if (!e.isIntersecting) return;
      imgIO.unobserve(e.target);
      (e.target.matches('img') ? [e.target] : $$('img[data-src]', e.target)).forEach(showImg);
    }), { rootMargin: '600px 0px' });
    deferGroups.forEach(g => imgIO.observe(g));
  } else deferGroups.forEach(g => (g.matches('img') ? [g] : $$('img[data-src]', g)).forEach(showImg));

  /* =========================================================
     Navigation (works with or without GSAP)
  ========================================================= */
  const nav = $('.nav');
  const burger = $('.burger');
  const menu = $('.mobile-menu');
  let lenis = null;

  // Desktop dropdowns & mega menu
  const dropItems = $$('.nav__item.has-drop');
  const closeDrops = (except) => dropItems.forEach(li => {
    if (li === except) return;
    li.classList.remove('is-open');
    $('.nav__caret', li)?.setAttribute('aria-expanded', 'false');
  });
  const openDrop = (li) => {
    closeDrops(li);
    li.classList.add('is-open');
    $('.nav__caret', li)?.setAttribute('aria-expanded', 'true');
  };
  dropItems.forEach(li => {
    const caret = $('.nav__caret', li);
    let t;
    if (finePointer) {
      li.addEventListener('pointerenter', () => { clearTimeout(t); openDrop(li); });
      li.addEventListener('pointerleave', () => { t = setTimeout(() => { li.classList.remove('is-open'); caret?.setAttribute('aria-expanded', 'false'); }, 160); });
    }
    caret?.addEventListener('click', e => {
      e.preventDefault();
      li.classList.contains('is-open') ? closeDrops() : openDrop(li);
    });
    li.addEventListener('focusout', e => { if (!li.contains(e.relatedTarget)) { li.classList.remove('is-open'); caret?.setAttribute('aria-expanded', 'false'); } });
  });
  document.addEventListener('click', e => { if (!e.target.closest('.nav__item.has-drop')) closeDrops(); });

  // Mobile accordion
  $$('.mm__toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const sub = document.getElementById(btn.getAttribute('aria-controls'));
      const open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(open));
      sub?.classList.toggle('is-open', open);
      btn.closest('.mm__group')?.classList.toggle('is-open', open);
    });
  });

  function closeMenu() {
    if (!document.body.classList.contains('menu-open')) return;
    document.body.classList.remove('menu-open');
    burger?.setAttribute('aria-expanded', 'false');
    menu?.setAttribute('aria-hidden', 'true');
    lenis?.start();
    burger?.focus({ preventScroll: true });
  }
  burger?.addEventListener('click', () => {
    if (document.body.classList.contains('menu-open')) return closeMenu();
    document.body.classList.add('menu-open');
    burger.setAttribute('aria-expanded', 'true');
    menu?.setAttribute('aria-hidden', 'false');
    lenis?.stop();
    if (hasGsap && !reduceMotion) gsap.fromTo('.mm__list > li, .mm__quote', { y: 24, opacity: 0 }, { y: 0, opacity: 1, duration: .7, stagger: .04, ease: 'expo.out', delay: .15 });
  });
  window.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    closeMenu(); closeDrops();
  });
  $$('.mobile-menu a').forEach(a => a.addEventListener('click', () => closeMenu()));

  /* =========================================================
     Video modal (YouTube, loads only on click)
  ========================================================= */
  let lastFocus = null;
  const vmodal = document.createElement('div');
  vmodal.className = 'vmodal';
  vmodal.setAttribute('role', 'dialog');
  vmodal.setAttribute('aria-modal', 'true');
  vmodal.setAttribute('aria-label', 'Video player');
  vmodal.hidden = true;
  vmodal.innerHTML = '<div class="vmodal__backdrop" data-close></div><div class="vmodal__box"><button type="button" class="vmodal__close" data-close aria-label="Close video"><i class="bi bi-x-lg"></i></button><div class="vmodal__frame"></div><p class="vmodal__title"></p></div>';
  document.body.appendChild(vmodal);
  const openVideo = (id, title) => {
    lastFocus = document.activeElement;
    $('.vmodal__frame', vmodal).innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0&modestbranding=1" title="${(title || 'Video').replace(/"/g, '&quot;')}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`;
    $('.vmodal__title', vmodal).textContent = title || '';
    vmodal.hidden = false;
    requestAnimationFrame(() => vmodal.classList.add('is-open'));
    document.body.classList.add('modal-open');
    lenis?.stop();
    $('.vmodal__close', vmodal).focus();
  };
  const closeVideo = () => {
    if (vmodal.hidden) return;
    vmodal.classList.remove('is-open');
    setTimeout(() => { vmodal.hidden = true; $('.vmodal__frame', vmodal).innerHTML = ''; }, 250);
    document.body.classList.remove('modal-open');
    lenis?.start();
    lastFocus?.focus?.({ preventScroll: true });
  };
  document.addEventListener('click', e => {
    const v = e.target.closest('[data-yt]');
    if (v) { e.preventDefault(); openVideo(v.dataset.yt, v.dataset.title); return; }
    if (e.target.closest('[data-close]') && e.target.closest('.vmodal')) closeVideo();
  });
  window.addEventListener('keydown', e => { if (e.key === 'Escape') closeVideo(); });

  /* =========================================================
     Photo lightbox
  ========================================================= */
  const lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', 'Photo viewer');
  lb.hidden = true;
  lb.innerHTML = '<div class="lightbox__backdrop" data-lb-close></div><figure class="lightbox__fig"><img alt=""><figcaption></figcaption></figure><button type="button" class="lightbox__btn lightbox__prev" aria-label="Previous photo"><i class="bi bi-arrow-left"></i></button><button type="button" class="lightbox__btn lightbox__next" aria-label="Next photo"><i class="bi bi-arrow-right"></i></button><button type="button" class="lightbox__close" data-lb-close aria-label="Close photo viewer"><i class="bi bi-x-lg"></i></button>';
  document.body.appendChild(lb);
  let lbItems = [], lbIndex = 0;
  const lbShow = (i) => {
    lbIndex = (i + lbItems.length) % lbItems.length;
    const a = lbItems[lbIndex];
    const img = $('img', lb);
    img.src = a.getAttribute('href');
    img.alt = $('img', a)?.alt || '';
    $('figcaption', lb).textContent = `${lbIndex + 1} / ${lbItems.length}`;
  };
  const lbOpen = (a) => {
    lastFocus = a;
    lbItems = $$('[data-lightbox]', a.closest('[data-gallery]') || document);
    lbShow(lbItems.indexOf(a));
    lb.hidden = false;
    requestAnimationFrame(() => lb.classList.add('is-open'));
    document.body.classList.add('modal-open');
    lenis?.stop();
    $('.lightbox__close', lb).focus();
  };
  const lbClose = () => {
    if (lb.hidden) return;
    lb.classList.remove('is-open');
    setTimeout(() => { lb.hidden = true; }, 250);
    document.body.classList.remove('modal-open');
    lenis?.start();
    lastFocus?.focus?.({ preventScroll: true });
  };
  document.addEventListener('click', e => {
    const a = e.target.closest('[data-lightbox]');
    if (a) { e.preventDefault(); lbOpen(a); return; }
    if (e.target.closest('[data-lb-close]')) lbClose();
  });
  $('.lightbox__prev', lb).addEventListener('click', () => lbShow(lbIndex - 1));
  $('.lightbox__next', lb).addEventListener('click', () => lbShow(lbIndex + 1));
  window.addEventListener('keydown', e => {
    if (lb.hidden) return;
    if (e.key === 'Escape') lbClose();
    if (e.key === 'ArrowLeft') lbShow(lbIndex - 1);
    if (e.key === 'ArrowRight') lbShow(lbIndex + 1);
  });
  let touchX = null;
  lb.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', e => {
    if (touchX === null) return;
    const dx = e.changedTouches[0].clientX - touchX;
    if (Math.abs(dx) > 50) lbShow(lbIndex + (dx < 0 ? 1 : -1));
    touchX = null;
  });

  /* =========================================================
     Filters (portfolio, showreel, blog, homepage work) with shareable URLs
  ========================================================= */
  const onFilterChange = [];
  $$('[data-filter-for]').forEach(group => {
    const grid = $(group.dataset.filterFor);
    if (!grid) return;
    const items = [...grid.children].filter(el => el.dataset.cats !== undefined);
    const chips = $$('[data-filter]', group);
    const section = group.closest('section');
    const countEl = section ? $('[data-filter-count]', section) : null;
    const empty = section ? $('.empty-state', section) : null;
    const shareable = !grid.closest('.work');
    const apply = (key, push, animate = true) => {
      if (!chips.some(c => c.dataset.filter === key)) key = 'all';
      chips.forEach(c => { const on = c.dataset.filter === key; c.classList.toggle('is-active', on); c.setAttribute('aria-pressed', String(on)); });
      let shown = 0;
      items.forEach(el => {
        const ok = key === 'all' || el.dataset.cats.split(' ').includes(key);
        el.hidden = !ok;
        if (ok) shown++;
      });
      if (countEl) {
        const label = chips.find(c => c.dataset.filter === key)?.textContent || '';
        countEl.textContent = key === 'all' ? `Showing all ${shown}` : `Showing ${shown} in ${label}`;
      }
      if (empty) empty.hidden = shown !== 0;
      // Animate only on a user's click; on page load the normal scroll reveals handle the cards.
      // lazy:false renders immediately, so it can never overwrite a reveal later in the same frame.
      if (animate && hasGsap && !reduceMotion) gsap.fromTo(items.filter(el => !el.hidden), { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: .5, stagger: Math.min(.03, .6 / items.length), ease: 'power2.out', overwrite: true, lazy: false });
      else if (animate || !hasGsap) items.forEach(el => { el.style.opacity = 1; el.style.transform = 'none'; });
      if (shareable && push) {
        const u = new URL(location.href);
        key === 'all' ? u.searchParams.delete('category') : u.searchParams.set('category', key);
        history.replaceState(null, '', u);
      }
      onFilterChange.forEach(fn => fn(grid));
    };
    chips.forEach(c => c.addEventListener('click', () => apply(c.dataset.filter, true)));
    const initial = shareable ? (new URLSearchParams(location.search).get('category') || 'all') : 'all';
    apply(initial, false, false);
    // keep filtered items visible even if their reveal animation has not run
    items.forEach(el => el.classList.add('is-filterable'));
  });

  /* =========================================================
     Forms
  ========================================================= */
  const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  const fieldErr = (input, msg) => {
    const wrap = input.closest('.field') || input.closest('.check')?.parentElement;
    const err = input.type === 'checkbox' ? input.closest('form').querySelector('.consent-err') : wrap?.querySelector('.field__err');
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    (input.closest('.field') || input.closest('.check'))?.classList.toggle('is-invalid', !!msg);
    if (err) err.textContent = msg || '';
  };
  const validate = (input) => {
    if (input.disabled || input.closest('[hidden]')) return '';
    const v = (input.value || '').trim();
    if (input.type === 'checkbox') return input.required && !input.checked ? 'Please confirm your consent to continue.' : '';
    if (input.type === 'file') {
      const f = input.files && input.files[0];
      if (!f) return input.required ? 'Please attach your file.' : '';
      if (f.size > 5 * 1024 * 1024) return 'Please upload a file smaller than 5 MB.';
      if (!/\.(pdf|docx?)$/i.test(f.name)) return 'Please upload a PDF, DOC or DOCX file.';
      return '';
    }
    if (input.required && !v) return 'This field is required.';
    if (!v) return '';
    if (input.type === 'email' && !emailRe.test(v)) return 'Please enter a valid email address.';
    if (input.type === 'tel') { const d = v.replace(/\D/g, ''); if (d.length < 10 || d.length > 13) return 'Please enter a valid mobile number.'; }
    if (input.type === 'url' && !/^https?:\/\/\S+\.\S+/i.test(v)) return 'Please enter a full link starting with https://';
    return '';
  };
  const summarise = (form) => {
    const lines = [];
    $$('input, select, textarea', form).forEach(el => {
      if (!el.name || el.type === 'hidden' || el.type === 'file' || el.name === 'company_website' || el.name === 'consent' || el.disabled || el.closest('[hidden]')) return;
      if (el.type === 'checkbox' && !el.checked) return;
      const v = (el.value || '').trim();
      if (!v) return;
      const label = el.type === 'checkbox' ? el.closest('fieldset')?.querySelector('legend')?.textContent : form.querySelector(`label[for="${el.id}"]`)?.childNodes[0]?.textContent;
      lines.push(`${(label || el.name).trim()}: ${v}`);
    });
    return lines.join('\n');
  };

  $$('.pb-form').forEach(form => {
    const status = $('.form-status', form);
    const submit = $('button[type="submit"]', form);
    $$('input, select, textarea', form).forEach(el => {
      el.addEventListener('blur', () => { if (el.getAttribute('aria-invalid') === 'true' || (el.value && el.type !== 'checkbox')) fieldErr(el, validate(el)); });
      el.addEventListener('change', () => { if (el.getAttribute('aria-invalid') === 'true') fieldErr(el, validate(el)); });
    });

    // Quote page: show service-specific fields
    const sw = $('[data-quote-switch]', form);
    if (sw) {
      const sync = () => $$('fieldset.dyn', form).forEach(fs => {
        const on = fs.dataset.when === sw.value;
        fs.hidden = !on;
        $$('input, select, textarea', fs).forEach(el => { el.disabled = !on; });
        if (on && hasGsap && !reduceMotion) gsap.from(fs, { opacity: 0, y: 12, duration: .5, ease: 'power2.out' });
      });
      const map = { photography: 'Photography', video: 'Video Production', digital: 'Digital Marketing', events: 'Event Management' };
      const pre = map[new URLSearchParams(location.search).get('service')];
      if (pre) sw.value = pre;
      sw.addEventListener('change', sync);
      sync();
    }

    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (form.dataset.busy === '1') return;           // prevent duplicate submissions
      let first = null;
      $$('input, select, textarea', form).forEach(el => {
        if (!el.name || el.type === 'hidden' || el.name === 'company_website') return;
        const msg = validate(el);
        fieldErr(el, msg);
        if (msg && !first) first = el;
      });
      if (first) { first.focus(); return; }

      $('[name="source_page"]', form).value = location.href;
      try { $('[name="utm"]', form).value = sessionStorage.getItem('pb_utm') || ''; } catch (err) { /* ignore */ }

      // Honeypot: bots fill hidden fields; pretend success without sending
      if ($('[name="company_website"]', form).value) { showStatus('success'); return; }

      if (!FORM_ENDPOINT) { showStatus('fallback'); return; }

      form.dataset.busy = '1';
      submit.disabled = true;
      submit.classList.add('is-busy');
      try {
        const res = await fetch(FORM_ENDPOINT, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error(res.status);
        showStatus('success');
        form.reset();
        if (sw) sw.dispatchEvent(new Event('change'));
      } catch (err) {
        showStatus('error');
      } finally {
        form.dataset.busy = '';
        submit.disabled = false;
        submit.classList.remove('is-busy');
      }
    });

    function showStatus(kind) {
      const d = form.dataset;
      if (kind === 'success') {
        status.className = 'form-status is-success';
        status.innerHTML = `<i class="bi bi-check-circle-fill"></i><div><b>${d.successTitle}</b><p>${d.successText}</p></div>`;
      } else if (kind === 'error') {
        status.className = 'form-status is-error';
        status.innerHTML = `<i class="bi bi-exclamation-triangle-fill"></i><div><b>${d.errorTitle}</b><p>${d.errorText}</p></div>`;
      } else {
        const subject = encodeURIComponent(`Website ${form.dataset.form.replace('-', ' ')}: ${($('[name="name"], [name="full_name"]', form)?.value || '').trim()}`);
        const body = summarise(form);
        const hasFile = $$('input[type="file"]', form).some(f => f.files && f.files.length);
        status.className = 'form-status is-fallback';
        status.innerHTML = `<i class="bi bi-send-check-fill"></i><div><b>Your details are ready to send.</b>
          <p>Choose how you would like to send them to our team${hasFile ? ' (please attach your file to the email)' : ''}:</p>
          <div class="form-status__actions">
            <a class="btn-x btn-grad" href="mailto:${CONTACT.email}?subject=${subject}&body=${encodeURIComponent(body)}">Send by email <span class="ico"><i class="bi bi-envelope-fill"></i></span></a>
            <a class="btn-x btn-ghost" target="_blank" rel="noopener" href="https://api.whatsapp.com/send?phone=${CONTACT.whatsapp}&text=${encodeURIComponent(body)}">Send on WhatsApp <span class="ico"><i class="bi bi-whatsapp"></i></span></a>
          </div></div>`;
      }
      status.focus({ preventScroll: true });
      status.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
    }
  });

  // Careers: "Apply Now" pre-fills the position
  $$('[data-apply]').forEach(b => b.addEventListener('click', () => {
    const sel = $('#f-position');
    if (!sel) return;
    const title = b.dataset.apply;
    if (![...sel.options].some(o => o.text === title)) sel.add(new Option(title, title), 1);
    sel.value = title;
  }));

  if (!hasGsap) return;

  /* =========================================================
     Motion (GSAP)
  ========================================================= */
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.config({ ignoreMobileResize: true });

  // Smooth scrolling only with a mouse/trackpad; phones keep native scrolling (faster, lighter)
  if (window.Lenis && !reduceMotion && finePointer) {
    lenis = new Lenis({ duration: 1.15, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    if (isHome && $('.preloader')) lenis.stop();
  }

  const scrollToTarget = (target, immediate) => {
    if (!target) return;
    if (lenis) lenis.scrollTo(target, { offset: -90, duration: immediate ? 0 : 1.4, immediate: !!immediate });
    else target.scrollIntoView({ behavior: reduceMotion || immediate ? 'auto' : 'smooth' });
  };
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = document.getElementById(id.slice(1));
      if (!target) return;
      e.preventDefault();
      closeMenu();
      scrollToTarget(target);
      history.replaceState(null, '', id);
    });
  });

  // Marquees: duplicate tracks so the loop is seamless
  $$('.marquee').forEach(m => {
    const track = $('.marquee__track', m);
    if (!track) return;
    for (let i = 0; i < 2; i++) {
      const clone = track.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      $$('img', clone).forEach(img => img.setAttribute('alt', ''));
      m.appendChild(clone);
    }
  });

  /* ---------------------------------------------------------
     Glass ribbon — the signature motif
  --------------------------------------------------------- */
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
      hero: tablet
        ? { count: mobile ? 17 : 21, size: mobile ? 84 : 112, radius: mobile ? Math.min(132, w * .34) : 210, from: 180, to: 360, fade: 2, ramp: [0, 1] }
        : { count: 26, size: Math.min(190, w * .12), radius: Math.min(360, w * .24), from: 150, to: 395, fade: 6, ramp: [0, 1] },
      page: tablet
        ? { count: mobile ? 15 : 19, size: mobile ? 74 : 100, radius: mobile ? Math.min(118, w * .3) : 190, from: 180, to: 360, fade: 2, ramp: [0, 1] }
        : { count: 22, size: Math.min(150, w * .095), radius: Math.min(290, w * .195), from: 150, to: 395, fade: 5, ramp: [0, 1] },
      'page-solo': tablet
        ? { count: 12, size: mobile ? 70 : 96, radius: mobile ? 130 : 180, from: 110, to: 250, fade: 3, ramp: [.1, .9] }
        : { count: 18, size: Math.min(150, w * .1), radius: Math.min(300, w * .21), from: 100, to: 260, fade: 4, ramp: [0, 1] },
      cta: { count: mobile ? 14 : 22, size: mobile ? 90 : 150, radius: mobile ? 140 : 260, from: 165, to: 345, fade: 3, ramp: [.25, .95] },
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
      const pos = document.createElement('i');
      pos.className = 'pane-pos';
      pos.style.cssText = `transform:rotate(${lerp(cfg.from, cfg.to, t).toFixed(2)}deg) translateX(${cfg.radius}px);z-index:${i}`;
      const p = document.createElement('i');
      p.className = 'pane';
      p.style.cssText = `--s:${cfg.size}px;--c:${c.join(',')};--c2:${c2.join(',')};--o:${o};animation-delay:${(-i * .09).toFixed(2)}s`;
      pos.appendChild(p);
      ring.appendChild(pos);
      panes.push(p);
    }
    const item = { el, ring, panes, cfg };
    ribbons.push(item);
    return item;
  };

  // The wave runs as a CSS animation on transform only, so the GPU does the work and the
  // main thread stays free; it pauses whenever the ribbon is off-screen.
  const ribbonIO = 'IntersectionObserver' in window
    ? new IntersectionObserver(entries => entries.forEach(e => e.target.classList.toggle('is-paused', !e.isIntersecting)), { rootMargin: '100px' })
    : null;
  // Desktop gets the full pane-by-pane wave; phones and tablets get a gentle sway of the
  // whole ring (one element), which keeps the look while saving battery and CPU.
  const animateRibbon = (item) => {
    if (reduceMotion) return;
    const full = finePointer && window.innerWidth >= 992;
    item.el.classList.add(full ? 'is-live' : 'is-live-lite');
    ribbonIO?.observe(item.el);
  };

  // On small screens the hero ribbon frames the reel card instead of the headline
  const placeHeroRibbon = () => {
    const el = $('[data-ribbon="hero"]');
    const host = window.innerWidth < 992 ? $('.hero__visual') : $('.hero');
    if (el && host && el.parentElement !== host) host.prepend(el);
  };
  placeHeroRibbon();

  // Hero ribbons are built right away; the rest are built only when you scroll near them,
  // which keeps the first second after page load free for taps and scrolling.
  const lazyRibbonIO = 'IntersectionObserver' in window
    ? new IntersectionObserver(entries => entries.forEach(e => {
        if (!e.isIntersecting) return;
        lazyRibbonIO.unobserve(e.target);
        const r = buildRibbon(e.target);
        if (r) animateRibbon(r);
      }), { rootMargin: '500px 0px' })
    : null;
  $$('[data-ribbon]').forEach(el => {
    const key = el.dataset.ribbon;
    const immediate = key === 'hero' || key === 'page' || !lazyRibbonIO;
    if (!immediate) { lazyRibbonIO.observe(el); return; }
    const r = buildRibbon(el);
    if (r && key !== 'hero' && key !== 'page') animateRibbon(r);
  });
  const heroRibbon = ribbons.find(r => r.el.dataset.ribbon === 'hero');
  const pageRibbon = ribbons.find(r => r.el.dataset.ribbon === 'page');

  let lastW = window.innerWidth;
  window.addEventListener('resize', () => {
    if (Math.abs(window.innerWidth - lastW) < 80) return;
    lastW = window.innerWidth;
    placeHeroRibbon();
    if (window.innerWidth >= 1200) closeMenu();
    ribbons.splice(0).forEach(r => { ribbonIO?.unobserve(r.el); r.el.classList.remove('is-live', 'is-live-lite'); });
    $$('[data-ribbon]').filter(el => el.firstChild).forEach(el => { const r = buildRibbon(el); if (r) animateRibbon(r); });
  });

  /* ---------------------------------------------------------
     Counters (real numbers are in the HTML; animate from zero)
  --------------------------------------------------------- */
  const numFmt = new Intl.NumberFormat('en-IN');
  function countUp(el) {
    const end = parseFloat(el.dataset.count);
    const obj = { v: 0 };
    let last = -1;
    gsap.to(obj, { v: end, duration: reduceMotion ? 0 : 2.2, ease: 'power3.out', onUpdate: () => {
      const v = Math.round(obj.v);
      if (v !== last) { last = v; el.textContent = numFmt.format(v); }   // only touch the DOM when the number changes
    } });
  }
  const counterEls = $$('.stats [data-count]');
  if ('IntersectionObserver' in window) {
    const countIO = new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { countIO.unobserve(e.target); countUp(e.target); }
    }), { threshold: .4 });
    counterEls.forEach(el => countIO.observe(el));
  }

  /* ---------------------------------------------------------
     Homepage hero
  --------------------------------------------------------- */
  const reel = $('.reel-card');
  const startReel = () => {
    if (!reel) return;
    const imgs = $$('img', reel);
    // Later slides load once the page has finished loading
    const loadSlides = () => $$('img[data-src]', reel).forEach(showImg);
    if (document.readyState === 'complete') loadSlides(); else window.addEventListener('load', loadSlides, { once: true });
    const bars = $$('.reel-card__progress i', reel);
    const cat = $('[data-reel-cat]', reel);
    const title = $('[data-reel-title]', reel);
    let idx = 0;
    const DURATION = 3.6;
    const play = () => {
      const img = imgs[idx];
      if (img.dataset.src) showImg(img);
      imgs.forEach((im, i) => im.classList.toggle('is-active', i === idx));
      cat.innerHTML = img.dataset.cat || '';
      title.innerHTML = img.dataset.title || '';
      gsap.fromTo([cat, title], { y: 14, opacity: 0 }, { y: 0, opacity: 1, duration: .7, stagger: .06, ease: 'power3.out' });
      bars.forEach((b, i) => { b.classList.toggle('is-done', i < idx); b.classList.remove('is-run'); });
      void bars[idx].offsetWidth;                      // restart the CSS animation
      bars[idx].classList.add('is-run');
      setTimeout(() => { idx = (idx + 1) % imgs.length; play(); }, DURATION * 1000);
    };
    if (reduceMotion) return;
    play();
  };

  // Phones: hero text is visible from the first paint and only slides a little (no fade),
  // so the main content shows up immediately instead of waiting for the animation.
  const heroFade = (y, duration, stagger) => (finePointer && window.innerWidth >= 992)
    ? { y, opacity: 0, duration, stagger }
    : { y: Math.round(y / 3), duration: duration * .8, stagger };

  const heroIntro = () => {
    const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
    tl.from('.hero__title .line > span', { yPercent: 115, rotate: 4, duration: 1.4, stagger: .1 })
      .from('[data-hero-fade]', heroFade(30, 1.1, .08), '-=1.1')
      .from('.reel-card', { clipPath: 'inset(18% 18% 18% 18% round 32px)', scale: .9, duration: 1.6 }, '-=1.3')
      .from('[data-float]', { y: 40, opacity: 0, scale: .9, duration: 1.1, stagger: .12 }, '-=1.1')
      .from('.nav__bar', { y: -30, opacity: 0, duration: 1, clearProps: 'transform,opacity' }, '-=1.4');
    if (heroRibbon) {
      animateRibbon(heroRibbon);
      tl.from(heroRibbon.panes, { opacity: 0, duration: .9, stagger: .025, ease: 'power2.out' }, '-=1.6')
        .from(heroRibbon.ring, { scale: .7, duration: 1.2, ease: 'back.out(1.4)' }, '<');
    }
    $$('.hero [data-count]').forEach(countUp);
    startReel();
  };

  // Inner pages: lighter entrance for the page hero
  const pageIntro = () => {
    const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
    const title = $('[data-hero-title]');
    if (title) tl.from(title, heroFade(28, .8, 0));
    tl.from('[data-hero-fade]', heroFade(18, .7, .06), title ? '-=0.6' : 0);
    if (pageRibbon) {
      animateRibbon(pageRibbon);
      tl.from(pageRibbon.panes, { opacity: 0, duration: .7, stagger: .02, ease: 'power2.out' }, '-=.7')
        .from(pageRibbon.ring, { scale: .75, duration: 1, ease: 'back.out(1.4)' }, '<');
    }
  };

  const runPreloader = () => {
    const pre = $('.preloader');
    let played = false;
    const finish = () => {
      document.body.classList.remove('is-loading');
      pre?.remove();
      lenis?.start();
      if (played) ScrollTrigger.refresh();   // layout only changed if the intro screen ran
      if (location.hash) setTimeout(() => scrollToTarget(document.getElementById(location.hash.slice(1)), true), 50);
    };
    if (!isHome) { if (!reduceMotion) pageIntro(); finish(); return; }
    // The intro screen plays once per browser session
    let seen = false;
    try { seen = sessionStorage.getItem('pb_intro') === '1'; sessionStorage.setItem('pb_intro', '1'); } catch (e) { /* storage blocked */ }
    const desktop = finePointer && window.innerWidth >= 992;
    if (!pre || reduceMotion || seen || !desktop) { finish(); heroIntro(); return; }
    played = true;
    const counter = { v: 0 };
    const countEl = $('.preloader__count', pre);
    const tl = gsap.timeline();
    tl.to('.preloader__word span', { y: 0, duration: .6, ease: 'expo.out' })
      .to(counter, { v: 100, duration: .7, ease: 'power2.inOut', onUpdate: () => (countEl.textContent = Math.round(counter.v)) }, 0.05)
      .to('.preloader__bar', { scaleX: 1, duration: .7, ease: 'power2.inOut' }, 0.05)
      .to('.preloader__word span', { y: '-110%', duration: .45, ease: 'expo.in' }, '+=0.02')
      .to(pre, { yPercent: -100, duration: .75, ease: 'expo.inOut' }, '-=0.1')
      .add(heroIntro, '-=0.5')
      .add(finish);
  };
  const fontsReady = document.fonts ? Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, isHome && finePointer ? 700 : 200))]) : Promise.resolve();
  fontsReady.then(runPreloader);

  if (isHome && finePointer && !reduceMotion) {
    const hero = $('.hero');
    const ringX = heroRibbon ? gsap.quickTo(heroRibbon.el, 'x', { duration: 1.2, ease: 'power3' }) : null;
    const ringY = heroRibbon ? gsap.quickTo(heroRibbon.el, 'y', { duration: 1.2, ease: 'power3' }) : null;
    const chips = $$('[data-float]').map((el, i) => ({ x: gsap.quickTo(el, 'x', { duration: 1, ease: 'power3' }), y: gsap.quickTo(el, 'y', { duration: 1, ease: 'power3' }), depth: (i + 1) * 10 }));
    hero.addEventListener('pointermove', e => {
      const nx = e.clientX / window.innerWidth - .5;
      const ny = e.clientY / window.innerHeight - .5;
      ringX?.(nx * -40); ringY?.(ny * -30);
      chips.forEach(c => { c.x(nx * c.depth * 2); c.y(ny * c.depth * 2); });
    });
  }
  if (isHome && !reduceMotion && window.matchMedia('(min-width: 992px)').matches) {
    gsap.to('.hero__content', { yPercent: -12, opacity: .2, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    if (heroRibbon) gsap.to(heroRibbon.el, { rotation: -16, scale: .88, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
  }

  /* ---------------------------------------------------------
     Nav hide on scroll
  --------------------------------------------------------- */
  ScrollTrigger.create({
    start: 'top top', end: 'max',
    onUpdate: self => {
      if (document.body.classList.contains('menu-open') || $('.nav__item.is-open')) return;
      nav.classList.toggle('is-hidden', self.direction === 1 && self.scroll() > 240);
      nav.classList.toggle('is-scrolled', self.scroll() > 40);
    }
  });

  /* ---------------------------------------------------------
     Reveals
  --------------------------------------------------------- */
  // Reveals check each pending element's live position on scroll (rAF-throttled). This survives
  // images loading, refreshes that restore the scroll position and jumps straight to a section.
  const revealEls = $$('.reveal');
  if (reduceMotion) {
    gsap.set(revealEls, { opacity: 1, y: 0 });
  } else {
    const pending = new Set(revealEls);
    let ticking = false;
    const checkReveals = () => {
      ticking = false;
      if (!pending.size) return;
      const vh = window.innerHeight, past = [], inView = [];
      pending.forEach(el => {
        const r = el.getBoundingClientRect();
        if (!r.width && !r.height) return;               // hidden (e.g. filtered out)
        if (r.bottom < 0) past.push(el);                 // already scrolled past: show instantly
        else if (r.top < vh) inView.push(el);            // anything visible on screen: animate
      });
      past.concat(inView).forEach(el => pending.delete(el));
      if (past.length) gsap.set(past, { opacity: 1, y: 0, overwrite: true });
      if (inView.length) gsap.to(inView, { opacity: 1, y: 0, duration: .7, stagger: Math.min(.06, .35 / inView.length), ease: 'power3.out', overwrite: true });
    };
    const requestCheck = () => { if (!ticking) { ticking = true; requestAnimationFrame(checkReveals); } };
    window.addEventListener('scroll', requestCheck, { passive: true });
    window.addEventListener('resize', requestCheck);
    window.addEventListener('load', requestCheck);
    lenis?.on('scroll', requestCheck);
    onFilterChange.push(requestCheck);
    // Content can move into view without any scrolling (fonts or images finishing loading),
    // so also re-check whenever the layout changes.
    document.fonts?.ready.then(requestCheck);
    document.addEventListener('load', requestCheck, true);   // any image/iframe finishing
    if ('ResizeObserver' in window) new ResizeObserver(requestCheck).observe(document.body);
    requestCheck();
  }

  // Looping CSS animations (marquees, photo wall, seal) pause while off-screen
  if ('IntersectionObserver' in window) {
    const loopIO = new IntersectionObserver(entries => entries.forEach(e => e.target.classList.toggle('anim-paused', !e.isIntersecting)), { rootMargin: '80px' });
    $$('.marquee, .wall, .seal').forEach(el => loopIO.observe(el));
  }

  // Intro photo wall: duplicate each column for a seamless loop
  $$('.wall__track').forEach(track => {
    [...track.children].forEach(fig => {
      const clone = fig.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      $$('img', clone).forEach(img => img.setAttribute('alt', ''));
      track.appendChild(clone);
    });
  });

  /* ---------------------------------------------------------
     Responsive scroll scenes
  --------------------------------------------------------- */
  const mm = gsap.matchMedia();

  if ($('.svc-card')) {
    mm.add('(min-width: 992px) and (prefers-reduced-motion: no-preference)', () => {
      const cards = $$('.svc-stack .svc-card');
      cards.forEach((card, i) => {
        const next = cards[i + 1];
        if (!next) return;
        gsap.to(card, { scale: .94 - (cards.length - i) * .006, ease: 'none', scrollTrigger: { trigger: next, start: 'top bottom', end: 'top 25%', scrub: true } });
      });
    });
  }

  mm.add('(prefers-reduced-motion: no-preference)', () => {
    $$('[data-parallax]').forEach(img => {
      gsap.fromTo(img, { yPercent: -6 }, { yPercent: 6, ease: 'none', scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
    });
    $$('.dash__line').forEach(line => gsap.fromTo(line, { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 2, ease: 'power2.out', scrollTrigger: { trigger: line.closest('.dash'), start: 'top 85%' } }));
    if ($('.wall')) {
      gsap.fromTo('[data-wall="up"]', { y: 50 }, { y: -50, ease: 'none', scrollTrigger: { trigger: '.wall', start: 'top bottom', end: 'bottom top', scrub: true } });
      gsap.fromTo('[data-wall="down"]', { y: -50 }, { y: 50, ease: 'none', scrollTrigger: { trigger: '.wall', start: 'top bottom', end: 'bottom top', scrub: true } });
    }
    if ($('.phero__img img')) gsap.fromTo('.phero__img img', { yPercent: -4, scale: 1.08 }, { yPercent: 4, ease: 'none', scrollTrigger: { trigger: '.phero', start: 'top top', end: 'bottom top', scrub: true } });
    gsap.fromTo('.footer__word', { yPercent: 45 }, { yPercent: 0, ease: 'none', scrollTrigger: { trigger: '.footer', start: 'top bottom', end: 'bottom bottom', scrub: true } });
  });

  // Horizontal work gallery: pinned with a mouse/trackpad, swipe carousel on touch or reduced motion
  const work = $('.work');
  if (work) {
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
    onFilterChange.push(grid => { if (grid.closest('.work')) { grid.scrollLeft = 0; ScrollTrigger.refresh(); } });
  }

  // Journey line (horizontal on desktop, vertical on mobile)
  $$('.journey').forEach(j => {
    const line = $('.journey__line i', j);
    mm.add({ desktop: '(min-width: 992px)', mobile: '(max-width: 991.98px)', reduce: '(prefers-reduced-motion: reduce)' }, ctx => {
      const { desktop, reduce } = ctx.conditions;
      const prop = desktop ? 'scaleX' : 'scaleY';
      if (reduce) { gsap.set(line, { [prop]: 1 }); return; }
      gsap.fromTo(line, { [prop]: 0 }, { [prop]: 1, ease: 'none', scrollTrigger: { trigger: j, start: desktop ? 'top 75%' : 'top 70%', end: 'bottom 60%', scrub: true } });
    });
  });

  /* ---------------------------------------------------------
     Testimonials
  --------------------------------------------------------- */
  if (window.Swiper && $('.voices .swiper')) {
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
     Cursor, magnetic buttons, sector preview, reel tilt (mouse only)
  --------------------------------------------------------- */
  if (finePointer && !reduceMotion) {
    const cursor = $('.cursor');
    const dot = $('.cursor-dot');
    if (cursor && dot) {
      const cx = gsap.quickTo(cursor, 'x', { duration: .35, ease: 'power3' });
      const cy = gsap.quickTo(cursor, 'y', { duration: .35, ease: 'power3' });
      const dx = gsap.quickTo(dot, 'x', { duration: .1 });
      const dy = gsap.quickTo(dot, 'y', { duration: .1 });
      window.addEventListener('pointermove', e => { document.body.classList.add('has-cursor'); cx(e.clientX); cy(e.clientY); dx(e.clientX); dy(e.clientY); });
      document.addEventListener('pointerover', e => {
        const view = e.target.closest('[data-cursor="view"]');
        const hov = e.target.closest('a, button, .cap, summary, label');
        cursor.classList.toggle('is-view', !!view && !e.target.closest('.btn-x, .reel-card__play'));
        cursor.dataset.label = view ? (view.dataset.cursorLabel || 'View') : '';
        cursor.classList.toggle('is-hover', !view && !!hov);
        dot.style.visibility = view ? 'hidden' : 'visible';
      });
    }

    $$('.btn-x').forEach(btn => {
      if (btn.closest('.nav__mega, .pb-form, .form-status')) return;
      const mx = gsap.quickTo(btn, 'x', { duration: .6, ease: 'elastic.out(1, .4)' });
      const my = gsap.quickTo(btn, 'y', { duration: .6, ease: 'elastic.out(1, .4)' });
      btn.addEventListener('pointermove', e => {
        const r = btn.getBoundingClientRect();
        mx((e.clientX - r.left - r.width / 2) * .25);
        my((e.clientY - r.top - r.height / 2) * .35);
      });
      btn.addEventListener('pointerleave', () => { mx(0); my(0); });
    });

    const preview = $('.sector-preview');
    const list = $('.sector-list');
    if (preview && list) {
      const pImgs = $$('img', preview);
      const px = gsap.quickTo(preview, 'x', { duration: .6, ease: 'power3' });
      const py = gsap.quickTo(preview, 'y', { duration: .6, ease: 'power3' });
      const pr = gsap.quickTo(preview, 'rotation', { duration: .8, ease: 'power3' });
      let lastX = 0;
      list.addEventListener('pointerenter', e => { gsap.set(preview, { x: e.clientX, y: e.clientY }); gsap.to(preview, { opacity: 1, scale: 1, duration: .5, ease: 'power3.out', overwrite: 'auto' }); });
      list.addEventListener('pointerleave', () => gsap.to(preview, { opacity: 0, scale: .6, duration: .4, ease: 'power3.in', overwrite: 'auto' }));
      list.addEventListener('pointermove', e => { px(e.clientX); py(e.clientY); pr(gsap.utils.clamp(-12, 12, (e.clientX - lastX) * .6)); lastX = e.clientX; });
      $$('.sector a', list).forEach(a => a.addEventListener('pointerenter', () => pImgs.forEach((im, i) => im.classList.toggle('is-active', i === +a.dataset.img))));
      ScrollTrigger.create({ trigger: list, start: 'top bottom', end: 'bottom top', onLeave: () => gsap.set(preview, { opacity: 0 }), onLeaveBack: () => gsap.set(preview, { opacity: 0 }) });
    }

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

})();
