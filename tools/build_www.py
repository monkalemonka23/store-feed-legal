# -*- coding: utf-8 -*-
"""Przebudowuje sekcje #doc i #faq oraz dane strukturalne na stronie projektu
Store Feed z pomocy w repozytorium wtyczki.

  python3 tools/build_www.py ../4.5_store_feed/docs/help/store-feed-help.md

Zmienia:
  store-feed-what-s-new-app/index.html      sekcje #doc i #faq, FAQPage, ItemList
  store-feed-what-s-new-app/store-feed-help.md   kopia pomocy (adres zaciemniony)

Tresc pytan FAQ jest w tools/faq_items.py i to ja sie edytuje recznie.
Pomoc pochodzi z wtyczki i NIE jest tu poprawiana: zmiany tresci zglasza sie
watkowi wtyczki.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_doc as B
import faq_items as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'store-feed-what-s-new-app', 'index.html')
HELP_COPY = os.path.join(ROOT, 'store-feed-what-s-new-app', 'store-feed-help.md')
URL = 'https://growboost.pl/store-feed-what-s-new-app/'

# Sekcja 8 (rozwiazywanie problemow) mieszka w #faq, 12 (Contact) w sekcji
# Contact strony; reszta w #doc.
DOC_SECS = ['1', '2', '3', '4', '5', '6', '7', '9', '10', '11']


def replace_block(text, start, end, new):
    i = text.index(start)
    j = text.index(end, i) + len(end)
    return text[:i] + new + text[j:]


def swap_jsonld(text, needle, new):
    i = text.index(needle)
    start = text.rindex('{', 0, i)
    return text[:start] + new + text[text.index('\n</script>', i):]


def plain(html):
    t = re.sub(r'</p>\s*<ul>', ' ', html)
    t = re.sub(r'</li>\s*<li>', ' ', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
    return re.sub(r'\s+\.', '.', re.sub(r'\s+', ' ', t).strip())


def main(help_path):
    raw = open(help_path, encoding='utf-8').read()
    secs = B.split_sections(raw)

    doc_body = '\n\n'.join(B.indent(B.convert(secs[k])) for k in DOC_SECS)
    faq8 = B.indent(B.convert(secs['8'])).replace('>8. FAQ: Something', '>8. Something')
    doc_toc = B.toc(secs, DOC_SECS)

    page = open(PAGE, encoding='utf-8').read()

    doc = (
        '  <section id="doc" class="doc" aria-labelledby="doc-h">\n'
        + page[page.index('  <h2 id="doc-h">'):page.index('  <nav class="toc toc--cols" aria-labelledby="doctoc-h">')]
        + '  <nav class="toc toc--cols" aria-labelledby="doctoc-h">\n'
        '    <h3 class="toc__h" id="doctoc-h">Documentation - contents</h3>\n'
        '    <ol>\n' + doc_toc + '\n    </ol>\n'
        '    <p class="toc__note">Troubleshooting is section 8, in the <a href="#faq">FAQ</a>'
        ' below. <a href="#toc-h">Back to the whole page</a>.</p>\n'
        '  </nav>\n\n' + doc_body + '\n\n  </section>')
    page = replace_block(page, '  <section id="doc" class="doc"',
                         '  </section>\n\n  <section id="faq"',
                         doc + '\n\n  <section id="faq"')

    faq_head = page[page.index('  <h2 id="faq-h">'):page.index('        <p class="toc__group">General questions</p>')]
    faq_tail = page[page.index('      <div>\n        <p class="toc__group"><a href="#s8">'):page.index('  <div class="faq">')]
    faq = ('  <section id="faq" class="doc" aria-labelledby="faq-h">\n' + faq_head
           + '        <p class="toc__group">General questions</p>\n        <ol>\n'
           + F.toc_html() + '\n        </ol>\n      </div>\n' + faq_tail
           + F.items_html() + '\n\n' + faq8 + '\n\n  </section>')
    page = replace_block(page, '  <section id="faq" class="doc"',
                         '  </section>\n\n  <section id="changelog"',
                         faq + '\n\n  <section id="changelog"')

    faq_ld = ('{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n'
              '  "mainEntity": [\n'
              + ',\n'.join('    { "@type": "Question", "name": %s,\n'
                           '      "acceptedAnswer": { "@type": "Answer", "text": %s } }'
                           % (json.dumps(q), json.dumps(plain(a)))
                           for _i, q, a in F.FAQ)
              + '\n  ]\n}')
    page = swap_jsonld(page, '"@type": "FAQPage"', faq_ld)

    rows, pos = [], 0
    for num, title in re.findall(r'^## (\d+)\. (.*)$', raw, re.M):
        if num == '12':
            continue
        pos += 1
        rows.append('    { "@type": "ListItem", "position": %d, "name": %s, "url": %s }'
                    % (pos, json.dumps('%s. %s' % (num, title.replace('FAQ: ', ''))),
                       json.dumps(URL + '#' + B.sid(num))))
    doc_ld = ('{\n  "@context": "https://schema.org",\n  "@type": "ItemList",\n'
              '  "name": "Store Feed documentation - sections",\n'
              '  "itemListOrder": "https://schema.org/ItemListOrderAscending",\n'
              '  "numberOfItems": %d,\n  "itemListElement": [\n' % pos
              + ',\n'.join(rows) + '\n  ]\n}')
    page = swap_jsonld(page, '"Store Feed documentation - sections"', doc_ld)

    open(PAGE, 'w', encoding='utf-8').write(page)

    # Kopia pomocy na stronie: adres kontaktowy nigdy otwartym tekstem.
    copy = raw.replace(
        'Email **support@growboost.pl**. We reply within 24 hours on business days.',
        'Email **support (at) growboost.pl** - we reply within 24 hours on business days.')
    assert '@growboost' not in copy, 'adres nadal otwartym tekstem'
    open(HELP_COPY, 'w', encoding='utf-8').write(copy)

    print('#doc: %d sekcji, #faq: %d pytan + sekcja 8, pomoc: %d wierszy'
          % (len(DOC_SECS), len(F.FAQ), copy.count('\n') + 1))


if __name__ == '__main__':
    main(sys.argv[1])
