#!/usr/bin/env python3
"""Builds the Dynamic Horse Solutions pages from one frame, so the menu and footer never drift. Run: python3 build.py"""
import io

RELEASE = "release.html"   # the Dynamic Horse-branded release on this site (Angel 14:14); the short link still serves the old staging page
WEBHOOK = "https://n8n.aztechsol.com/webhook/dhs-registration"
JO_EMAIL = "az.horsesensetraining@gmail.com"
SITE = "https://dynamichorsesolutions.com"   # share images and og:url need the full address
NAV = [("index.html", "Home"), ("classes.html", "Classes"), ("about.html", "About"), ("contact.html", "Contact")]
CLASS_PAGES = ("part-1.html", "part-2.html", "part-3.html")   # the Classes item stays current on these

def frame(slug, title, desc, body):
    link = lambda h, t: f'<a href="{h}"{" class=\"cta\"" if h == "classes.html" else ""}{" aria-current=\"page\"" if h == slug or (h == "classes.html" and slug in CLASS_PAGES) else ""}>{t}</a>'
    cta = [x for x in NAV if x[0] == "classes.html"]; rest = [x for x in NAV if x[0] != "classes.html"]
    wide = "".join(link(*x) for x in rest + cta)     # Angel 14:50: Classes far right on desktop
    narrow = "".join(link(*x) for x in cta + rest)   # and first in the phone menu
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/favicon-512.png" type="image/png">
<link rel="apple-touch-icon" href="assets/favicon-512.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dynamic Horse Solutions">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{"" if slug == "index.html" else slug}">
<meta property="og:image" content="{SITE}/assets/og/{slug[:-5]}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/assets/og/{slug[:-5]}.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script defer src="https://stats.aztechsol.com/script.js" data-website-id="718dd775-101a-4a25-a182-e886c37360be" data-domains="dynamichorsesolutions.com"></script>
</head>
<body>
<header class="top">
  <a class="brand" href="index.html" aria-label="Dynamic Horse Solutions, home"><img class="wordmark lockup" src="assets/lockup.svg" alt="Dynamic Horse Solutions" width="2723" height="400"></a>
  <nav class="wide" aria-label="Menu">{wide}</nav>
  <details class="narrow"><summary aria-label="Menu"><span></span><span></span><span></span></summary>
    <nav aria-label="Menu">{narrow}</nav></details>
</header>
<main>
{body}
</main>
<footer>
  <img src="assets/logo.svg" alt="Dynamic Horse Solutions" width="140" height="140">
  <p><a href="classes.html">Classes</a> · <a href="contact.html">Contact</a></p>
  <p class="soon">Coming soon: <a href="podcast.html">Podcast</a> · <a href="book.html">Book</a> · <a href="videos.html">Video series</a></p>
  <p>© 2026 Dynamic Horse Solutions · Tucson, Arizona</p>
  <p class="credit">Photo: <a href="https://commons.wikimedia.org/wiki/File:NewForestPonies_sunrise.jpg">Joana Kruse</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>, via Wikimedia Commons.</p>
