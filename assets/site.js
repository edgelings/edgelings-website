/* Edgelings website script. Plain JavaScript, no build step.
   Config comes from window.EDG, written by _src/build.py. */
(function () {
  'use strict';
  var C = window.EDG || {};
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Statistics with consent (PostHog, EU) ---------- */
  var CKEY = 'edg.consent';
  var choice = null;
  try { choice = localStorage.getItem(CKEY); } catch (e) { /* storage blocked */ }
  var queue = [];
  var ph = null;
  function track(ev, props) {
    props = props || {};
    props.site = 'web'; props.lang = C.lang || 'en';
    if (ph) ph.capture(ev, props); else if (!choice) queue.push([ev, props]);
  }
  window.edgTrack = track;
  function loadStats(mode) {
    if (!C.ph || ph) return;
    var s = document.createElement('script');
    s.async = true; s.src = (C.phAssets || 'https://eu-assets.i.posthog.com') + '/static/array.js';
    s.onload = function () {
      if (!window.posthog || !window.posthog.init) return;
      var opts = { api_host: C.phHost || 'https://eu.i.posthog.com', autocapture: false, capture_pageview: false, capture_pageleave: true, disable_session_recording: true, disable_surveys: true, person_profiles: 'identified_only' };
      if (mode === 'yes') opts.persistence = 'localStorage+cookie';
      else { opts.cookieless_mode = 'always'; opts.persistence = 'memory'; }
      window.posthog.init(C.ph, opts);
      ph = window.posthog;
      ph.register({ site: 'web', lang: C.lang || 'en' });
      ph.capture('$pageview');
      queue.forEach(function (q) { ph.capture(q[0], q[1]); }); queue = [];
    };
    document.head.appendChild(s);
  }
  function setChoice(v) {
    choice = v;
    try { localStorage.setItem(CKEY, v); } catch (e) { /* storage blocked */ }
    $('#consent') && $('#consent').classList.remove('on');
    if (ph) { location.reload(); return; }
    loadStats(v);
  }
  var banner = $('#consent');
  if (banner) {
    if (!choice) banner.classList.add('on'); else loadStats(choice);
    $('#c-yes').addEventListener('click', function () { setChoice('yes'); });
    $('#c-no').addEventListener('click', function () { setChoice('no'); });
  }
  $$('[data-cookies]').forEach(function (b) { b.addEventListener('click', function () { banner && banner.classList.add('on'); }); });

  /* ---------- Platform: store links and the smart /get link ---------- */
  var ua = navigator.userAgent || '';
  var ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var android = /Android/.test(ua);
  document.documentElement.classList.add(ios ? 'is-ios' : android ? 'is-android' : 'is-desktop');
  $$('a[data-store]').forEach(function (a) {
    a.addEventListener('click', function () { track('store_click', { store: a.getAttribute('data-store'), placement: a.getAttribute('data-place') || '' }); });
  });
  $$('a[href="/get"]').forEach(function (a) {
    a.addEventListener('click', function () { track('get_click', { placement: a.getAttribute('data-place') || '' }); });
  });

  /* ---------- Hero loop: pause button, reduced motion, off-screen pause ---------- */
  $$('video[data-loop]').forEach(function (v) {
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); }
    var b = v.parentNode.querySelector('.vidctl');
    if (b) b.addEventListener('click', function () {
      if (v.paused) { v.play(); b.textContent = 'II'; b.setAttribute('aria-label', b.getAttribute('data-pause') || 'Pause video'); }
      else { v.pause(); b.textContent = '>'; b.setAttribute('aria-label', b.getAttribute('data-play') || 'Play video'); }
    });
    if (reduce && b) { b.textContent = '>'; b.setAttribute('aria-label', b.getAttribute('data-play') || 'Play video'); }
    if ('IntersectionObserver' in window && !reduce) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) v.pause();
          else if (!b || b.textContent !== '>') { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        });
      }, { threshold: 0.25 }).observe(v);
    }
  });

  /* ---------- Trailer: loads only on tap ---------- */
  $$('[data-trailer]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.parentNode, v = document.createElement('video');
      v.src = btn.getAttribute('data-trailer'); v.controls = true; v.autoplay = true; v.playsInline = true;
      v.setAttribute('playsinline', ''); v.poster = btn.getAttribute('data-poster') || '';
      box.querySelector('img.poster') && box.querySelector('img.poster').remove();
      btn.remove(); box.appendChild(v); var p = v.play(); if (p && p.catch) p.catch(function () {});
      track('trailer_play');
    });
  });

  /* ---------- Playable demo ---------- */
  var frameBox = $('#demo-frame'), overlay = $('#demo-overlay'), endCard = $('#demo-end'), iframe = null, levels = 0;
  var small = function () { return window.innerWidth < 760 || (window.matchMedia && matchMedia('(pointer: coarse)').matches && window.innerWidth < 1024); };
  function startDemo() {
    if (iframe) return;
    iframe = document.createElement('iframe');
    iframe.src = '/demo/?lang=' + encodeURIComponent(frameBox.getAttribute('data-lang') || 'en'); iframe.title = frameBox.getAttribute('data-title') || 'Edgelings demo'; iframe.allow = 'autoplay; fullscreen';
    if (small() && overlay) { overlay.appendChild(iframe); overlay.classList.add('on'); document.body.style.overflow = 'hidden'; }
    else { frameBox.appendChild(iframe); var st = $('.start', frameBox); st && st.remove(); }
    track('demo_start', { mode: small() ? 'fullscreen' : 'inline' });
  }
  function closeOverlay() {
    if (!overlay) return;
    overlay.classList.remove('on'); document.body.style.overflow = '';
    if (iframe) { iframe.remove(); iframe = null; }
  }
  $$('[data-demo]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); if (frameBox) frameBox.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' }); startDemo(); }); });
  var startBtn = frameBox && $('.start', frameBox);
  startBtn && startBtn.addEventListener('click', startDemo);
  var closeBtn = overlay && $('.close', overlay);
  closeBtn && closeBtn.addEventListener('click', function () { closeOverlay(); track('demo_close', { levels: levels }); });
  function showEnd() {
    closeOverlay();
    if (endCard) { endCard.classList.add('on'); if (small()) frameBox.scrollIntoView({ block: 'center' }); }
  }
  var again = endCard && $('[data-again]', endCard);
  again && again.addEventListener('click', function () { endCard.classList.remove('on'); });
  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || d.source !== 'edgelings-demo') return;
    if (d.type === 'level') { levels = Math.max(levels, d.level || 0); track('demo_level', { level: d.level }); }
    if (d.type === 'end') { track('demo_end', { levels: levels }); showEnd(); }
    if (d.type === 'get') { track('get_click', { placement: 'demo' }); location.href = (C.base || '') + '/get'; }
  });
  if (frameBox && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (iframe && iframe.contentWindow && frameBox.contains(iframe)) iframe.contentWindow.postMessage({ source: 'edgelings-site', type: e.isIntersecting ? 'resume' : 'pause' }, '*');
      });
    }, { threshold: 0.1 }).observe(frameBox);
  }

  /* ---------- Scoring strip: drag a slime towards the edge ---------- */
  var track_ = $('#track'), blob = $('#blob'), pts = $('#pts'), msg = $('#ptsmsg');
  if (track_ && blob) {
    var EDGE = 0.94, pos = 0.12, drag = false, touched = false, fallen = false;
    var zone = function (p) { return p > 0.72 ? 3 : p > 0.45 ? 2 : 1; };
    var render = function () {
      blob.style.left = (pos * 100) + '%';
      var T = function (k) { return track_.getAttribute('data-' + k) || ''; };
      if (pos > EDGE) {
        pts.textContent = T('pts').replace('{n}', '0'); pts.classList.add('zero'); msg.textContent = T('m0');
        if (!fallen) { fallen = true; blob.classList.add('fall'); setTimeout(function () { blob.classList.remove('fall'); fallen = false; pos = 0.12; render(); }, 900); }
        return;
      }
      var z = zone(pos);
      pts.textContent = T('pts').replace('{n}', String(30 * z)); pts.classList.remove('zero');
      msg.textContent = T('m' + z);
    };
    var at = function (x) { var r = track_.getBoundingClientRect(); return Math.max(0.05, Math.min(1.02, (x - r.left) / r.width)); };
    blob.addEventListener('pointerdown', function (e) { drag = true; touched = true; blob.setPointerCapture(e.pointerId); });
    blob.addEventListener('pointermove', function (e) { if (drag && !fallen) { pos = at(e.clientX); render(); } });
    blob.addEventListener('pointerup', function () { drag = false; track('score_strip'); });
    blob.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { pos = Math.min(1.02, pos + 0.04); touched = true; render(); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { pos = Math.max(0.05, pos - 0.04); touched = true; render(); e.preventDefault(); }
    });
    render();
    // Until someone touches it, the slime shows the idea by itself.
    if (!reduce) {
      var t = 0;
      var auto = setInterval(function () {
        if (touched) { clearInterval(auto); return; }
        if (fallen) return;
        t += 1; pos = 0.12 + (t % 30) * 0.03; render();
      }, 160);
    }
  }

  /* ---------- Screenshots carousel ---------- */
  $$('.carousel').forEach(function (c) {
    var strip = $('.strip', c);
    $$('.arrow', c).forEach(function (a) {
      a.addEventListener('click', function () { strip.scrollBy({ left: (a.classList.contains('l') ? -1 : 1) * 260, behavior: reduce ? 'auto' : 'smooth' }); });
    });
  });

  /* ---------- Meet the slimes: wiggle on tap ---------- */
  $$('.slime').forEach(function (s) {
    var go = function () { s.classList.remove('wig'); void s.offsetWidth; s.classList.add('wig'); };
    s.addEventListener('click', go); s.addEventListener('mouseenter', go);
    s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { go(); e.preventDefault(); } });
  });

  /* ---------- FAQ opens are counted ---------- */
  $$('.faq details').forEach(function (d) {
    d.addEventListener('toggle', function () { if (d.open) track('faq_open', { q: (d.id || '').slice(0, 40) }); });
  });

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.12 });
    $$('.rv').forEach(function (el) { io.observe(el); });
  } else { $$('.rv').forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- Language: menu choice is remembered, the visitor's own language is suggested ---------- */
  var LKEY = 'edg.lang';
  $$('[data-setlang]').forEach(function (a) { a.addEventListener('click', function () { try { localStorage.setItem(LKEY, a.getAttribute('data-setlang')); } catch (e) { /* storage blocked */ } track('lang_switch', { to: a.getAttribute('data-setlang') }); }); });
  (function () {
    var cur = C.lang || 'en', sug = C.suggest || {}, bar = $('#suggest');
    if (!bar) return;
    var stored = null; try { stored = localStorage.getItem(LKEY); } catch (e) { /* storage blocked */ }
    if (stored) return;
    var pick = function () {
      var list = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || 'en'];
      for (var i = 0; i < list.length; i++) {
        var tag = String(list[i] || '').toLowerCase(), c = tag.split('-')[0];
        if (c === 'pt') return tag === 'pt-br' ? 'pt-BR' : 'pt';
        if (c === 'es') return tag === 'es' || tag === 'es-es' ? 'es' : 'es-419';
        if (c === 'zh') return /hant|-tw|-hk|-mo/.test(tag) ? 'zh-Hant' : 'zh-Hans';
        if (sug[c]) return c;
      }
      return 'en';
    };
    var want = pick();
    if (want === cur || !sug[want]) return;
    var alt = document.querySelector('link[rel="alternate"][data-code="' + want + '"]');
    if (!alt) return;
    var t = sug[want];
    bar.innerHTML = '';
    var span = document.createElement('span'); span.textContent = t.text; span.lang = t.html;
    var go = document.createElement('a'); go.className = 'pill small'; go.href = alt.href; go.textContent = t.go; go.lang = t.html;
    go.addEventListener('click', function () { try { localStorage.setItem(LKEY, want); } catch (e) { /* storage blocked */ } track('lang_suggest', { to: want, taken: true }); });
    var no = document.createElement('button'); no.type = 'button'; no.className = 'x'; no.textContent = t.no; no.lang = t.html;
    no.addEventListener('click', function () { try { localStorage.setItem(LKEY, cur); } catch (e) { /* storage blocked */ } bar.classList.remove('on'); track('lang_suggest', { to: want, taken: false }); });
    bar.appendChild(span); bar.appendChild(go); bar.appendChild(no); bar.classList.add('on');
  })();

  /* ---------- Social links: switched on in Supabase (table site_links) ---------- */
  var social = $('#social');
  if (social && C.sb && C.sbKey) {
    var ICON = {
      tiktok: 'M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.8a5.7 5.7 0 1 0 4.8 5.6V9.1a7.3 7.3 0 0 0 4.3 1.4v-3a4.3 4.3 0 0 1-3.2-1.7z',
      instagram: 'M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM12 4.6c2.4 0 2.7 0 3.6.1 2.4.1 3.6 1.3 3.7 3.7.1 1 .1 1.2.1 3.6s0 2.7-.1 3.6c-.1 2.4-1.3 3.6-3.7 3.7-1 .1-1.2.1-3.6.1s-2.7 0-3.6-.1c-2.4-.1-3.6-1.3-3.7-3.7-.1-1-.1-1.2-.1-3.6s0-2.7.1-3.6C4.8 6 6 4.8 8.4 4.7c1-.1 1.2-.1 3.6-.1zM12 3c-2.4 0-2.8 0-3.7.1C5 3.2 3.2 5 3.1 8.3 3 9.2 3 9.6 3 12s0 2.8.1 3.7c.1 3.3 1.9 5.1 5.2 5.2.9.1 1.3.1 3.7.1s2.8 0 3.7-.1c3.3-.1 5.1-1.9 5.2-5.2.1-.9.1-1.3.1-3.7s0-2.8-.1-3.7C20.8 5 19 3.2 15.7 3.1 14.8 3 14.4 3 12 3z',
      youtube: 'M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3z',
      facebook: 'M14 8.5V6.8c0-.8.2-1.3 1.4-1.3H17V2.6c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.1H8.3v3H11V21h3v-9.5h2.6l.4-3z',
      x: 'M17.8 3h3l-6.6 7.6L22 21h-6.1l-4.8-6.3L5.6 21h-3l7.1-8.1L2.2 3h6.2l4.4 5.8zm-1 16.2h1.7L7.3 4.7H5.5z',
      discord: 'M19.3 5.3A16 16 0 0 0 15.4 4l-.5 1a14.8 14.8 0 0 0-5.8 0l-.5-1a16 16 0 0 0-3.9 1.3C2.2 9 1.5 12.6 1.8 16.2a16 16 0 0 0 4.9 2.5l1-1.6a10.4 10.4 0 0 1-1.6-.8l.4-.3a11.4 11.4 0 0 0 10.9 0l.4.3-1.6.8 1 1.6a16 16 0 0 0 4.9-2.5c.4-4.2-.7-7.8-2.8-10.9zM8.7 14c-1 0-1.8-.9-1.8-2s.8-2 1.8-2 1.8.9 1.8 2-.8 2-1.8 2zm6.6 0c-1 0-1.8-.9-1.8-2s.8-2 1.8-2 1.8.9 1.8 2-.8 2-1.8 2z'
    };
    fetch(C.sb + '/rest/v1/site_links?select=network,url,label&active=eq.true&order=sort.asc', { headers: { apikey: C.sbKey } })
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (rows) {
        rows.forEach(function (r) {
          if (!ICON[r.network] || !/^https:\/\//.test(r.url || '')) return;
          var a = document.createElement('a');
          a.href = r.url; a.rel = 'noopener me'; a.target = '_blank'; a.setAttribute('aria-label', r.label || ('Edgelings on ' + r.network));
          a.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="' + ICON[r.network] + '"/></svg>';
          a.addEventListener('click', function () { track('social_click', { network: r.network }); });
          social.appendChild(a);
        });
        if (social.children.length) social.hidden = false;
      }).catch(function () { /* no links, nothing shown */ });
  }
})();
