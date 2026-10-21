<!-- Plain-text copy of https://growboost.pl/store-feed-what-s-new-app/#doc
     Kept in sync by hand with docs/help/store-feed-help.md in the app repo. -->

# Store Feed - Help Center

Store Feed shows a "What's new" list on your store: new products, blog posts
and active promotions, collected automatically. This guide explains how to set
it up and what to do when something doesn't look right.

Each section has a number (for example **6.2**). If you contact support, you can
simply point to it.

---

## 1. Plans

### 1.1 What each plan includes

| | Free | Starter |
|---|---|---|
| Price | free, no time limit | $7.99 / month or $79.99 / year |
| Free trial | not applicable | 14 days |
| New products | Yes | Yes |
| Blog posts | No | Yes |
| Promotions and discount codes | No | Yes |
| Number of entries in the widget | up to 6 | 6, 12 or 24 |
| Time window (last 7, 14 or 30 days) | Yes | Yes |
| Widget title | Yes | Yes |
| Corner style | Yes | Yes |
| Close button | Yes | Yes |
| Show or hide on desktop / tablet / mobile | Yes | Yes |
| Place it on any page, in header or footer | Yes | Yes |
| Automatic daily refresh + manual refresh | Yes | Yes |
| Accent colour | No | Yes |
| Product and blog images | No | Yes |
| Icon style (Flat, 3D, Emoticon) | Emoticon only | Yes |
| How the widget opens and its height | No | Yes |
| Show only chosen collections and blogs | No | Yes |
| Hide products with a chosen tag | No | Yes |
| Store Feed icon in the widget footer | always shown | not shown |
| Your own footer text and link | No | Yes |
| Statistics: views, clicks, click rate, by device | No | Yes |

### 1.2 Changing your plan

Starter begins with a **14-day free trial**. Twelve monthly payments come to
$95.88, so paying yearly ($79.99) saves $15.89 - 17% off.

1. Open the Store Feed app in your Shopify admin.
2. Click **Plans** (or **Change plan**) in the top right corner.
3. Choose a plan and confirm it on the Shopify page.

When you move to a lower plan, Shopify switches it at the end of your current
billing period. Until then you keep the features you paid for.

---

## 2. Adding Store Feed to your store

### 2.1 The quick way

1. Open the Store Feed app.
2. In **Add Store Feed to your storefront**, click **Add** next to the page
   where you want the widget (Home page, Product pages, Collection pages, and
   so on).
3. The theme editor opens with Store Feed already added. Drag it where you want
   it and click **Save**.

The app shows which pages already have the widget ("Added") and which copies
are hidden in the theme editor ("Hidden").

Next to **Add Store Feed to your storefront** the app shows whether the widget
is live: **Active on your store**, or **Not on your store yet**.

### 2.2 Adding it yourself

1. Go to **Online Store > Themes > Customize**.
2. Open the page you want.
3. Click **Add section** and choose **Store Feed** under **Apps**.
4. Click **Save**.

If Store Feed is not on the list, your theme does not support app sections.
This is the case for some older themes.

### 2.3 Where it works best

- **In the header (recommended)** - it appears on every page, near the top,
  where shoppers look first. After a shopper clicks an entry, the widget on
  the next page folds to its title bar (when it sits in the top half of the
  screen), so it never covers what they came to see. One tap opens it again.
- **As its own section on a page** - good for the home page or a collection.
- **In the footer** - it appears on every page, but fewer shoppers scroll
  that far.
- **Not inside a product card or a product slider.** There it is repeated for
  every product in the grid.
- **It needs at least 200 px of width.** In very narrow spots (for example the
  row of icons in a header) it stays hidden.

### 2.4 More than one place

You can add Store Feed in several places. Every copy shows the same list and
uses the same settings from the app.

---

## 3. What appears in the feed

### 3.1 Products

A product appears when it is:

- **Active** (not a draft or archived),
- **available on the Online Store sales channel**,
- **published within the chosen time window** (last 7, 14 or 30 days).

Tip: a product added through an import or an app is sometimes active but not
available on the Online Store channel. Open the product in Shopify, check
**Sales channels** and make sure **Online Store** is ticked.

See also: 3.7 Choosing what to include (Starter)

### 3.2 Blog posts (Starter)

Published blog posts from the chosen time window (last 7, 14 or 30 days).

See also: 3.7 Choosing what to include (Starter)

### 3.3 Promotions (Starter)

**Which promotions appear**

- Promotions must be **active**.
- Promotions that **started before the chosen time window** still appear while
  they run, but only in places left free by everything else (3.4).
