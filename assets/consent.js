/* growboost.pl - cookie banner + Google Consent Mode v2 + GTM */
(function () {
  'use strict';

  var GTM_ID = 'GTM-WVR58V76';
  var STORAGE_KEY = 'gb_consent_v1';
  var POLICY_URL = '/privacy-policy/';

  /* --- dataLayer + gtag --- */
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  var saved = null;
  try { saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null'); } catch (e) { saved = null; }

  /* --- 1. Everything denied by default (must run BEFORE GTM) --- */
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    functionality_storage: 'granted',
    security_storage: 'granted',
    wait_for_update: 500
  });

  /* --- 2. Restore previous choice --- */
  if (saved && saved.analytics === true) {
    gtag('consent', 'update', { analytics_storage: 'granted' });
  }

  /* --- 3. Load GTM --- */
  (function (w, d, s, i) {
    w.dataLayer = w.dataLayer || [];
    w.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
    var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s);
    j.async = true;
    j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i;
    f.parentNode.insertBefore(j, f);
  })(window, document, 'script', GTM_ID);

  /* --- 4. Save the choice --- */
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

  /* --- 5. Banner --- */
  var el = null;

  function hide() {
    if (el && el.parentNode) { el.parentNode.removeChild(el); }
    el = null;
  }

  function show() {
    if (el || !document.body) { return; }
    el = document.createElement('div');
    el.className = 'gb-consent';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Cookie settings');
    el.innerHTML =
      '<p class="gb-consent__text">We use cookies that are necessary for this site to work. ' +
      'With your consent we also run Google Analytics 4 to see which pages people find useful. ' +
      'Details in our <a href="' + POLICY_URL + '">privacy policy</a>.</p>' +
      '<div class="gb-consent__actions">' +
      '<button type="button" class="gb-btn gb-btn--ghost" data-gb="reject">Necessary only</button>' +
      '<button type="button" class="gb-btn gb-btn--solid" data-gb="accept">Allow analytics</button>' +
      '</div>';
    document.body.appendChild(el);
  }

  /* --- 6. Event delegation: works for the banner and for any
         [data-gb-consent-open] link, whenever it appears --- */
  document.addEventListener('click', function (ev) {
    var t = ev.target;
    if (!t || !t.closest) { return; }

    var opener = t.closest('[data-gb-consent-open]');
    if (opener) { ev.preventDefault(); show(); return; }

    var btn = t.closest('[data-gb]');
    if (btn) { save(btn.getAttribute('data-gb') === 'accept'); }
  }, false);

  function init() { if (!saved) { show(); } }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
