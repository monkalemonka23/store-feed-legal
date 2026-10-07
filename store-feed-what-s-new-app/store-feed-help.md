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
| Price | free, no time limit | $7.99 / month or $79.90 / year |
| Free trial | - | 14 days |
| New products | ✓ | ✓ |
| Blog posts | - | ✓ |
| Promotions and discount codes | - | ✓ |
| Number of entries in the widget | up to 5 | 5, 10 or 20 |
| Time window (last 7, 14 or 30 days) | ✓ | ✓ |
| Widget title | ✓ | ✓ |
| Corner style | ✓ | ✓ |
| Close button | ✓ | ✓ |
| Show or hide on desktop / tablet / mobile | ✓ | ✓ |
| Place it on any page, in header or footer | ✓ | ✓ |
| Automatic daily refresh + manual refresh | ✓ | ✓ |
| Accent color | - | ✓ |
| Icon style (Flat, 3D, Emoticon) | Emoticon only | ✓ |
| How the widget opens and its height | - | ✓ |
| Show only chosen collections and blogs | - | ✓ |
| Hide products with a chosen tag | - | ✓ |
| Store Feed icon in the widget footer | always shown | not shown |
| Your own footer text and link | - | ✓ |
| Statistics: views, clicks, click rate, by device | - | ✓ |

### 1.2 Changing your plan

Starter begins with a **14-day free trial**. Paying yearly ($79.90) costs the same
as ten monthly payments, so two months are free - 17% off.

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

### 2.2 Adding it yourself

1. Go to **Online Store > Themes > Customize**.
2. Open the page you want.
3. Click **Add section** and choose **Store Feed** under **Apps**.
4. Click **Save**.

If Store Feed is not on the list, your theme does not support app sections.
This is the case for some older themes.

### 2.3 Where it works best

- **As its own section on a page** - the most common choice.
- **In the header or footer** - then it appears on every page.
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

- Promotions must be **active** and must have **started within the chosen
  time window**.
- **Automatic discounts** appear automatically.
- **Discount codes** appear only when they are **available to all customers**.
- **To show a code that is limited to some customers**, add the tag `public`
  to that discount in Shopify. The code will then be shown to everyone who sees
  the widget.
- "Buy X, get Y" discounts show what to buy and what you get, with links.
- Products that are sold out are not listed in a promotion. If nothing in a
  promotion can be bought any more, the promotion is not shown.
- If a promotion has an end date, the widget shows it.

See also: 3.8 Discounts launched through Shopify Rollouts

### 3.4 When there are more updates than places

The number of entries is set in **Max entries** (Free: 5).

1. Promotions are picked first, then blog posts, then products.
2. Within each kind, the newest are picked.
3. The chosen entries are then shown **newest first**.

Example: 2 promotions, 3 blog posts and 6 new products, with 5 places - the
widget shows the 2 promotions and 3 blog posts, sorted by date.

### 3.5 On the page of a listed item

When a shopper is already on the page of a product or blog post from the list,
that entry is skipped and the next one takes its place. Promotions stay and are
marked **Viewing**.

### 3.6 Nothing new to show

If there is nothing new in the chosen time window, the widget stays hidden. You
can choose a longer window (30 days) in **Date range**.

### 3.7 Choosing what to include (Starter)

- **Collections** - show only products from the chosen collections.
- **Blogs** - show only posts from the chosen blogs.
- **Exclude products with tag** - products with any of these tags never
  appear (useful for items that are always on sale and are not really "new").

---

### 3.8 Discounts launched through Shopify Rollouts (Starter)

Since October 2026 a Shopify **Rollout** can include a discount, so a campaign
goes live together with your theme and checkout changes, or reaches only a share
of buyers as a test. Two things decide whether that discount belongs in the feed.

**Announce only a discount every buyer can use.** While a rollout is serving, the
discount's own status stops telling the whole story: it can read Scheduled or
Expired while the buyers one treatment reaches do get it, and read Active while
nobody gets it. Store Feed reads the discount, not the rollout, so it cannot tell
those cases apart. Treat a rollout discount as safe to announce only when the
rollout serves it to everyone - effective traffic allocation 100, with a single
treatment at 100 that activates the discount.

Running a discount on part of your traffic, or testing two offers against each
other? Keep it out of the feed until you take it to full traffic. The widget
would tell every visitor about an offer only some of them can use, and there is
no switch that hides one promotion.

