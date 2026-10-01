# Zasady pracy nad growboost.pl

Plik wczytywany automatycznie na starcie sesji w tym repo. Obowiazuja
takze zasady rozmowy z `4.5_store_feed/CLAUDE.md` (styl odpowiedzi,
fakty i pewnosc, kolejnosc w odpowiedzi) — tutaj jest to, co dotyczy
samej strony.

## Zakres: ktore repozytorium wolno zmieniac

- **`monkalemonka23/store-feed-legal` (ta strona) — TAK.** Tu powstaja
  commity i tu ida pushe.
- **`monkalemonka23/4.5_store_feed` (wtyczka) — TYLKO DO PODGLADU.**
  Czytac wolno: do weryfikacji tresci, cen, dokumentacji i linkow,
  ktore strona powtarza za aplikacja. **Nie commitowac, nie pushowac,
  nie proponowac zmian w plikach.** Zmiany w aplikacji robi operatorka
  w osobnym watku; commit z tej sesji wszedlby jej w droge.
  Ustalone 2026-10-01.
- Jesli w trakcie pracy nad strona wyjdzie blad po stronie aplikacji —
  **zglosic go w odpowiedzi**, nie poprawiac.

## Wdrozenie

- GitHub Pages serwuje z `main`. Praca idzie na galezi
  `claude/optimistic-keller-4jap2d`, operatorka scala przez GitHub
  (Compare → Create pull request → Merge). Nie ma lokalnego klonu.
- Po scaleniu uruchamia sie workflow "pages build and deployment".
  Zanim powiesz, ze cos jest na zywo, sprawdz, czy skonczyl sie
  sukcesem.
- **Po kazdej zmianie w `assets/*.css` lub `assets/*.js` podbic numer
  wersji w `?v=...` we wszystkich czterech stronach.** Nazwy plikow
  sie nie zmieniaja, wiec bez tego przegladarka i CDN serwuja stara
  kopie — to juz kilka razy wygladalo jak "zmiany nie weszly".
  To samo dotyczy podmienionego obrazka: zmienic nazwe pliku.

## Czego nie zmyslac

- Linkow, ktorych nie dostalas (kanal YouTube, listing App Store).
- Identyfikatorow pol Google Forms — `docs.google.com` jest
  zablokowany przez proxy tego srodowiska, nie da sie ich odczytac.
- Zawartosci portfolio na Adobe Stock — `stock.adobe.com` tez jest
  zablokowany.
- `growboost.pl` jest zablokowany, wiec stanu na zywo nie sprawdzisz
  sama; rozstrzyga log wdrozenia albo operatorka.

## Sprawdzenie przed zgloszeniem gotowosci

Lokalnie `python3 -m http.server 8899` w katalogu repo, potem Chromium
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, Playwright):

1. Struktura HTML: niezamkniete tagi, zduplikowane `id`, martwe
   kotwice, brakujace pliki, przeskoki w hierarchii naglowkow.
2. Kazdy blok `application/ld+json` musi sie parsowac.
3. axe-core (`pip install axe-core-python`), reguly
   `wcag2a wcag2aa wcag21a wcag21aa`, 4 strony x 2 szerokosci —
   **zero naruszen** to stan oczekiwany, nie cel.
4. Brak poziomego paska przewijania na 320/390/768/1024/1280/1440 px.
5. Przy zmianie wygladu: zrzut przed i po, porownanie piksel po
   pikselu (PIL `ImageChops`), a nie "wyglada tak samo".

## Tresc

- Strona i dokumentacja po angielsku. Odpowiedzi w czacie po polsku.
- Znaki edytorskie (poltrajki, polpauzy, cudzyslowy typograficzne,
  wielokropki) nie wchodza na strone — tylko ASCII. Zostaja `✓`
  (z ukryta etykieta tekstowa), `·`, `©` i polskie znaki w nazwach
  wlasnych.
- Adres kontaktowy nigdy nie stoi otwartym tekstem w zrodle: czesci
  siedza w `data-u`/`data-d` zakodowane ROT13, sklada je
  `assets/mail.js`. Dotyczy takze `.js`, `.md`, `llms.txt` i danych
  strukturalnych.
- Ceny i rabaty **przeliczac**, nie przepisywac. Stan na 2026-10-01:
  Starter $7.99/mies. lub $79.90/rok = rowno dziesiec rat, czyli dwa
  miesiace gratis, 17%. Zmiana ktorejkolwiek liczby uniewaznia oba
  sformulowania — sprawdzic rachunek od nowa.
- Cena, ktora sprzedawca realnie placi, ustawiana jest w Shopify
  Partner Dashboard (managed pricing). W kodzie aplikacji sa tylko
  napisy informacyjne.

## Pliki, o ktorych latwo zapomniec przy zmianie tresci

- `llms.txt` — fakty dla modeli jezykowych.
- `store-feed-what-s-new-app/store-feed-help.md` — kopia dokumentacji,
  ma byc zgodna z sekcja `#doc`.
- `sitemap.xml` — `lastmod`.
- Dane strukturalne: `SoftwareApplication`, `FAQPage`, `ItemList`,
  `BreadcrumbList`, `WebPage`.