</footer>
</body>
</html>
"""

CLASSES_DATA = [
    dict(slug="part-1", num="Part I", title="The Hind End Junction", parts="Pelvis • Sacrum • Lumbar Spine",
         img="class-1-hind-end", when="Saturday, November 7, 2026", time="9 AM – 1 PM", status="booked",
         blurb="The bones of the pelvis, sacrum and lumbar spine, the sacroiliac and lumbosacral joints, the hip, and the medial gluteal muscle that drives impulsion and lifts the back."),
    dict(slug="part-2", num="Part II", title="The Thoracic Sling", parts="Chest • Shoulder • Forelimb",
         img="class-2-thoracic-sling", when="Saturday, February 27, 2027", time="time to be announced", status="open",
         blurb="The thoracic sling: the muscles that carry the horse's chest between its front legs, and how they lift the front end into a weight bearing posture."),
    dict(slug="part-3", num="Part III", title="Poll &amp; TMJ", parts="Poll • Jaw • Upper Neck",
         img="class-3-poll-tmj", when="April 2027", time="date to be announced", status="open",
         blurb="The poll and the temporomandibular joint, where the head meets the spine, and how the jaw and upper neck shape the whole horse's way of going."),
]
TURNSTILE_SITEKEY = "0x4AAAAAAF2xBfE9am2PxE1r"   # Angel's widget, 2026-11-06 14:14; the secret lives only in n8n (credential 4fN01sgazguMbgJ3)
TURNSTILE_JS = '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>'
PRICE_TOTAL, PRICE_DEPOSIT = 220, 110   # Angel 2026-11-06 13:37: an unscheduled class is $220, and $110 holds the place (50%)
WHERE = "Copper Horse Ranch · 9887 N Camino de Oeste · Tucson, AZ"
INCL = "Lecture · demonstration · guided skeleton exploration · workbook included"

def class_card(c):
    badge = '<span class="badge full">Fully booked</span>' if c["status"] == "booked" else f'<span class="badge open">Registration open · ${PRICE_DEPOSIT} deposit</span>'
    return f'''<a class="class-card" href="{c["slug"]}.html">
  <picture><source media="(min-width:760px)" srcset="assets/{c["img"].split("-")[0]}-{c["img"].split("-")[1]}-card.webp"><img src="assets/{c["img"]}.webp" alt="" width="1200" height="900" loading="lazy"></picture>
  <div class="cc-body">
    <p class="num">{c["num"]}</p>
    <h3>{c["title"]}</h3>
    <p class="when">{c["when"]}</p>
    {badge}
    <span class="more">View the class →</span>
  </div>
</a>'''

CLASS_GRID = '<div class="class-grid">' + "".join(class_card(c) for c in CLASSES_DATA) + '</div>'

def reg_form(c):
    return f'''
<section class="form-wrap" id="register">
  <h2>Register for {c["num"]}</h2>
  <div class="deposit">
    <p><b>${PRICE_TOTAL}</b> for the class. A <b>${PRICE_DEPOSIT} deposit</b> (50%) holds your place now; the balance is due before the class.</p>
    <p class="small">Jo Ann confirms your place and sends deposit details by email or text. Deposits are paid by Zelle or PayPal.</p>
  </div>
  <form id="reg" class="reg" novalidate>
    <input type="hidden" name="class" value="{c["slug"]}">
    <input type="hidden" name="class_label" value="{c["num"]} · {c["title"].replace("&amp;","&")} · {c["when"]} · ${PRICE_TOTAL}, ${PRICE_DEPOSIT} deposit">
    <label>Full name <input name="full_name" autocomplete="name" required></label>
    <div class="two">
      <label>Email <input name="email" type="email" autocomplete="email" required></label>
      <label>Phone <input name="phone" type="tel" autocomplete="tel" required></label>
    </div>
    <div class="two">
      <label>People attending <input name="people" type="number" min="1" max="20" value="1" required></label>
    </div>
    <fieldset>
      <legend>How you'll pay the deposit</legend>
      <label class="inline"><input type="radio" name="payment" value="Zelle" checked> Zelle</label>
      <label class="inline"><input type="radio" name="payment" value="PayPal"> PayPal</label>
    </fieldset>
    <label>Anything Jo Ann should know <span class="opt">(optional)</span> <textarea name="notes" rows="3"></textarea></label>
    <div class="cf-turnstile" data-sitekey="{TURNSTILE_SITEKEY}" data-action="register" data-theme="light"></div>
    <button class="btn" type="submit">Hold my place</button>
    <p id="msg" class="msg" role="status" aria-live="polite"></p>
  </form>
</section>
{TURNSTILE_JS}
<script>
(function(){{
  var f=document.getElementById("reg"), msg=document.getElementById("msg");
  function mailto(d){{
    var body="Registration\\n\\nClass: "+d.class_label+"\\nName: "+d.full_name+"\\nEmail: "+d.email+"\\nPhone: "+d.phone+"\\nPeople: "+d.people+"\\nDeposit by: "+d.payment+"\\nNotes: "+(d.notes||"");
    return "mailto:{JO_EMAIL}?subject="+encodeURIComponent("Registration: {c["num"]} · "+d.full_name)+"&body="+encodeURIComponent(body);
  }}
  f.addEventListener("submit",function(e){{
    e.preventDefault();
    if(!f.checkValidity()){{ f.reportValidity(); return; }}
    var d=Object.fromEntries(new FormData(f).entries()); d.turnstile_token=d["cf-turnstile-response"]||""; delete d["cf-turnstile-response"];
    if(!d.turnstile_token){{ msg.textContent="One moment: the security check is still loading. Please try again in a few seconds."; return; }}
    d.deposit={PRICE_DEPOSIT}; d.total={PRICE_TOTAL}; d.submitted_at=new Date().toISOString(); d.page=location.href;
    var btn=f.querySelector("button"); btn.disabled=true; msg.textContent="Sending…";
    fetch("{WEBHOOK}",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(d)}})
      .then(function(r){{ return r.json().catch(function(){{return {{}}}}).then(function(j){{ return {{r:r,j:j}}; }}); }})
      .then(function(x){{ var r=x.r, j=x.j;
        if(r.status===400 && j && j.error){{ msg.textContent=j.error; if(window.turnstile) turnstile.reset(); return; }}
        if(!r.ok || !j.ok) throw new Error(r.status); f.reset(); if(window.turnstile) turnstile.reset(); var t="Hi Jo Ann, this is "+d.full_name+". I just registered for "+d.class_label+" ("+d.people+" attending) and will send my $"+d.deposit+" deposit by "+d.payment+". My email is "+d.email+".";
        msg.innerHTML="<b>Thank you, your place is held.</b> Send your $"+d.deposit+" deposit to Jo Ann by Zelle or PayPal, then let her know it's on its way:<br><a class=\\"btn\\" href=\\"sms:+15204038200?&body="+encodeURIComponent(t)+"\\">Text Jo Ann</a>"; }})
      .catch(function(){{ msg.innerHTML="Your email app is opening with your registration filled in. Press send and it goes to Jo Ann. If nothing opens, email <a href=\\""+mailto(d)+"\\">{JO_EMAIL}</a> or call 520-403-8200."; location.href=mailto(d); }})
      .finally(function(){{ btn.disabled=false; }});
  }});
}})();
</script>
'''

def class_page(c):
    hero = f'''<section class="class-hero" style="background-image:linear-gradient(180deg,rgba(22,38,43,.35),rgba(22,38,43,.85)),url(assets/{c["img"]}.webp)">
  <div class="ch-copy">
    <p class="num">{c["num"]} · Equine Biomechanics</p>
    <h1>{c["title"]}</h1>
    <p class="parts">{c["parts"]}</p>
  </div>
</section>'''
    facts = f'''<div class="facts">
    <p class="when">{c["when"]}<br><span>{c["time"]}</span></p>
    <p class="where">{WHERE}</p>
    <p class="incl">{INCL}</p>
  </div>'''
    if c["status"] == "booked":
        body = f'''
<section class="class-detail">
  <p class="badge full big">Fully booked</p>
  <p class="lede">{c["blurb"]}</p>
  {facts}
  <p class="price">$110 <span>introductory price · half the ${PRICE_TOTAL} rate of the classes that follow</span></p>
  <div class="extras">
    <article class="extra">
      <h3>The Media Release</h3>
      <p>This class is being filmed for the online series. If you're attending, please sign the consent to be filmed before you arrive. It takes a minute on your phone.</p>
      <p><a class="btn" href="{RELEASE}">Sign the media release</a></p>
    </article>
    <article class="extra">
      <h3>The Workbook</h3>
      <p>The class workbook, <em>The Hind End Junction</em>: posture, the anatomy of the hind end, and room for your notes.</p>
      <p><a class="btn ghost" href="assets/hind-end-junction-workbook.pdf" download>Download the workbook (PDF)</a></p>
    </article>
  </div>
  <p class="note">Missed this one? It's being filmed for the <a href="videos.html">online series</a>, and Parts <a href="part-2.html">II</a> and <a href="part-3.html">III</a> are open for registration.</p>
</section>'''
    else:
        body = f'''
<section class="class-detail">
  <p class="badge open big">Registration open</p>
  <p class="lede">{c["blurb"]}</p>
  {facts}
  <p class="price">${PRICE_TOTAL} <span>per person · ${PRICE_DEPOSIT} deposit holds your place</span></p>
  <p><a class="btn" href="#register">Register with a ${PRICE_DEPOSIT} deposit</a></p>
</section>
{reg_form(c)}'''
    return hero + body

# Placeholder pages with a "tell me when it's out" form (Angel, 2026-11-06 16:30). The words are Lena's until Vanessa and Jo Ann send theirs.
NOTIFY = "https://n8n.aztechsol.com/webhook/dhs-notify"
COMING_DATA = [
    dict(slug="podcast", label="The Podcast", img="teachers.jpg", eyebrow="Coming soon · Listen",
         title="The Dynamic Horse Podcast", sub="Conversations on structure, posture and function",
         blurb="Jo Ann and Vanessa talk through how a horse is built and how it moves: what they see in the clinic, the questions riders bring them, and the small changes that make a big difference to a horse's comfort and way of going.",
         ask="Leave your email and we'll let you know when the first episode is out."),
    dict(slug="book", label="The Book", img="class-2-thoracic-sling.webp", eyebrow="Coming soon · Read",
         title="The Book", sub="Equine Biomechanics, from the skeleton out",
         blurb="Everything the series teaches, in one place: the hind end, the thoracic sling, the poll and jaw, and how they work together, with drawings from the classes and room for your own notes.",
         ask="Leave your email and we'll let you know when the book is ready."),
    dict(slug="videos", label="The Video Series", img="hero-sunrise.webp", eyebrow="Coming soon · Watch",
         title="The Video Series", sub="Equine Biomechanics, online and at your own pace",
         blurb="Each part of the series is being filmed at the ranch, starting with The Hind End Junction on November 7, so you can learn at your own pace and come back to it with your own horse.",
         ask="Leave your email and we'll let you know when the first part is online."),
]

def coming_page(x):
    return f'''<section class="class-hero" style="background-image:linear-gradient(180deg,rgba(22,38,43,.35),rgba(22,38,43,.85)),url(assets/{x["img"]})">
  <div class="ch-copy">
    <p class="num">{x["eyebrow"]}</p>
    <h1>{x["title"]}</h1>
    <p class="parts">{x["sub"]}</p>
  </div>
</section>
<section class="class-detail">
  <p class="badge open big">Coming soon</p>
  <p class="lede">{x["blurb"]}</p>
</section>
<section class="form-wrap" id="notify">
  <h2>Be the first to know</h2>
  <p>{x["ask"]} One email when it's ready, nothing else.</p>
  <form id="notify-form" class="reg" novalidate>
    <input type="hidden" name="interest" value="{x["slug"]}">
    <div class="two">
      <label>Name <input name="name" autocomplete="name"></label>
      <label>Email <input name="email" type="email" autocomplete="email" required></label>
    </div>
    <input name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-5000px">
    <div class="cf-turnstile" data-sitekey="{TURNSTILE_SITEKEY}" data-action="notify" data-theme="light"></div>
    <button class="btn" type="submit">Notify me</button>
    <p id="msg" class="msg" role="status" aria-live="polite"></p>
  </form>
</section>
{TURNSTILE_JS}
<script>
(function(){{
  var f=document.getElementById("notify-form"), msg=document.getElementById("msg");
  f.addEventListener("submit",function(e){{
    e.preventDefault();
    if(!f.checkValidity()){{ f.reportValidity(); return; }}
    var d=Object.fromEntries(new FormData(f).entries()); d.turnstile_token=d["cf-turnstile-response"]||""; delete d["cf-turnstile-response"];
    if(!d.turnstile_token){{ msg.textContent="One moment: the security check is still loading. Please try again in a few seconds."; return; }}
    d.submitted_at=new Date().toISOString(); d.page=location.href;
    var btn=f.querySelector("button"); btn.disabled=true; msg.textContent="Sending…";
    fetch("{NOTIFY}",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(d)}})
      .then(function(r){{ return r.json().catch(function(){{return {{}}}}).then(function(j){{ return {{r:r,j:j}}; }}); }})
      .then(function(x){{ var r=x.r, j=x.j;
        if(r.status===400 && j && j.error){{ msg.textContent=j.error; if(window.turnstile) turnstile.reset(); return; }}
        if(!r.ok || !j.ok) throw new Error(r.status);
        f.reset(); if(window.turnstile) turnstile.reset(); msg.innerHTML="<b>Thank you, you're on the list.</b> We'll email you when it's ready.";
      }})
      .catch(function(){{ msg.innerHTML="That didn't go through. Please try again, or email <a href=\\"mailto:{JO_EMAIL}\\">{JO_EMAIL}</a> and we'll add you."; if(window.turnstile) turnstile.reset(); }})
      .finally(function(){{ btn.disabled=false; }});
  }});
}})();
</script>
'''

HOME = f"""
<section class="hero-slider single" aria-label="Equine Biomechanics">
  <div class="slides">
    <img class="slide is-on" src="assets/hero-sunrise-1100.webp" srcset="assets/hero-sunrise-1100.webp 1100w, assets/hero-sunrise.webp 2200w" sizes="100vw" alt="Two ponies walking through morning mist at sunrise" style="object-position:38% 78%">
  </div>
  <div class="hero-copy">
    <p class="eyebrow">A three-part educational series for horse owners &amp; riders</p>
    <h1>Equine Biomechanics</h1>
    <p class="triad"><span>Structure</span><i>•</i><span>Posture</span><i>•</i><span>Function</span></p>
    <p class="hero-actions"><a class="btn" href="classes.html">See the classes</a><a class="btn light" href="about.html">Meet the teachers</a></p>
  </div>
