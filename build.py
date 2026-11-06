#!/usr/bin/env python3
"""Builds the Dynamic Horse Solutions pages from one frame, so the menu and footer never drift. Run: python3 build.py"""
import io

RELEASE = "https://link.aztechsol.com/bewell-release"
WEBHOOK = "https://n8n.aztechsol.com/webhook/dhs-registration"
JO_EMAIL = "az.horsesensetraining@gmail.com"
NAV = [("index.html", "Home"), ("classes.html", "Classes"), ("register.html", "Register"), ("about.html", "About"), ("contact.html", "Contact")]

def frame(slug, title, desc, body):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == slug else ""}>{t}</a>' for h, t in NAV)
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
<meta property="og:title" content="{title}">
<meta property="og:image" content="assets/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="top">
  <a class="brand" href="index.html" aria-label="Dynamic Horse Solutions, home"><img src="assets/mark.svg" alt="" width="48" height="48"></a>
  <nav class="wide" aria-label="Menu">{links}<a class="release" href="{RELEASE}">Sign the media release</a></nav>
  <details class="narrow"><summary aria-label="Menu"><span></span><span></span><span></span></summary>
    <nav aria-label="Menu">{links}<a class="release" href="{RELEASE}">Sign the media release</a></nav></details>
</header>
<main>
{body}
</main>
<footer>
  <img src="assets/logo.svg" alt="Dynamic Horse Solutions" width="140" height="140">
  <p><a href="classes.html">Classes</a> · <a href="register.html">Register</a> · <a href="{RELEASE}">Media release</a> · <a href="contact.html">Contact</a></p>
  <p>© 2026 Dynamic Horse Solutions · Tucson, Arizona</p>
  <p class="credit">Photos: <a href="https://commons.wikimedia.org/wiki/File:Domestic_horse_at_Suryachaur_and_the_mountains_in_the_back1.jpg">Shadow Ayush</a> · <a href="https://commons.wikimedia.org/wiki/File:Saint-Laurent-d%27Aigouze_-_Camargue_horses_-_04.jpg">Benjamin Smith</a> · <a href="https://commons.wikimedia.org/wiki/File:NewForestPonies_sunrise.jpg">Joana Kruse</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>, via Wikimedia Commons.</p>
</footer>
</body>
</html>
"""

SATURDAY = """
  <article class="part part-one">
    <div class="band">
      <p class="num">Part I · This Saturday</p>
      <h3>The Hind End Junction</h3>
      <p class="parts">Pelvis • Sacrum • Lumbar Spine</p>
    </div>
    <div class="part-body">
      <img src="assets/hind-end.jpg" alt="Drawing of a horse's skeleton with the lumbar spine, sacrum and pelvis highlighted" width="842" height="716">
      <div>
        <p class="when">Saturday, November 7, 2026<br><span>9 AM – 1 PM</span></p>
        <p class="where">Copper Horse Ranch<br>9887 N Camino de Oeste · Tucson, AZ</p>
        <p class="price">$110 <span>per person</span></p>
        <p class="incl">Lecture · demonstration · guided skeleton exploration · workbook included</p>
        <p class="actions"><a class="btn" href="register.html?class=part-1">Register for Saturday</a></p>
        <p class="small">Space is limited. Early registration encouraged.</p>
      </div>
    </div>
  </article>"""

LATER = """
  <div class="later">
    <article class="part">
      <p class="num">Part II</p>
      <h3>The Thoracic Sling</h3>
      <p class="when">February 2027 <em>(date TBD)</em></p>
      <p class="small"><a href="register.html?class=part-2">Hold a place</a></p>
    </article>
    <article class="part">
      <p class="num">Part III</p>
      <h3>Poll &amp; TMJ</h3>
      <p class="when">April 2027 <em>(date TBD)</em></p>
      <p class="small"><a href="register.html?class=part-3">Hold a place</a></p>
    </article>
  </div>"""

HOME = f"""
<section class="hero-slider" aria-label="Equine Biomechanics">
  <div class="slides">
    <img class="slide is-on" src="assets/hero-walk-1100.webp" srcset="assets/hero-walk-1100.webp 1100w, assets/hero-walk.webp 2200w" sizes="100vw" alt="A white horse walking along a ridge, mountains and sky behind" style="object-position:62% 55%">
    <img class="slide" src="assets/hero-camargue-1100.webp" srcset="assets/hero-camargue-1100.webp 1100w, assets/hero-camargue.webp 2200w" sizes="100vw" alt="Camargue horses standing in still water under a blue sky, their reflections below" style="object-position:50% 60%" loading="lazy">
    <img class="slide" src="assets/hero-sunrise-1100.webp" srcset="assets/hero-sunrise-1100.webp 1100w, assets/hero-sunrise.webp 2200w" sizes="100vw" alt="Two ponies walking through morning mist at sunrise" style="object-position:35% 70%" loading="lazy">
  </div>
  <div class="hero-copy">
    <p class="eyebrow">A three-part educational series for horse owners &amp; riders</p>
    <h1>Equine Biomechanics</h1>
    <p class="triad"><span>Structure</span><i>•</i><span>Posture</span><i>•</i><span>Function</span></p>
    <p class="hero-actions"><a class="btn" href="register.html?class=part-1">Register for Saturday</a><a class="btn light" href="classes.html">See the classes</a></p>
  </div>
  <div class="dots" role="group" aria-label="Photos"><button type="button" aria-label="Show photo 1" aria-current="true"></button><button type="button" aria-label="Show photo 2"></button><button type="button" aria-label="Show photo 3"></button></div>