- **Automatic discounts** appear automatically.
- **Discount codes** appear when they are **available to all customers**, or
  when you add the tag `public` to a code that is limited to some customers.
  A tagged code is shown to everyone who sees the widget.
- Products that are sold out are not listed in a promotion. If nothing in a
  promotion can be bought any more, the promotion is not shown.

**What the card shows**

- Every card starts with a short hook: for promotions the discount value
  (for example "15% off" or "Get 1 item free") in bold, for products "New
  product", for blog posts "New post". The name is the second line. If a
  discount code has no name of its own in Shopify, the card shows only the
  value, and the code stays in the code box.
- Promotions show their end date, or **No end date** when they have none. They
  do not show a start date: shoppers care when a deal ends, not when it began.
- When a promotion has an end date, the widget shows the date and time it ends.
  Each shopper sees it in their own time zone and in the date format they are
  used to (for example "Nov 30, 5:59 PM" in New York or "30 Nov, 22:59" in
  London). In the last 6 days it also counts down ("Ends in 3 days"). When
  3 days or fewer are left, the end date is shown in bold with a dot in your
  accent colour.
- How the date format is chosen: first from the shopper's browser, if it has
  the store language with a region (for example "en-GB" gives
  "30 Nov, 22:59"). Only when the browser has no such setting, the widget uses
  the country selected in your store (Shopify Markets), for example Spanish
  with Mexico gives "30 nov, 11:59 p.m.". So changing the country in your
  store changes the format only for shoppers whose browser has no regional
  setting for the store language. Some combinations look the same: English
  with Mexico uses the same format as English with the United States.
- "Buy X, get Y" discounts show what to buy and what you get, with links.
  When both come from the same collection, the widget shows it once, as
  "Buy and get from: Bars".
- A discount on selected variants of a product, for example only some
  colours, lists the product with those variants - "The Complete Snowboard
  (Ice, Dawn)" - and the link opens the product with the first of them
  selected.
- The widget shows the discount's terms: the amount, minimum purchase or
  quantity, one use per customer, the total number of uses, how many times it
  applies per order, and whether it can be combined with other discounts.
  The most useful terms come first (minimum purchase, where it applies,
  then usage limits and combinations). The discount value already shown in
  the hook is not repeated in the terms, and amounts drop empty cents
  ("$15 off", not "$15.00 off"). Terms that only repeat the collections or
  products listed on the card ("2 products") are left out, and general terms
  ("One-time purchase products", "For all countries") come last, after the
  discounts it can't be combined with. The first 2 lines are visible; they end
  after a whole term, never in the middle of a word. Collections and products
  take up to 2 lines too, with "and N more". Each card has one "more", after
  the first part that is cut: it opens the terms and the collections or
  products together, and "less" at the very end closes them. Opened terms,
  collections and products are shown as a list, one per line. "more" has a
  small arrow and no underline: it opens text in place, while underlined
  names lead to another page.

**Using the code**

- Automatic discounts (no code) show, where other cards have the code
  buttons, "Already applied in your cart" when the discount already applies
  in the shopper's cart, "Applies automatically once you meet the terms
  above" when it doesn't yet, or "Not applied: ... gives a bigger discount
  for this cart" when another discount it can't be combined with applies
  instead. The text follows the cart when it changes, also when the shopper
  adds or removes products in the theme's cart.
- In the terms, an automatic discount lists the other automatic discounts and
  the discount codes from the widget it can't be combined with, the same way
  a code lists the automatic discounts. When it can't be combined with any
  code from the widget, it says so in one sentence instead of listing them
  all. When it combines with fewer codes than it doesn't, it names only the
  codes it combines with, for example "Combines only with discount code
  SHIPUS3".