</section>

<section class="intro">
  <img class="logo" src="assets/logo.svg" alt="Dynamic Horse Solutions" width="240" height="240">
  <p class="lede">Explore the relationship between structure, posture and function through lecture, demonstration and guided exploration of a real equine skeleton. Learn to recognize healthy weight-bearing posture, identify postural imbalances, and better tell patterns of posture and restriction apart from those that may point to true discomfort.</p>
  <ul class="format"><li>Lecture</li><li>Demonstration</li><li>Guided skeleton exploration</li><li>Workbook included</li></ul>
</section>

<section class="series">
  <h2>The Complete Series</h2>
  {CLASS_GRID}
</section>

<section class="teaser">
  <img class="chase-oval" src="assets/chase.jpg" alt="Chase, a bay Thoroughbred with a white star" width="296" height="424">
  <div>
    <h2>Taught by two horsewomen, and by Chase</h2>
    <p>Jo Ann Lewis and Vanessa Helvey teach together, with the skeleton of Chase, an off-the-track Thoroughbred they both knew, on the table in front of you.</p>
    <p><a href="about.html">Meet the teachers →</a></p>
  </div>
</section>

<section id="videos" class="videos">
  <img class="mark" src="assets/mark-white.svg" alt="" width="64" height="64">
  <h2>Watch the Series Online</h2>
  <p>Each part of the series will be available here as video, so you can learn at your own pace and come back to it with your own horse.</p>
  <p class="status">Coming soon</p>
  <p><a class="btn ghost light" href="videos.html">Notify me</a></p>
  <p class="soon-links">Also on the way: <a href="podcast.html">the podcast</a> and <a href="book.html">the book</a>.</p>
