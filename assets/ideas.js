/* growboost.pl - formularz pomyslow na teksty.
   Wysylka w tle do Google Forms, tak samo jak zapis na premiere
   w launch.js. Identyfikatory pol pochodza z linku prefill
   (operatorka, 2026-10-01).

   UWAGA na pole formy: jesli drugie pytanie w formularzu jest
   jednokrotnego wyboru, Google przyjmuje wylacznie doslowna tresc
   opcji - cokolwiek innego przepada po cichu. Dlatego wybrana forma
   leci DODATKOWO w pierwszym polu, w nawiasie: nawet przy niezgodnej
   etykiecie informacja dociera. */
(function () {
  'use strict';

  var FORM_ID = '1FAIpQLSf-AJdyDGHUsGrS5iN1eiyMh14JRvSnTtcyiY3E0Bd_uSpLcw';
  var ENTRY_TOPIC  = 'entry.544504816';
  var ENTRY_FORMAT = 'entry.1449093439';

  var form = document.getElementById('ideas-form');
  if (!form) { return; }

  var topicEl = document.getElementById('ideas-topic');
  var trapEl = document.getElementById('ideas-company');
  var errEl = document.getElementById('ideas-error');
  var okEl = document.getElementById('ideas-ok');
  var btnEl = document.getElementById('ideas-btn');

  topicEl.addEventListener('input', function () { errEl.hidden = true; });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    if (trapEl && trapEl.value) { return; }

    var topic = topicEl.value.trim();
    if (topic.length < 5) {
      errEl.textContent = 'Write a sentence or two about what you would like to read.';
      errEl.hidden = false;
      topicEl.focus();
      return;
    }

    var picked = form.querySelector('input[name="format"]:checked');
    var format = picked ? picked.value : 'either is fine';

    btnEl.disabled = true;
    btnEl.textContent = 'Sending...';

    var body = new FormData();
    body.append(ENTRY_TOPIC, topic + '\n\n(Prefers: ' + format + ')');
    body.append(ENTRY_FORMAT, format);

    fetch('https://docs.google.com/forms/d/e/' + FORM_ID + '/formResponse', {
      method: 'POST',
      mode: 'no-cors',
      body: body
    }).then(function () {
      form.hidden = true;
      okEl.hidden = false;
      okEl.focus();
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: 'blog_idea_sent', idea_format: format });
    })['catch'](function () {
      btnEl.disabled = false;
      btnEl.textContent = 'Send the idea';
      errEl.textContent = 'Something went wrong. Please email support@growboost.pl instead.';
      errEl.hidden = false;
    });
  });
})();