- **Use code** adds the code to the shopper's cart, so they don't have to
  type it at checkout. Codes already in the cart stay there. After the code is
  added, the button changes to **View cart** and opens the cart: the theme's
  cart drawer, or the cart page when the theme has none. Once the cart has
  been opened, with this button or from the theme, and has products in it,
  the button changes to **Check out** and takes the shopper to checkout. If
  the cart has been emptied in the meantime, the button goes back to
  **View cart** and opens the cart. The button keeps the same size for every
  label, so nothing on the card moves when it changes. The
  widget uses Shopify's built-in cart action, so an open cart drawer or cart
  section of the theme shows the new discount right away; themes Shopify
  doesn't recognise reload the page, and the message still shows. Shopify
  decides which codes apply, and the widget tells the shopper the result:
  - the code applies: "Code added to your cart.", plus which other codes
    still apply and which codes or automatic discounts stopped applying
    because they can't be combined with it;
  - another discount in the cart already applies and, by the settings of
    both discounts, can't be combined with this one: the shopper sees which
    one it is and that it gives the bigger discount (Shopify keeps the
    discount that saves more when two can't be combined);
  - 5 product or order codes already apply (Shopify's limit per order) and
    the new code can be combined with all of them: the widget doesn't add it,
    the button stays **Use code**, and the shopper is asked to remove one
    first. Codes can be removed at checkout;
  - shipping discount codes: the shipping discount shows at checkout, after
    the address is known. A code only for other countries than the shopper's
    market says which countries it is for;
  - a code for specific products when none of them is in the cart: the
    shopper is told that the code applies only to the products listed on the
    card, and the button changes to **Shop now**, which opens the page the
    card leads to;
  - the cart doesn't meet the discount's terms yet (for example it's
    empty): the code waits in the cart and applies once the cart meets them,
    and the button changes to **Shop now**. For "buy X, get Y" codes there
    is no button, only the message, because the widget can't tell whether X
    or Y is missing.

  If the cart doesn't return the code, or its end date has passed, the
  shopper is told the code isn't active anymore. If adding fails, the shopper
  is asked to use Copy instead. A code that is already in the cart shows
  **View cart** when the page loads - or **Shop now**, or no button, while it
  waits for the cart to meet its terms - and at the end of its terms, under
  "more", so nothing on the page moves: "This code is already in your cart.",
  plus the reason when it doesn't apply - another discount it can't be
  combined with, or a country it isn't for. When the shopper changes the
  products in the theme's cart, the widget reads the cart again and updates
  the buttons and these notes.
- In the terms, a discount code lists the store's automatic discounts it
  can't be combined with, and says that the store applies the one that
  saves more.
- **Copy** copies the code, for shoppers who prefer to paste it at checkout.
- Codes that contain a comma show only Copy (Shopify's cart can't take them
  from a button). The code is never shortened. The code and its buttons start
  under the card's icon and use the card's full width, so the card looks the
  same before and after the page finishes loading. When the code and the
  buttons don't fit side by side, the code goes above the buttons, and
  **Use code** and **Copy** stay together.
- Codes for selected customers only (a customer segment or a list of
  customers, shown because of the `public` tag) say "For selected customers
  only" in their terms. Shopify checks at checkout whether the shopper
  qualifies, so after **Use code** the shopper is told that the code is for
  selected customers and that checkout shows whether it applies.

**Naming discounts so the cards read well**

The widget shows the discount value ("2% off") on its own line above the name,
and reads the conditions from the discount's settings. Two habits make the
cards easier to read:

- Let the name say why or for whom, not how much, and leave thresholds out of
  it. "Review Reward", "Early Holiday Access" and "Welcome Savings" read
  better than "Review Reward: 2% off", "15% off Bars and Bites" or "10% off
  over $50", which repeat what the card already shows.
- Short codes are easier to read, and easier to type when copying fails:
  `SWEET2` works better than `EARLYACCESS15`. The code is never shortened on
  the card.

See also: 3.8 Discounts in Shopify Rollouts (Starter)

### 3.4 When there are more updates than places

The number of entries is set in **Max entries**: 6, 12 or 24 (Free: 6).
These numbers fill whole rows in both the 2- and 3-column layout. The widget
uses 2 columns from about 600 px of width and 3 from about 900 px.

1. Promotions are picked first, then blog posts, then products.
2. Within each kind, the newest are picked.
3. Promotions that started before the time window come last: they fill only
   the places that are still free.
4. The chosen entries are then shown **newest first**, read across the rows:
   the newest is first on the left, the next one to its right, and so on, row
   by row. Cards can have different heights; when the columns drift apart by
   more than about 60 px, the next row starts level again, leaving a small
   gap under the shorter cards, so the rows stay easy to read.
5. A promotion that already applies in the shopper's cart, an automatic
   discount or a code they added, is shown at the end of the list: the
   shopper already has it, so newer offers come first.

Example: 2 promotions, 3 blog posts and 6 new products, with 6 places, the
widget shows the 2 promotions, the 3 blog posts and the newest product,
sorted by date.

### 3.5 On the page of a listed item

When a shopper is already on the page of a product or blog post from the list,
that entry is skipped and the next one takes its place. Promotions stay, move
to the top of the list - unless they already apply in the cart, see 3.4 - and
are marked **Viewing**, under the discount value. For a "buy X, get Y"
promotion seen on the page of what the shopper gets, not of what they need to
buy, the badge says **Reward from this page**. On a product page the same goes
for promotions on a collection the product belongs to. A discount on the whole
store or on the order, with no products or collections of its own, is never
marked.

A promotion card leads to the page where the shopper finds what it applies to:
its collection, the biggest one when there are several, its product, or the
first of its products when there are several. A discount on the whole store or
on the order leads to all products, newest first.

### 3.6 Nothing new to show

If there is nothing new in the chosen time window and no promotion is running,
the widget stays hidden. You can choose a longer window (30 days) in
**Date range**.

### 3.7 Choosing what to include (Starter)

- **Collections** - show only products from the chosen collections.
- **Blogs** - show only posts from the chosen blogs.
- **Exclude products with tag** - products with any of these tags never
  appear (useful for items that are always on sale and are not really "new").

Your saved choices are shown as soon as the app opens. A collection or blog you
have since deleted from your store is marked **Removed from store**, so you can
untick it.

### 3.8 Discounts in Shopify Rollouts (Starter)

A Shopify **Rollout** can turn a discount on or off, and it can do that for only
a share of your traffic as a test.

Store Feed promotes only discounts that **every** shopper gets. A discount that
a rollout gives to part of your traffic stays out of the widget until it reaches
everyone. A discount that a rollout turns on for all traffic appears in the
widget.

You do not need to refresh anything: the widget updates on its own when a
rollout starts, changes or finishes.

---

## 4. Appearance: look and feel

### 4.1 Widget title

Shown at the top of the widget. You can use an emoji.

### 4.2 Accent colour (Starter)

Used for labels ("Product", "Blog", "Promo"), the entry count and small
details. Text on labels switches between black and white automatically, so it
stays readable.

Enter the colour as a hex code in the `#RRGGBB` format, for example `#7F77DD`.

### 4.3 Icon style (Starter)

Flat, 3D or Emoticon. Free plan uses Emoticon.

### 4.3a Product and blog images (Starter)

**Show product and blog images** (on by default): products and blog posts show
their main image, 64 by 64 px, instead of an icon. Entries without an image,
and promotions, keep the icon.

### 4.3b Language of the widget

Labels in the widget (Copy, Promo, Ends in..., dates, Viewing) follow your
store's language: English, Polish, German, French, Spanish (Latin America),
Italian, Dutch and Portuguese (Brazil). Other languages use English. Dates
and times follow the usual format of each language, for example
"18 oct 2026, 6:05 p.m." in Spanish. The widget title is your own text.
Discount terms come from Shopify and are shown in English.

See also: 3.3 Promotions (Starter), for where the regional date format comes
from

### 4.4 Corner style

Sharp, Rounded or Pill.

### 4.5 How the widget opens and its height (Starter)

- **Open** - shoppers see the list straight away.
- **Collapsed** - only the title bar; shoppers open it with one tap.
- **Height when open** - how much of the screen the open widget may take. When
  the list is longer, shoppers can scroll it inside the widget, or tap
  **Show all** below it to open the whole list. **Show less** brings it back
  to this height.

A shopper's own choice (opening or closing the list) is remembered while they
browse your store.

After a shopper clicks an entry, the widget on the page they land on starts
folded to its title bar if it sits in the top half of the screen. The list
does not cover the product or post they wanted to see, and one tap opens it.

### 4.6 Close button

Lets shoppers hide the widget. It stays hidden for them until they close the
browser tab.

### 4.7 Visibility by device

Show or hide the widget separately on desktop, tablet and mobile.

### 4.8 Footer

- **Free plan:** a small Store Feed icon at the bottom of the widget.
- **Starter:** no footer, or your own text (for example "Free shipping over
  $50"), optionally with a link. If the text is empty, nothing is shown.

---

## 5. Colours and background

### 5.1 Where the colours come from

You don't set a background for the widget. It takes the **background and text
colours of the section it sits in**, so it looks like part of your theme.

### 5.2 Changing the widget background

Change the colours of the section that holds the widget:

1. Go to **Online Store > Themes > Customize**.
2. Click the section where Store Feed is placed.
3. Change its **Color scheme** to one with the background you want.
4. Click **Save**.

The widget follows the new colours. If the text would be hard to read, it
switches to black or white text colour on its own.

### 5.3 Section with a background image

If the section uses an image as its background, the widget uses the section's
**colour scheme** background as a solid colour, so the list stays readable. To
change it, change the section's colour scheme (see 5.2).

### 5.4 Page with a gradient or image background

If the whole page has a gradient or image background, the widget stays
see-through so the background shows behind it.

---

## 6. Updates and changes

### 6.1 Automatic update

The list updates on its own every night (at 00:15 UTC). When you create,
change, turn off or delete a discount in Shopify, the widget updates on its
own a few seconds later.

### 6.2 Updating now

Click **Refresh now** in the app. You can do this once every 5 minutes. If it
was clicked recently, the button shows the time when it becomes available
again.

### 6.3 After changing settings

1. Click **Save** - either in the preview column or on the bar Shopify shows at
   the top when you have unsaved changes. The preview in the app now shows your
   real entries with the new settings (how many, from which dates, collections
   and blogs).
2. Saved settings reach your store with the nightly update. To send them
   now, click **Refresh now**.
3. Reload your store page (Ctrl+F5 on Windows, Cmd+Shift+R on Mac).

Shoppers see the change on the next page they open.

### 6.4 After changing your plan

Open the Store Feed app once after the change. The widget then updates to the
new plan by itself.

---

## 7. Analytics: Statistics (Starter)

- **Views** - how many times the widget was shown.
- **Clicks** - how many times shoppers clicked an entry.
- **Click rate (CTR)** - clicks divided by views.
- Figures by device (desktop, tablet, mobile), for the last 7, 30 or 90 days.

Statistics count the whole store together, not each copy of the widget
separately.

The widget sends its counts through your store's own address (the Shopify app
proxy), and Shopify signs every request, so no one can add numbers to another
store's statistics. Bots, crawlers and automated browsers are not counted.

If statistics stop updating: if you changed the app proxy address in
**Settings > Apps and sales channels > Store Feed > App proxy > Customize URL**,
change it back to `/apps/store-feed`. The widget sends its counts to that
address.

---

## 8. FAQ: Something doesn't look right

### 8.1 I can't see the widget on my store

1. Look at the badge next to **Add Store Feed to your storefront**. If it reads
   **Not on your store yet**, the widget has not been placed in your theme (2.1).
2. Check that it is added to that page and not hidden (the app shows "Added"
   next to the page, not "Hidden", see 2.1).
3. Check **Visibility by device** (4.7) for the device you are using.
4. Check that there is something new in the time window (3.6).
5. If you clicked the close button, it stays hidden until you close the
   browser tab (4.6).
6. If it sits in a very narrow spot, move it to its own section (2.3).

### 8.2 A new product is missing

1. The product is **Active** and available on **Online Store** (3.1).
2. It was published within the time window (3.1).
3. It doesn't have an excluded tag and belongs to the chosen collections (3.7).
4. There are enough places. Promotions and blog posts are picked first (3.4).
5. Click **Refresh now** (6.2).

### 8.3 A discount code is missing (Starter)

1. The discount is active. If it started before the time window, it shows only
   when there are free places left (3.4).
2. It is available to all customers, or it has the tag `public` (3.3).
3. At least one of its products can still be bought (3.3).
4. Click **Refresh now** (6.2).

### 8.4 The background colour doesn't match

The widget uses the colours of its section. Change the section's colour scheme
(See: 5.2).

### 8.5 I changed the look and I don't see the changes

1. In the app, click **Save**.
2. Click **Refresh now**. If the button is locked, wait until the time shown
   on it (6.2).
3. Wait for the green message **"Feed refreshed: N entries in your widget"**.
   Only then are your changes sent to your store. If you see a yellow message
   instead, try again in a few minutes.
4. Open your store page and reload it without the saved copy:
   - **Windows** (Chrome, Edge, Firefox): press **Ctrl + F5**
     (or **Ctrl + Shift + R**).
   - **Mac** (Chrome, Edge, Firefox): press **Cmd + Shift + R**.
   - **Mac** (Safari): press **Cmd + Option + R**.
5. Still the old look? Open your store in a private window:
   - Chrome and Edge: **Ctrl + Shift + N** (Windows), **Cmd + Shift + N** (Mac).
   - Firefox: **Ctrl + Shift + P** (Windows), **Cmd + Shift + P** (Mac).
   - Safari: **Cmd + Shift + N**.

Shoppers see the change on the next page they open.

### 8.6 The widget repeats many times

It was added inside a product card or slider. Remove it there and add it as its
own section (2.3).

### 8.7 Store Feed is not on the list of sections

Your theme does not support app sections (2.2).

---

## 9. Contact

Email **support (at) growboost.pl** - we reply within 24 hours on business days.
Mention the section number from this guide if it relates to your question.