</section>
"""

CLASSES = f"""
<section class="page-head">
  <h1>Classes</h1>
  <p class="lede center">Equine Biomechanics: Structure · Posture · Function. Three parts, each a morning at the ranch with a real equine skeleton.</p>
</section>
<section class="series">
  {CLASS_GRID}
  <p class="note">Attending Saturday? Please <a href="{RELEASE}">sign the media release</a> before you arrive.</p>
</section>
"""

REGISTER = """
<section class="page-head">
  <h1>Register</h1>
  <p class="lede center">Registration is on each class's own page. <a href="classes.html">Choose a class →</a></p>
</section>
<script>location.replace("classes.html");</script>
"""

ABOUT = """
<section class="page-head">
  <h1>About</h1>
  <p class="lede center">Dynamic Horse Solutions is the shared home of the teaching Jo Ann Lewis and Vanessa Helvey do together, in person in Tucson and on video for everyone who can't make it to the ranch.</p>
</section>

<section id="teachers" class="teachers">
  <h2>The Teachers</h2>
  <img class="duo" src="assets/teachers.jpg" alt="Vanessa Helvey and Jo Ann Lewis in the arena at Copper Horse Ranch" width="732" height="376">
  <div class="pair">
    <article>
      <h3>Jo Ann Lewis, BSc</h3>
      <p>Nineteen years as an equine professional, with an emphasis on postural correctness for horse and rider.</p>
    </article>
    <article>
      <h3>Vanessa Helvey, BSc</h3>
      <p>Equine Osteopath. Masterson Method<sup>®</sup> Certified Practitioner &amp; Instructor.</p>
    </article>
  </div>
