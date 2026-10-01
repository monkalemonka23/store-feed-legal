/* growboost.pl - formularz pomyslow na teksty.
   Nie ma backendu i nic nie zapisuje: skleja tresc maila i oddaje ja
   kliencie pocztowemu uzytkownika. Dzieki temu nie zbieramy zadnych
   danych i nie trzeba nic dopisywac do polityki prywatnosci. */
(function () {
  'use strict';

  var form = document.getElementById('ideas-form');
  if (!form) { return; }

  var topicEl = document.getElementById('ideas-topic');
  var errEl = document.getElementById('ideas-error');

  topicEl.addEventListener('input', function () { errEl.hidden = true; });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    var topic = topicEl.value.trim();
    if (topic.length < 5) {
      errEl.textContent = 'Write a sentence or two about what you would like to read.';
      errEl.hidden = false;
      topicEl.focus();
      return;
    }

    var picked = form.querySelector('input[name="format"]:checked');
    var format = picked ? picked.value : 'Either is fine';

    var body = 'What I want to know more about:\n' + topic +
               '\n\nPreferred form: ' + format + '\n';

    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: 'blog_idea_sent', idea_format: format });

    window.location.href = 'mailto:support@growboost.pl' +
      '?subject=' + encodeURIComponent('GrowBoost - blog idea') +
      '&body=' + encodeURIComponent(body);
  });
})();