</section>
<script>
(function(){{
  var s=[].slice.call(document.querySelectorAll(".hero-slider .slide")), d=[].slice.call(document.querySelectorAll(".hero-slider .dots button")), i=0, t;
  function go(n){{ s[i].classList.remove("is-on"); d[i].removeAttribute("aria-current"); i=(n+s.length)%s.length; s[i].classList.add("is-on"); d[i].setAttribute("aria-current","true"); }}
  function play(){{ if(matchMedia("(prefers-reduced-motion: reduce)").matches) return; clearInterval(t); t=setInterval(function(){{go(i+1)}},6000); }}
  d.forEach(function(b,n){{ b.addEventListener("click",function(){{ go(n); play(); }}); }});
  play();
}})();
</script>

<section class="intro">
  <img class="logo" src="assets/logo.svg" alt="Dynamic Horse Solutions" width="240" height="240">
  <p class="lede">Explore the relationship between structure, posture and function through lecture, demonstration and guided exploration of a real equine skeleton. Learn to recognize healthy weight-bearing posture, identify postural imbalances, and better tell patterns of posture and restriction apart from those that may point to true discomfort.</p>
  <ul class="format"><li>Lecture</li><li>Demonstration</li><li>Guided skeleton exploration</li><li>Workbook included</li></ul>
</section>

<section class="series">
  <h2>Next Class</h2>
  {SATURDAY}
  {LATER}
  <p class="note"><a href="classes.html">See every class, the workbook and the media release →</a></p>
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
</section>
"""

CLASSES = f"""
<section class="page-head">
  <h1>Classes</h1>
  <p class="lede center">Equine Biomechanics: Structure · Posture · Function. Three parts, each a morning at the ranch with a real equine skeleton.</p>
</section>

<section class="series">
  {SATURDAY}

  <div class="extras">
    <article class="extra">
      <h3>The Workbook</h3>
      <p>Saturday's workbook, <em>The Hind End Junction</em>: posture, the anatomy of the hind end, and room for your notes. Download it to print or to keep on your tablet.</p>
      <p><a class="btn ghost" href="assets/hind-end-junction-workbook.pdf" download>Download the workbook (PDF)</a></p>
    </article>
    <article class="extra">
      <h3>The Media Release</h3>
      <p>Saturday's class is being filmed for the online series. If you're attending, please sign the consent to be filmed before you arrive. It takes a minute on your phone.</p>
      <p><a class="btn ghost" href="{RELEASE}">Sign the media release</a></p>
    </article>
  </div>

  <h2 class="later-head">Coming Next</h2>
  {LATER}
  <p class="note">Dates for Parts II and III will be announced here. <a href="register.html">Hold a place</a> and Jo Ann will let you know first.</p>
</section>
"""

REGISTER = f"""
<section class="page-head">
  <h1>Register</h1>
  <p class="lede center">Save your place, and Jo Ann will confirm by email or text. Payment is by Zelle or PayPal to Jo Ann, as she'll explain when she confirms.</p>
</section>

