/* growboost.pl - adres kontaktowy skladany dopiero w przegladarce.
   W zrodle strony nie ma ani ciagu "user@domena", ani "mailto:", wiec
   proste zbieraczki adresow nie maja czego dopasowac. Czesci siedza
   w atrybutach data-* zakodowane ROT13.

   Bez JavaScriptu zostaje tresc zapasowa w rodzaju
   "support (at) growboost.pl" - czytelna dla czlowieka i dla czytnika
   ekranu, ale nie dla wyrazenia regularnego szukajacego malpy. */
(function () {
  'use strict';

  function rot13(s) {
    return s.replace(/[a-zA-Z]/g, function (c) {
      var base = c <= 'Z' ? 65 : 97;
      return String.fromCharCode((c.charCodeAt(0) - base + 13) % 26 + base);
    });
  }

  function build() {
    var links = document.querySelectorAll('a.mail');
    for (var i = 0; i < links.length; i++) {
      var el = links[i];
      var u = el.getAttribute('data-u');
      var d = el.getAttribute('data-d');
      if (!u || !d) { continue; }

      var address = rot13(u) + String.fromCharCode(64) + rot13(d);
      el.setAttribute('href', 'mai' + 'lto:' + address + (el.getAttribute('data-s') ? '?subject=' + el.getAttribute('data-s') : ''));
      el.textContent = address;
      el.removeAttribute('data-u');
      el.removeAttribute('data-d');
      el.removeAttribute('data-s');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
