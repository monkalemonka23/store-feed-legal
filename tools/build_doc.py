# -*- coding: utf-8 -*-
"""Zamienia docs/help/store-feed-help.md (z repozytorium wtyczki) na HTML
sekcji #doc i #faq na stronie projektu Store Feed.

Uzycie:  python3 tools/build_www.py <sciezka/do/store-feed-help.md>
Ten plik robi sama zamiane Markdown -> HTML; sklejanie strony jest
w tools/build_www.py, a tresc pytan FAQ w tools/faq_items.py.

Konwencje strony, ktore tu odtwarzamy:
  ## N. Tytul      -> <h3 id="sN">
  ### N.M Tytul    -> <h4 id="sN-M">
  #### N.M.K Tytul -> <h5 id="sN-M-K">
  (3.4), (See: 5.2), (6.1, 6.2)  -> odsylacze do tych sekcji
  "Tip: ..."       -> <div class="note">
  "See also: 3.7 ..." -> <p class="seealso">
  sekcja 12 (Contact) nie jest czescia #doc: prowadzi do #contact
  zrodlo strony zostaje ASCII (znaki spoza ASCII jako encje liczbowe)
"""
import re
import markdown

REF = r'\d+(?:\.\d+[a-z]?)*'
PAREN = re.compile(r'\((See: |see )?(' + REF + r'(?:, ' + REF + r')*)\)')

YES = '<span aria-hidden="true">&#10003;</span><span class="sr-only">Included</span>'
NO = '<span aria-hidden="true">-</span><span class="sr-only">Not included</span>'
NA = '<span aria-hidden="true">-</span><span class="sr-only">Not applicable</span>'


def sid(num):
    if num == '12':
        return 'contact'
    return 's' + num.replace('.', '-')


def link_refs(text):
    def repl(m):
        pre = m.group(1) or ''
        nums = [x.strip() for x in m.group(2).split(',')]
        links = ', '.join('<a href="#%s">%s</a>' % (sid(n), n) for n in nums)
        return '(' + pre + links + ')'
    text = PAREN.sub(repl, text)
    # numer sekcji na koncu nawiasu po przecinku, np. "(..., 3.3.1)"
    text = re.sub(r', (' + REF + r')\)',
                  lambda m: ', <a href="#%s">%s</a>)' % (sid(m.group(1)), m.group(1)),
                  text)
    return text


def fix_table(m):
    t = m.group(0)
    t = t.replace('<table>', '<table class="tbl">')
    t = t.replace('<td>Yes</td>', '<td>' + YES + '</td>')
    t = t.replace('<td>No</td>', '<td>' + NO + '</td>')
    t = t.replace('<td>not applicable</td>', '<td>' + NA + '</td>')
    t = re.sub(r'<th></th>', '<th scope="col">Feature</th>', t)
    t = re.sub(r'<th>([^<]*)</th>', r'<th scope="col">\1</th>', t)
    t = re.sub(r'<tr>\s*(.*?)\s*</tr>',
               lambda x: '<tr>' + re.sub(r'>\s+<', '><', x.group(1)) + '</tr>',
               t, flags=re.S)
    t = re.sub(r'\n\s*<tr>', '\n      <tr>', t)
    t = t.replace('<thead>', '  <thead>').replace('</thead>', '  </thead>')
    t = t.replace('<tbody>', '  <tbody>').replace('</tbody>', '  </tbody>')
    t = re.sub(r'\n\s*\n', '\n', t)
    return ('  <div class="tblwrap" role="region" aria-labelledby="s1-1" tabindex="0">\n  '
            + t + '\n  </div>')


def convert(md_text):
    h = markdown.markdown(md_text, extensions=['tables'],
                          output_format='html5', tab_length=2)

    def head(m):
        lvl, num, title = int(m.group(1)), m.group(2), m.group(3)
        tag = {2: 'h3', 3: 'h4', 4: 'h5'}[lvl]
        label = num + '.' if lvl == 2 else num
        return '<%s id="%s">%s %s</%s>' % (tag, sid(num), label, title, tag)

    h = re.sub(r'<h([234])>(' + REF + r')\.? ([^<]*)</h\1>', head, h)
    h = re.sub(r'<table>.*?</table>', fix_table, h, flags=re.S)
    h = h.replace('<hr />', '').replace('<hr>', '')
    h = re.sub(r'<p>(Tip: .*?)</p>',
               lambda m: '<div class="note">\n    <p>' + m.group(1) + '</p>\n  </div>',
               h, flags=re.S)
    h = re.sub(r'<p>See also: (' + REF + r') ([^<]*)</p>',
               lambda m: '<p class="seealso">See also: <a href="#%s">%s %s</a></p>'
                         % (sid(m.group(1)), m.group(1), m.group(2)), h)
    h = link_refs(h)
    h = re.sub(r'\n{3,}', '\n', h)
    return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in h)


def split_sections(raw):
    """Zwraca {numer sekcji: tekst Markdown} dla sekcji '## N. ...'."""
    body = raw.split('\n## 1. Plans', 1)
    assert len(body) == 2, 'nie znalazlem "## 1. Plans"'
    parts = re.split(r'\n(?=## \d+\. )', '## 1. Plans' + body[1])
    out = {}
    for p in parts:
        m = re.match(r'## (\d+)\. ', p)
        assert m, p[:60]
        out[m.group(1)] = p.strip()
    return out


def indent(h):
    return '\n'.join(('  ' + l if l.strip() else l) for l in h.split('\n'))


def toc(sections, keys):
    out = []
    for k in keys:
        sec = sections[k]
        title = re.match(r'## \d+\. (.*)', sec).group(1)
        subs = re.findall(r'^### (' + REF + r'[a-z]?) (.*)$', sec, re.M)
        deeps = re.findall(r'^#### (' + REF + r') (.*)$', sec, re.M)
        out.append('      <li value="%s"><a href="#%s">%s</a>' % (k, sid(k), title))
        main = [(n, t) for n, t in subs if not re.match(r'^\d+\.\d+[a-z]$', n)]
        if main:
            out.append('        <ol>')
            for num, t in main:
                kids = [(n, tt) for n, tt in subs if re.match(re.escape(num) + r'[a-z]$', n)]
                kids += [(n, tt) for n, tt in deeps if n.startswith(num + '.')]
                if kids:
                    out.append('          <li><a href="#%s">%s</a>' % (sid(num), t))
                    out.append('            <ul>')
                    for kn, kt in kids:
                        out.append('              <li><a href="#%s">%s %s</a></li>'
                                   % (sid(kn), kn, kt))
                    out.append('            </ul>')
                    out.append('          </li>')
                else:
                    out.append('          <li><a href="#%s">%s</a></li>' % (sid(num), t))
            out.append('        </ol>')
        out.append('      </li>')
    return '\n'.join(out)