**Nothing refreshes by itself.** A rollout starting or finishing is not sent to
Store Feed. The feed changes on its nightly refresh (6.1) or when you click
Refresh now (6.2).

So, on the day:

1. Set the rollout up in Shopify and start it.
2. Open Store Feed and click **Refresh now**.
3. Wait for the green message, then reload your store page (6.3).

Do the same when the rollout finishes, otherwise the widget keeps announcing the
offer until the nightly refresh.


## 4. Appearance: look and feel

### 4.1 Widget title

Shown at the top of the widget. You can use an emoji.

### 4.2 Accent color (Starter)

Used for labels ("Product", "Blog", "Promo"), the entry count and small
details. Text on labels switches between black and white automatically, so it
stays readable.

### 4.3 Icon style (Starter)

Flat, 3D or Emoticon. Free plan uses Emoticon.

### 4.4 Corner style

Sharp, Rounded or Pill.

### 4.5 How the widget opens and its height (Starter)

- **Open** - shoppers see the list straight away.
- **Collapsed** - only the title bar; shoppers open it with one tap.
- **Height when open** - how much of the screen the open widget may take.

A shopper's own choice (opening or closing the list) is remembered while they
browse your store.

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

## 5. Colors and background

### 5.1 Where the colors come from

You don't set a background for the widget. It takes the **background and text
colors of the section it sits in**, so it looks like part of your theme.

### 5.2 Changing the widget background

Change the colors of the section that holds the widget:

1. Go to **Online Store > Themes > Customize**.
2. Click the section where Store Feed is placed.
3. Change its **Color scheme** to one with the background you want.
4. Click **Save**.

The widget follows the new colors. If the text would be hard to read, it
switches to black or white text color on its own.

### 5.3 Section with a background image

If the section uses an image as its background, the widget uses the section's
**color scheme** background as a solid color, so the list stays readable. To
change it, change the section's color scheme (see 5.2).

### 5.4 Page with a gradient or image background

If the whole page has a gradient or image background, the widget stays
see-through so the background shows behind it.

---

## 6. Updates and changes

### 6.1 Automatic update

The list updates on its own every night (at 00:15 UTC).

### 6.2 Updating now

Click **Refresh now** in the app. You can do this once every 5 minutes. If it
was clicked recently, the button shows the time when it becomes available
again.

### 6.3 After changing settings

1. Click **Save**.
2. Click **Refresh now** - this sends your new settings to your store.
3. Reload your store page (Ctrl+F5 on Windows, Cmd+Shift+R on Mac).

Shoppers who are already browsing your shop may see the change up to 15 minutes later.

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

---

## 8. FAQ: Something doesn't look right

### 8.1 I can't see the widget on my store

1. Check that it is added to that page and not hidden (the app shows "Added"
   next to the page, not "Hidden", see 2.1).
2. Check **Visibility by device** (4.7) for the device you are using.
3. Check that there is something new in the time window (3.6).
4. If you clicked the close button, it stays hidden until you close the
   browser tab (4.6).
5. If it sits in a very narrow spot, move it to its own section (2.3).

### 8.2 A new product is missing

1. The product is **Active** and available on **Online Store** (3.1).
2. It was published within the time window (3.1).
3. It doesn't have an excluded tag and belongs to the chosen collections (3.7).
4. There are enough places - promotions and blog posts are picked first (3.4).
5. Click **Refresh now** (6.2).

### 8.3 A discount code is missing (Starter)

1. The discount is active and started within the time window.
2. It is available to all customers, or it has the tag `public` (3.3).
3. At least one of its products can still be bought (3.3).
4. Click **Refresh now** (6.2).

### 8.4 The background color doesn't match

The widget uses the colors of its section. Change the section's color scheme
(See: 5.2).

### 8.5 I changed the look and I don't see the changes

1. In the app, click **Save**.
2. Click **Refresh now**. If the button is locked, wait until the time shown
   on it (6.2).
3. Wait for the green message **"Feed refreshed - ... entries in your widget"**.
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

Shoppers who are already browsing your shop may see the change up to 15 minutes
later.

### 8.6 The widget repeats many times

It was added inside a product card or slider. Remove it there and add it as its
own section (2.3).

### 8.7 Store Feed is not on the list of sections

Your theme does not support app sections (2.2).

---

## 9. Contact

Email **support (at) growboost.pl** - we reply within 24 hours on business days.
Mention the section number from this guide if it relates to your question.
