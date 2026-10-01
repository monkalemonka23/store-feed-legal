/* growboost.pl - screenshot lightbox + reveal on scroll.
   Both features are optional: without JS the screenshots are still
   visible and every section is rendered in its final state. */
(function () {
  'use strict';

  /* ---------- lightbox ---------- */
  var dlg = document.getElementById('lightbox');
  var dlgImg = dlg ? dlg.querySelector('img') : null;
  var dlgCap = dlg ? dlg.querySelector('.lb__cap') : null;

  if (dlg && dlgImg && typeof dlg.showModal === 'function') {
    document.addEventListener('click', function (ev) {
      var btn = ev.target && ev.target.closest ? ev.target.closest('[data-full]') : null;
      if (btn) {
        var img = btn.querySelector('img');
        dlgImg.src = btn.getAttribute('data-full');
        dlgImg.alt = img ? img.alt : '';
        if (dlgCap) { dlgCap.textContent = btn.getAttribute('data-caption') || ''; }
        dlg.classList.remove('lb--zoom');
        dlg.showModal();
        return;
      }

      /* Screenshots are dense: on a phone the whole picture fits the screen
         but the text inside the widget does not. One tap switches to full
         size and the dialog pans. */
      if (ev.target === dlgImg) {
        dlg.classList.toggle('lb--zoom');
        return;
      }
      if (ev.target === dlg || (ev.target.closest && ev.target.closest('[data-lb-close]'))) {
        dlg.close();
      }
    }, false);

    dlg.addEventListener('close', function () {
      dlgImg.removeAttribute('src');
      dlg.classList.remove('lb--zoom');
    });
  }


  /* ---------- biezaca sekcja w przyklejonym pasku ---------- */
  var nav = document.querySelector('.pagenav');
  if (nav && 'IntersectionObserver' in window) {
    var links = {}, targets = [];
    Array.prototype.forEach.call(nav.querySelectorAll('a[href^="#"]'), function (a) {
      var el = document.getElementById(a.getAttribute('href').slice(1));
      if (el) { links[el.id] = a; targets.push(el); }
    });
    if (targets.length) {
      var seen = {};
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { seen[e.target.id] = e.isIntersecting; });
        /* Sekcje sa dlugie, wiec w pasku widoczne bywaja dwie naraz.
           Bierzemy OSTATNIA w kolejnosci dokumentu - czyli te, w ktora
           wlasnie weszlismy, nie te, z ktorej wychodzimy. */
        var current = null;
        for (var i = targets.length - 1; i >= 0; i--) {
          if (seen[targets[i].id]) { current = targets[i].id; break; }
        }
        for (var id in links) {
          if (id === current) { links[id].setAttribute('aria-current', 'true'); }
          else { links[id].removeAttribute('aria-current'); }
        }
      }, { rootMargin: '-70px 0px -55% 0px', threshold: 0 });
      targets.forEach(function (t) { spy.observe(t); });
    }
  }

  /* ---------- reveal on scroll ---------- */
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.reveal');
  if (!items.length) { return; }

  if (reduced || !('IntersectionObserver' in window)) {
    for (var i = 0; i < items.length; i++) { items[i].classList.add('is-in'); }
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  for (var j = 0; j < items.length; j++) { io.observe(items[j]); }
})();
