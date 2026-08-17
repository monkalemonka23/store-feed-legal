/* growboost.pl - launch countdown + waitlist form
   Form id and field ids are configured. No setup needed.
   Form details in the comment at the bottom of this file. */
(function () {
  'use strict';

  var LAUNCH_ISO = '2026-08-31T00:00:00+02:00';

  var GOOGLE_FORM_ID  = '1FAIpQLSeskbrcZf3ttK_oM5Q6zuBnhjsnauQIrLC_rvTTS4PV7dqijg';
  var ENTRY_EMAIL     = 'entry.1924395242';
  var ENTRY_CONSENT   = 'entry.1990253133';

  /* ---------- countdown ---------- */
  var target = new Date(LAUNCH_ISO).getTime();
  var units = ['days', 'hours', 'minutes', 'seconds'];
  var out = {};

  units.forEach(function (u) { out[u] = document.getElementById('cd-' + u); });

  function pad(n) { return n < 10 ? '0' + n : String(n); }

  function tick() {
    var left = target - Date.now();
    if (left <= 0) {
      var box = document.getElementById('countdown');
      if (box) { box.innerHTML = '<p class="cd-live">Store Feed is live.</p>'; }
      return;
    }
    var s = Math.floor(left / 1000);
    var v = {
      days: Math.floor(s / 86400),
      hours: Math.floor(s % 86400 / 3600),
      minutes: Math.floor(s % 3600 / 60),
      seconds: s % 60
    };
    units.forEach(function (u) {
      if (out[u]) { out[u].textContent = u === 'days' ? String(v[u]) : pad(v[u]); }
    });
    setTimeout(tick, 1000);
  }

  if (out.days) { tick(); }

  /* ---------- focus the email field when arriving via #launch ---------- */
  document.addEventListener('click', function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest('a[href="#launch"]') : null;
    if (!a) { return; }
    setTimeout(function () {
      var input = document.getElementById('notify-email');
      if (input && !input.disabled) { input.focus({ preventScroll: true }); }
    }, 600);
  }, false);

  /* ---------- waitlist form ---------- */
  var form = document.getElementById('notify-form');
  if (!form) { return; }

  var emailEl = document.getElementById('notify-email');
  var consentEl = document.getElementById('notify-consent');
  var trapEl = document.getElementById('notify-company');
  var errEl = document.getElementById('notify-error');
  var okEl = document.getElementById('notify-ok');
  var btnEl = document.getElementById('notify-btn');

  function fail(msg, el) {
    errEl.textContent = msg;
    errEl.hidden = false;
    if (el) { el.focus(); }
  }

  emailEl.addEventListener('input', function () { errEl.hidden = true; });
  consentEl.addEventListener('change', function () { errEl.hidden = true; });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    if (trapEl && trapEl.value) { return; }

    var email = emailEl.value.trim();
    if (!email || email.indexOf('@') < 1 || email.indexOf('.', email.indexOf('@')) < 0) {
      return fail('Enter a valid email address.', emailEl);
    }
    if (!consentEl.checked) {
      return fail('Please tick the consent box so we may email you.', consentEl);
    }

    btnEl.disabled = true;
    btnEl.textContent = 'Sending…';

    var body = new FormData();
    body.append(ENTRY_EMAIL, email);
    body.append(ENTRY_CONSENT, 'I consent');

    fetch('https://docs.google.com/forms/d/e/' + GOOGLE_FORM_ID + '/formResponse', {
      method: 'POST',
      mode: 'no-cors',
      body: body
    }).then(function () {
      form.hidden = true;
      okEl.hidden = false;
      okEl.focus();
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: 'waitlist_signup' });
    })['catch'](function () {
      btnEl.disabled = false;
      btnEl.textContent = 'Notify me';
      fail('Something went wrong. Please email support@growboost.pl instead.');
    });
  });
})();

/* ---------------------------------------------------------------
   Google Form: "Store Feed launch list"
   https://docs.google.com/forms/d/e/1FAIpQLSeskbrcZf3ttK_oM5Q6zuBnhjsnauQIrLC_rvTTS4PV7dqijg/viewform
   entry.1924395242 = Email
   entry.1990253133 = Consent ("I consent")

   If the form questions are ever edited, re-read the ids via
   three-dot menu -> "Get pre-filled link".
   --------------------------------------------------------------- */