</section>

<section id="chase" class="chase">
  <img src="assets/chase.jpg" alt="Chase, a bay Thoroughbred with a white star" width="296" height="424">
  <div>
    <h2>Meet Chase, our teacher</h2>
    <p>Chase was an off-the-track Thoroughbred known to both instructors during his life. Today, his skeleton offers a rare chance to explore equine anatomy in three dimensions, and to understand how structure shapes the living, moving horse.</p>
  </div>
</section>

<section class="mark-story">
  <img src="assets/mark.svg" alt="" width="120" height="120">
  <p class="why">A horse resting on an open human hand, because, in Jo Ann's words, <em>"the solution comes with human support."</em></p>
</section>
"""

CONTACT = f"""
<section class="page-head">
  <h1>Contact</h1>
  <p class="lede center">For upcoming dates, the online series, or to hold a place in a class.</p>
</section>
<section class="contact">
  <div class="card">
    <p class="who">Jo Ann Lewis</p>
    <p><a href="tel:+15204038200">520-403-8200</a></p>
    <p><a href="mailto:{JO_EMAIL}">{JO_EMAIL}</a></p>
  </div>
  <p class="place">Classes are held at Copper Horse Ranch<br>9887 N Camino de Oeste · Tucson, AZ</p>
  <p><a class="btn" href="classes.html">See the classes</a></p>
