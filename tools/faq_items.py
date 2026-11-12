# -*- coding: utf-8 -*-
"""Tresc sekcji #faq na stronie Store Feed.

Zrodlo odpowiedzi: docs/help/store-feed-help.md i docs/growboost-aktualizacja.txt
z repozytorium wtyczki. Kazda odpowiedz konczy sie odsylaczem do sekcji pomocy.
Kolejnosc listy = kolejnosc na stronie i w spisie tresci FAQ.
"""

FAQ = [
 ("q1", "Do I need to edit my theme code?",
  "No. Store Feed installs as a Shopify app block, so you place it from Theme Editor. Online Store 2.0 themes are supported (<a href=\"#s2-2\">2.2</a>)."),

 ("q22", "Can I see how it looks on my store before shoppers do?",
  "Yes. <strong>Add</strong> in the app opens the theme editor with Store Feed already in place, showing your own products in your own theme, and nothing changes on your store until you click <strong>Save</strong>. After Save the widget is on your store, and the entries it shows arrive with the next feed update: click <strong>Refresh now</strong> to send them straight away, or wait for the nightly one (<a href=\"#s2-1\">2.1</a>, <a href=\"#s6-1\">6.1</a>, <a href=\"#s6-2\">6.2</a>)."),

 ("q12", "Where on my store should I put the widget?",
  "<strong>The header is the best place</strong> - the widget then appears on every page, near the top, where shoppers look first. Page by page:</p> <ul> <li><strong>Home page:</strong> the header, or its own section near the top, so new visitors see the store is active.</li> <li><strong>Product pages:</strong> the header, or a section below the product details - best of all in the column with <strong>Add to cart</strong>, under the button, which is where <strong>Add</strong> in the app puts it. A promotion that covers the product is marked <strong>Viewing</strong> (<a href=\"#s3-5\">3.5</a>).</li> <li><strong>Collection pages:</strong> a section above or below the product grid.</li> <li><strong>Blog posts:</strong> a section below the article - a short way from reading to shopping.</li> <li><strong>Pages from a page builder app:</strong> landing pages built outside the theme editor are still part of your theme, so a widget in the header or footer shows on them too.</li> <li><strong>Checkout:</strong> not possible, Shopify doesn't allow app blocks there. A code added with <strong>Use code</strong> is already in the cart when the shopper gets to checkout (<a href=\"#s3-3-3\">3.3.3</a>).</li> </ul> <p>Full guidance: <a href=\"#s2-3\">2.3</a>."),

 ("q13", "Will it match my theme?",
  "Yes, with no settings to fill in. The widget takes its fonts from your theme's headings, product card titles and text, its colors from the section it sits in, and its width and spacing from your theme's content area. The widget title is always a little larger than the entry titles (<a href=\"#s4-9\">4.9</a>, <a href=\"#s5-1\">5.1</a>)."),

 ("q19", "What should I call the widget, and what can I put in the footer?",
  "A short title that says there is something new, in your store's voice - 2-4 words, so it fits on one line on a phone: \"What's New\", \"Fresh this week\", \"New &amp; on sale\", \"&#128293; Hot right now\". In the footer (Starter) put one more reason to buy or to come back, with a link where it helps: \"Free shipping over $50\", \"30-day free returns\", \"New arrivals every Friday\" (<a href=\"#s4-1\">4.1</a>, <a href=\"#s4-8\">4.8</a>)."),

 ("q14", "Which themes is it tested on?",
  "Horizon, Dawn, Savor, Craft, Ritual, Publisher, Heritage and Taste. It works with any Online Store 2.0 theme that supports app blocks, so a theme not on this list, or a customized one, will most likely work too. If something doesn't look right, write to us with the theme name, the page address and a screenshot: a fix in the app reaches every store (<a href=\"#s11-4\">11.4</a>)."),

 ("q20", "Does it work with Shopify Markets, B2B or a headless storefront?",
  "Markets and B2B: every shopper sees the same entries - the widget does not adjust the list to a market or to a B2B catalog, and discounts set for specific markets are left out. Amounts on promotion cards are converted to the shopper\u0027s currency with Shopify\u0027s exchange rate, with the currency code added, for example \"20.94 CAD off\". Translations: names and titles appear in your store\u0027s default language, also when you have translated them with Translate &amp; Adapt, and the widget title is one text for all languages. Right-to-left languages (Arabic, Hebrew, Persian, Urdu) are not tested. Headless storefronts (Hydrogen or your own front end): no, the widget is a block for Online Store themes (<a href=\"#s10\">10</a>, <a href=\"#s3-3-2\">3.3.2</a>, <a href=\"#s11-4\">11.4</a>)."),

 ("q21", "What happens when I switch themes?",
  "The widget belongs to the theme you added it to. After you publish another theme, the app shows its pages as not added yet - click <strong>Add</strong> again and the widget is back, with the same settings (<a href=\"#s2-1\">2.1</a>)."),

 ("q4", "Will it slow my store down?",
  "The widget comes built into your store\u0027s pages, so nothing has to be fetched to show it after the page loads, and its script starts only once the shopper moves, taps, scrolls or types. A copy below the first screen is prepared only when the shopper starts scrolling or it comes into view. The measured difference is in <a href=\"#measured\">Measured on a real store</a>. Every copy still adds to the page, so use 1-2 per page, 3 at most (<a href=\"#s9-4\">9.4</a>, <a href=\"#s2-4\">2.4</a>)."),

 ("q2", "Does it collect data about my customers?",
  "No. The app reads your products, blog articles, discounts and discount rollouts, and which of your theme's sections carry the widget. It requests no customer scopes and does no per-visitor tracking. Views and clicks are counted as daily totals per device type, never per visitor. The widget sets no cookies (<a href=\"#s9-1\">9.1</a>, <a href=\"#s9-2\">9.2</a>)."),

 ("q15", "Can search engines see the widget?",
  "Yes. The widget is part of your page's HTML, so its entries are ordinary links that search engines can follow. It also adds a short list of the entries in structured data, schema.org ItemList (<a href=\"#s9-6\">9.6</a>)."),

 ("q3", "How often does the feed refresh?",
  "Discounts and newly published products reach the widget on their own, usually within a few minutes. A discount with a start date in the future appears exactly when it starts, and one that ends shows that it has ended and leaves with the next update. New blog posts wait for the nightly update at 00:15 UTC - the app shows that time in your store\u0027s own time zone, under <strong>Refresh now</strong> - or for <strong>Refresh now</strong> itself; a post scheduled a day or more ahead appears at its publish time (<a href=\"#s6-1\">6.1</a>, <a href=\"#s6-2\">6.2</a>)."),

 ("q5", "Can customers close the widget?",
  "Yes, and it stays closed for the rest of their session (<a href=\"#s4-6\">4.6</a>)."),

 ("q6", "Can I put it in more than one place?",
  "Yes. Every copy shows the same list and the same settings. We recommend 1-2 widgets per page, 3 at most: a header or footer widget counts on every page, and each extra copy repeats the same entries and makes the page slower to load (<a href=\"#s2-4\">2.4</a>)."),

 ("q11", "Can shoppers apply a code without typing it?",
  "Yes. Every discount code in the widget has a <strong>Use code</strong> button that adds it to the cart. The <strong>Copy</strong> button stays for shoppers who prefer to paste the code at checkout (<a href=\"#s3-3-3\">3.3.3</a>)."),

 ("q8", "Does Store Feed work with Shopify discount rollouts?",
  "Yes. Store Feed only promotes discounts that every shopper gets. A discount that a rollout gives to only part of your traffic stays hidden until it reaches everyone. A discount that a rollout turns on for all traffic appears in the widget, and the widget updates automatically when a rollout changes (<a href=\"#s3-8\">3.8</a>)."),

 ("q16", "What happens if I uninstall the app?",
  "The widget disappears from your store together with the app, and you don't need to edit your theme. Shopify cancels a Starter subscription automatically. About 48 hours later Shopify asks apps to erase the store's data, and we then permanently delete your settings, the feed and the statistics. If that request never arrives, we delete everything ourselves 20 days after you uninstall (<a href=\"#s1-3\">1.3</a>, <a href=\"#s9-3\">9.3</a>)."),

 ("q17", "I run a large store. Will it keep up?",
  "Yes. The widget is part of your store's pages and Shopify serves it with them, so our servers are not involved in showing it and heavy traffic does not slow it down. The size of your catalog does not matter either: each update reads only the newest products from the time window, the newest posts and your active discounts (<a href=\"#s11-1\">11.1</a>)."),

 ("q18", "I have few new products. Is it still worth it?",
  "With few new products the list can be short or empty. Choose the 30-day time window and add blog posts and promotions (Starter) to keep it full. The Free plan has no time limit, so you can see how it looks on your own store before deciding (<a href=\"#s11-2\">11.2</a>)."),

 ("q9", "How are views and clicks counted?",
  "<strong>A view counts when the widget appears on the shopper's screen</strong> - at least its title bar - not when the page loads, so a widget lower down counts only once the shopper scrolls to it. One view per page, however many copies the page shows. <strong>A click</strong> counts once for an entry, a collection or product name on a promotion card, or <strong>Use code</strong>; <strong>Copy</strong> is not counted. Counts are sent only for shoppers who allow analytics in your store's customer privacy settings, and bots and crawlers are never counted. The widget sends them through your store's own address (the Shopify app proxy), signed by Shopify, so no one can add numbers to another store's statistics. Statistics are kept for 180 days and the app shows the last 90. On Starter the app also breaks the numbers down by widget setup - the title it showed, whether it started open or folded, and how many entries - and exports both views to CSV (<a href=\"#s7\">7</a>)."),

 ("q10", "My statistics stopped updating",
  "If you changed the app proxy address in <strong>Settings &gt; Apps and sales channels &gt; Store Feed &gt; App proxy &gt; Customize URL</strong>, change it back to <code>/apps/store-feed</code>. The widget sends its counts to that address (<a href=\"#s7\">7</a>)."),

 ("q7", "What does Starter cost, and can I try it first?",
  "$7.99 a month, or $79.99 a year - paying yearly saves $15.89 against twelve monthly payments, 17% off. Starter begins with a <strong>14-day free trial</strong>, so you can see the full feed on your own store before anything is charged. The Free plan has no time limit. Charges are billed in advance on your Shopify bill and are not refunded, also not for the unused part of a month or a year (<a href=\"#s1-1\">1.1</a>, <a href=\"#s1-3\">1.3</a>)."),

]


def items_html():
    out = []
    for qid, q, a in FAQ:
        out.append('  <div class="faq">')
        out.append('    <h3 id="%s">%s</h3>' % (qid, q))
        out.append('    <p>%s</p>' % a)
        out.append('  </div>')
    return '\n'.join(out)


def toc_html():
    return '\n'.join('          <li><a href="#%s">%s</a></li>' % (q[0], q[1])
                     for q in FAQ)
