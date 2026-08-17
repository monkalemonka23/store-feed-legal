/* growboost.pl — baner cookies + Google Consent Mode v2 + GTM
   Kategorie: niezbędne (zawsze) + analityka (GA4 przez GTM).
   PODMIEŃ GTM_ID na swój identyfikator kontenera. */
(function () {
  'use strict';

  var GTM_ID = 'GTM-WVR58V76';        // <-- PODMIEŃ
  var STORAGE_KEY = 'gb_consent_v1';
  var POLICY_URL = '/privacy-policy/';

  /* --- dataLayer + gtag --- */
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  var saved = null;
  try { saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null'); } catch (e) { saved = null; }

  /* --- 1. Domyślnie wszystko odrzucone (musi być PRZED GTM) --- */
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    functionality_storage: 'granted',
    security_storage: 'granted',
    wait_for_update: 500
  });

  /* --- 2. Odtworzenie wcześniejszej decyzji --- */
  if (saved && saved.analytics === true) {
    gtag('consent', 'update', { analytics_storage: 'granted' });
  }

  /* --- 3. Start GTM --- */
  (function (w, d, s, i) {
    w[ 'dataLayer' ] = w[ 'dataLayer' ] || [];
    w.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
    var f = d.getElementsByTagName(s)[ 0 ],
        j = d.createElement(s);
    j.async = true;
    j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i;
    f.parentNode.insertBefore(j, f);
  })(window, document, 'script', GTM_ID);

  /* --- 4. Zapis decyzji --- */
  function save(analytics) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        analytics: analytics,
        date: new Date().toISOString()
      }));
    } catch (e) {}
    gtag('consent', 'update', { analytics_storage: analytics ? 'granted' : 'denied' });
    window.dataLayer.push({ event: analytics ? 'consent_accepted' : 'consent_rejected' });
    hide();
  }

  /* --- 5. Baner --- */
  var el = null;

  function hide() { if (el) { el.remove(); el = null; } }

  function show() {
    if (el) return;
    el = document.createElement('div');
    el.className = 'gb-consent';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Cookie consent form');
    el.innerHTML =
      '<p class="gb-consent__text">We use nessesary cookis to let this page work. ' +
      'If Yo will agree, we will use Google Analytics 4 (GA4), to know, which files are useful. ' +
      'Detailes in <a href="' + /privacy-policy/ + '">privacy policy</a>.</p>' +
      '<div class="gb-consent__actions">' +
      '<button type="button" class="gb-btn gb-btn--ghost" data-gb="reject">Only nessesary</button>' +
      '<button type="button" class="gb-btn gb-btn--solid" data-gb="accept">I agree for GA4</button>' +
      '</div>';
    document.body.appendChild(el);
    el.querySelector('[data-gb="accept"]').addEventListener('click', function () { save(true); });
    el.querySelector('[data-gb="reject"]').addEventListener('click', function () { save(false); });
  }

  function init() {
    if (!saved) show();
    // link „zmień zgody" gdziekolwiek na stronie
    document.querySelectorAll('[data-gb-consent-open]').forEach(function (a) {
      a.addEventListener('click', function (ev) { ev.preventDefault(); show(); });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