<section class="form-wrap">
  <form id="reg" class="reg" novalidate>
    <label>Class
      <select name="class" id="class" required>
        <option value="part-1">Part I · Sat, Nov 7 · 9 AM–1 PM · $110 per person</option>
        <option value="part-2">Part II · February 2027 · hold a place</option>
        <option value="part-3">Part III · April 2027 · hold a place</option>
      </select>
    </label>
    <label>Full name <input name="full_name" autocomplete="name" required></label>
    <div class="two">
      <label>Email <input name="email" type="email" autocomplete="email" required></label>
      <label>Phone <input name="phone" type="tel" autocomplete="tel" required></label>
    </div>
    <div class="two">
      <label>People attending <input name="people" type="number" min="1" max="20" value="1" required></label>
      <label>Horses you'll be thinking of <span class="opt">(optional)</span> <input name="horses" type="number" min="0" max="20" value="1"></label>
    </div>
    <fieldset>
      <legend>How you'll pay Jo Ann</legend>
      <label class="inline"><input type="radio" name="payment" value="Zelle" checked> Zelle</label>
      <label class="inline"><input type="radio" name="payment" value="PayPal"> PayPal</label>
    </fieldset>
    <label>Anything Jo Ann should know <span class="opt">(optional)</span> <textarea name="notes" rows="3"></textarea></label>
    <p class="small">Attending Saturday? The class is being filmed. Please also <a href="{RELEASE}">sign the media release</a>.</p>
    <button class="btn" type="submit">Send my registration</button>
    <p id="msg" class="msg" role="status" aria-live="polite"></p>
  </form>
</section>
<script>
(function(){{
  var f=document.getElementById("reg"), msg=document.getElementById("msg");
  var q=new URLSearchParams(location.search).get("class"); if(q) document.getElementById("class").value=q;
  function mailto(d){{
    var sel=f.querySelector("#class"), cls=sel.options[sel.selectedIndex].text;
    var body="Registration\\n\\nClass: "+cls+"\\nName: "+d.full_name+"\\nEmail: "+d.email+"\\nPhone: "+d.phone+"\\nPeople: "+d.people+"\\nHorses: "+(d.horses||"")+"\\nPaying by: "+d.payment+"\\nNotes: "+(d.notes||"");
    return "mailto:{JO_EMAIL}?subject="+encodeURIComponent("Registration: "+cls.split(" · ")[0]+" · "+d.full_name)+"&body="+encodeURIComponent(body);
  }}
  f.addEventListener("submit",function(e){{
    e.preventDefault();
    if(!f.checkValidity()){{ f.reportValidity(); return; }}
    var d=Object.fromEntries(new FormData(f).entries());
    d.class_label=f.querySelector("#class").selectedOptions[0].text; d.submitted_at=new Date().toISOString(); d.page=location.href;
    var btn=f.querySelector("button"); btn.disabled=true; msg.textContent="Sending…";
    fetch("{WEBHOOK}",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(d)}})
      .then(function(r){{ if(!r.ok) throw new Error(r.status); f.reset(); msg.innerHTML="Thank you, you're registered. Jo Ann will confirm and send payment details."; }})
      .catch(function(){{ msg.innerHTML="Your email app is opening with your registration filled in. Press send and it goes to Jo Ann. If nothing opens, email <a href=\\""+mailto(d)+"\\">{JO_EMAIL}</a> or call 520-403-8200."; location.href=mailto(d); }})
      .finally(function(){{ btn.disabled=false; }});
  }});
}})();
</script>
"""

ABOUT = """
<section class="page-head">
  <h1>About</h1>
  <p class="lede center">Dynamic Horse Solutions is the shared home of the teaching Jo Ann Lewis and Vanessa Helvey do together, in person in Tucson and on video for everyone who can't make it to the ranch.</p>
</section>

<section id="teachers" class="teachers">
  <h2>The Teachers</h2>
  <img class="duo" src="assets/teachers.jpg" alt="Jo Ann Lewis and Vanessa Helvey" width="732" height="376">
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
  <p><a class="btn" href="register.html">Register for a class</a></p>
</section>
"""

PAGES = [
    ("index.html", "Dynamic Horse Solutions — Equine Biomechanics", "Equine Biomechanics: Structure · Posture · Function. A three-part series for horse owners and riders in Tucson, taught by Jo Ann Lewis and Vanessa Helvey.", HOME),
    ("classes.html", "Classes — Dynamic Horse Solutions", "Part I, The Hind End Junction, Saturday November 7, 2026 at Copper Horse Ranch, Tucson; then Parts II and III in 2027.", CLASSES),
    ("register.html", "Register — Dynamic Horse Solutions", "Register for an Equine Biomechanics class with Jo Ann Lewis and Vanessa Helvey.", REGISTER),
    ("about.html", "About — Dynamic Horse Solutions", "Jo Ann Lewis, Vanessa Helvey and Chase, the teachers of Equine Biomechanics.", ABOUT),
    ("contact.html", "Contact — Dynamic Horse Solutions", "Reach Jo Ann Lewis about classes, dates and the online series.", CONTACT),
]
for slug, title, desc, body in PAGES:
    io.open(slug, "w", encoding="utf-8").write(frame(slug, title, desc, body))
    print("built", slug)
