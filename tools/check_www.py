# -*- coding: utf-8 -*-
"""Sprawdzenia strony przed zgloszeniem gotowosci (CLAUDE.md):
axe-core WCAG 2.1 A/AA na 4 stronach x 2 szerokosci, brak poziomego paska
na 6 szerokosciach, bledy w konsoli.

  python3 -m http.server 8899 --bind 127.0.0.1   (w katalogu repo)
  python3 tools/check_www.py [sciezka/do/chrome]
"""
import asyncio
import glob
import sys

from axe_core_python.async_playwright import Axe
from playwright.async_api import async_playwright

PAGES = ['/', '/store-feed-what-s-new-app/', '/privacy-policy/', '/terms/', '/404.html']
WIDTHS_AXE = [1280, 390]
WIDTHS_SCROLL = [320, 390, 768, 1024, 1280, 1440]
RULES = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']
BASE = 'http://127.0.0.1:8899'


def find_chrome():
    if len(sys.argv) > 1:
        return sys.argv[1]
    hits = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome'))
    if not hits:
        raise SystemExit('nie znalazlem przegladarki w /opt/pw-browsers')
    return hits[-1]


async def main():
    axe = Axe()
    bad = 0
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=find_chrome(), args=['--no-sandbox'])
        for path in PAGES:
            ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
            pg = await ctx.new_page()
            errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(BASE + path, wait_until='networkidle')
            for w in WIDTHS_AXE:
                await pg.set_viewport_size({'width': w, 'height': 900})
                v = (await axe.run(pg, options={'runOnly': {'type': 'tag', 'values': RULES}}))['violations']
                bad += len(v)
                print('axe  %-32s %5d px  naruszen: %d' % (path, w, len(v)))
                for x in v:
                    print('        [%s] %s (%d el.)' % (x['impact'], x['id'], len(x['nodes'])))
                    for n in x['nodes'][:2]:
                        print('          ', (n.get('html') or '')[:140])
            for w in WIDTHS_SCROLL:
                await pg.set_viewport_size({'width': w, 'height': 900})
                sw, cw = await pg.evaluate(
                    '() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]')
                if sw > cw + 1:
                    bad += 1
                    wide = await pg.evaluate(
                        "(w) => [...document.querySelectorAll('*')]"
                        ".filter(e => e.getBoundingClientRect().right > w + 1)"
                        ".slice(0,5).map(e => e.tagName + '.' + (e.className || '').toString().slice(0,40))", w)
                    print('SCROLL %-30s %5d px  %d > %d  %s' % (path, w, sw, cw, wide))
            # googletagmanager bywa odciety przez proxy srodowiska, to nie blad strony
            errs = [e for e in errs if 'googletagmanager' not in e and 'TUNNEL' not in e]
            if errs:
                bad += len(errs)
                print('KONSOLA %-29s %s' % (path, errs[:3]))
            await ctx.close()
        await b.close()
    print('\nSUMA problemow:', bad)
    return 1 if bad else 0


raise SystemExit(asyncio.run(main()))