</section>
"""

PAGES = [
    ("index.html", "Dynamic Horse Solutions — Equine Biomechanics", "Equine Biomechanics: Structure · Posture · Function. A three-part series for horse owners and riders in Tucson, taught by Jo Ann Lewis and Vanessa Helvey.", HOME),
    ("classes.html", "Classes — Dynamic Horse Solutions", "Part I, The Hind End Junction, Saturday November 7, 2026 at Copper Horse Ranch, Tucson; then Parts II and III in 2027.", CLASSES),
    *[(f'{c["slug"]}.html', f'{c["num"]}: {c["title"].replace("&amp;", "&")} — Dynamic Horse Solutions', f'{c["num"]} of Equine Biomechanics, {c["title"].replace("&amp;", "&")}, at Copper Horse Ranch in Tucson.', class_page(c)) for c in CLASSES_DATA],
    ("register.html", "Register — Dynamic Horse Solutions", "Register for an Equine Biomechanics class with Jo Ann Lewis and Vanessa Helvey.", REGISTER),
    ("about.html", "About — Dynamic Horse Solutions", "Jo Ann Lewis, Vanessa Helvey and Chase, the teachers of Equine Biomechanics.", ABOUT),
    ("contact.html", "Contact — Dynamic Horse Solutions", "Reach Jo Ann Lewis about classes, dates and the online series.", CONTACT),
    *[(f'{x["slug"]}.html', f'{x["title"]} — Dynamic Horse Solutions', f'{x["blurb"].split(":")[0].split(",")[0]}. Coming soon; sign up to be told when it is out.', coming_page(x)) for x in COMING_DATA],
]
for slug, title, desc, body in PAGES:
    io.open(slug, "w", encoding="utf-8").write(frame(slug, title, desc, body))
    print("built", slug)
