# -*- coding: utf-8 -*-
"""
Moteur de génération des articles créés via l'interface /admin (Decap CMS).
Lit les fichiers Markdown de _articles/ et :
 1. génère une page article-cms-<slug>.html pour chacun (même style que les articles existants)
 2. injecte les cartes correspondantes dans blog.html entre les marqueurs CMS
Pur Python (stdlib) — aucune dépendance, ne casse jamais le site existant.
"""
import os, re, html, datetime, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER_ARTICLES = os.path.join(ICI, "_articles")
DOSSIER_GALERIE = os.path.join(ICI, "_galerie")

# ---------- Mini-convertisseur Markdown -> HTML (sous-ensemble suffisant) ----------
def md_inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    return t

def md_to_html(md):
    lignes = md.split("\n")
    out, i, n = [], 0, len(lignes)
    while i < n:
        l = lignes[i].rstrip()
        if not l.strip():
            i += 1; continue
        # Titres
        m = re.match(r'^(#{2,4})\s+(.*)', l)
        if m:
            niv = len(m.group(1))
            out.append(f"<h{niv}>{md_inline(m.group(2))}</h{niv}>")
            i += 1; continue
        # Citation
        if l.startswith(">"):
            bloc = []
            while i < n and lignes[i].startswith(">"):
                bloc.append(lignes[i][1:].strip()); i += 1
            out.append(f"<blockquote><p>{md_inline(' '.join(bloc))}</p></blockquote>")
            continue
        # Liste non ordonnée
        if re.match(r'^[-*]\s+', l):
            items = []
            while i < n and re.match(r'^[-*]\s+', lignes[i].strip()):
                items.append(f"<li>{md_inline(re.sub(r'^[-*]\\s+','',lignes[i].strip()))}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        # Liste ordonnée
        if re.match(r'^\d+\.\s+', l):
            items = []
            while i < n and re.match(r'^\d+\.\s+', lignes[i].strip()):
                items.append(f"<li>{md_inline(re.sub(r'^\\d+\\.\\s+','',lignes[i].strip()))}</li>"); i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        # Paragraphe
        para = [l]
        i += 1
        while i < n and lignes[i].strip() and not re.match(r'^(#{2,4}\s|[-*]\s|\d+\.\s|>)', lignes[i].strip()):
            para.append(lignes[i].rstrip()); i += 1
        out.append(f"<p>{md_inline(' '.join(para))}</p>")
    return "\n".join(out)

# ---------- Parse frontmatter YAML simple (clé: valeur) ----------
def parse_article(chemin):
    txt = open(chemin, encoding="utf-8").read()
    meta, corps = {}, txt
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', txt, re.DOTALL)
    if m:
        for ligne in m.group(1).split("\n"):
            if ":" in ligne:
                k, v = ligne.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
        corps = m.group(2)
    return meta, corps

CATS = {"guide":"Guide","prix":"Prix & budget","projet":"Projet","local":"Local","tendance":"Tendance"}

def slug_de(nom):
    return re.sub(r'\.md$', '', os.path.basename(nom))

def page_article(meta, corps_html, slug):
    titre = html.escape(meta.get("title","Article"))
    desc = html.escape(meta.get("description",""))
    cat = meta.get("category","guide")
    badge = CATS.get(cat, "Article")
    date = meta.get("date","")[:10]
    auteur = html.escape(meta.get("author","Abelyan Arkadi"))
    readtime = meta.get("readtime","6")
    try:
        d = datetime.date.fromisoformat(date); date_fr = d.strftime("%d/%m/%Y")
    except Exception:
        date_fr = date
    fichier = f"article-cms-{slug}.html"
    return fichier, f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titre} — IPP Renovare</title>
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="author" content="{auteur}">
    <link rel="canonical" href="https://ipprenovare.com/{fichier}">
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/assets/images/apple-touch-icon.png">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{titre}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://ipprenovare.com/{fichier}">
    <meta property="og:image" content="https://ipprenovare.com/assets/images/og-image.jpg">
    <meta name="theme-color" content="#a50e17">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/styles.css">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BlogPosting","headline":"{titre}","description":"{desc}","author":{{"@type":"Person","name":"{auteur}"}},"publisher":{{"@type":"Organization","name":"IPP Renovare","logo":{{"@type":"ImageObject","url":"https://ipprenovare.com/assets/images/logo.png"}}}},"datePublished":"{date}","mainEntityOfPage":"https://ipprenovare.com/{fichier}"}}
    </script>
</head>
<body>
    <header class="header">
        <div class="header-inner">
            <a href="index.html" class="logo">
                <img src="assets/images/logo.png" alt="Logo IPP Renovare" onerror="this.onerror=null;this.src='assets/images/logo.svg';">
                <div>IPP Renovare<span class="logo-sous">Plâtrier · Nancy</span></div>
            </a>
            <nav class="nav">
                <ul class="nav-liens">
                    <li><a href="index.html">Accueil</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="realisations.html">Réalisations</a></li>
                    <li><a href="album.html">Album</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="a-propos.html">À propos</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
                <a href="contact.html" class="btn btn-primaire">Devis gratuit</a>
                <div class="menu-burger"><span></span><span></span><span></span></div>
            </nav>
        </div>
    </header>
    <section class="article-banniere">
        <div class="article-banniere-contenu">
            <nav class="breadcrumb"><a href="index.html">Accueil</a><span class="sep">›</span><a href="blog.html">Blog</a><span class="sep">›</span>{badge}</nav>
            <span class="surtitre" style="color: var(--rouge);">{badge}</span>
            <h1>{titre}</h1>
            <div class="article-banniere-meta">
                <span>Publié le <strong>{date_fr}</strong></span>
                <span>Par <strong>{auteur}</strong></span>
                <span><strong>{readtime} min</strong> de lecture</span>
            </div>
        </div>
    </section>
    <article class="article-contenu">
{corps_html}
        <div class="article-cta">
            <h3>Un projet de plâtrerie ou de rénovation à Nancy ?</h3>
            <p>Devis gratuit sous 48h, déplacement offert dans tout le Grand Nancy.</p>
            <a href="contact.html" class="btn btn-clair">Demander mon devis →</a>
        </div>
    </article>
    <footer class="footer">
        <div class="container">
            <div class="footer-bas" style="border:none; padding:2rem 0;">
                <div>© 2026 IPP Renovare · SIREN 888 502 945</div>
                <div><a href="mentions-legales.html">Mentions légales</a> · <a href="blog.html">Blog</a></div>
            </div>
        </div>
    </footer>
    <script src="assets/js/script.js"></script>
</body>
</html>
"""

def carte_blog(meta, slug):
    titre = html.escape(meta.get("title","Article"))
    extrait = html.escape(meta.get("extrait", meta.get("description","")))
    cat = meta.get("category","guide")
    badge = CATS.get(cat, "Article")
    sub = html.escape(meta.get("subcategory","Conseils"))
    date = meta.get("date","")[:10]
    try:
        d = datetime.date.fromisoformat(date)
        mois = ["janv.","févr.","mars","avril","mai","juin","juil.","août","sept.","oct.","nov.","déc."][d.month-1]
        date_fr = f"{mois} {d.year}"
    except Exception:
        date_fr = date
    rt = meta.get("readtime","6")
    return f'''                <article class="article-carte fade-in" data-categorie="{cat}">
                    <a href="article-cms-{slug}.html" style="display: contents;">
                        <div class="article-image"></div>
                        <div class="article-corps">
                            <span class="article-categorie">{badge}</span>
                            <div class="article-meta">{date_fr} · {rt} min · {sub}</div>
                            <h2 class="article-titre">{titre}</h2>
                            <p class="article-extrait">{extrait}</p>
                            <span class="article-lien">Lire l'article →</span>
                        </div>
                    </a>
                </article>'''

# ---------- Galerie photos (créées via /admin -> _galerie/*.md) ----------
# Rayons de l'album : slug -> (mot-clé alt court)
GALERIE_CATS = {
    "platrerie":     "Plâtrerie",
    "cloisons":      "Cloisons",
    "faux-plafonds": "Faux-plafond",
    "isolation":     "Isolation",
    "renovation":    "Rénovation",
    "peinture":      "Peinture",
}

def slugify(txt):
    """Transforme 'Enduits décoratifs' -> 'enduits-decoratifs' (pour l'id du rayon)."""
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode("ascii")
    txt = re.sub(r'[^a-zA-Z0-9]+', '-', txt).strip('-').lower()
    return txt or "autre"

def infos_categorie(meta):
    """Renvoie (slug, nom affiché). Priorité au champ 'nouvelle_categorie' si rempli."""
    nouvelle = meta.get("nouvelle_categorie", "").strip()
    if nouvelle:
        return slugify(nouvelle), nouvelle
    slug = meta.get("categorie", "platrerie")
    if slug not in GALERIE_CATS:
        slug = "platrerie"
    return slug, GALERIE_CATS[slug]

def figure_photo(meta, slug, nom):
    src = meta.get("image", "").strip()
    legende = html.escape(meta.get("legende", ""))
    alt = f"{html.escape(nom)} à Nancy — {legende}" if legende else f"{html.escape(nom)} à Nancy"
    return f'''                    <figure class="album-photo" data-cat="{slug}">
                        <img src="{html.escape(src)}" alt="{alt}" loading="lazy" data-legende="{legende}">
                        <figcaption>{legende}</figcaption>
                    </figure>'''

def galerie():
    """Range chaque photo publiée via /admin dans le bon rayon de album.html.
    Si une photo indique une catégorie inédite, un nouveau rayon est créé
    automatiquement en bas de l'album — le client est autonome."""
    if not os.path.isdir(DOSSIER_GALERIE):
        return 0
    # lire et trier les photos (plus récentes d'abord)
    entrees = []
    for f in sorted(os.listdir(DOSSIER_GALERIE)):
        if f.endswith(".md"):
            meta, _ = parse_article(os.path.join(DOSSIER_GALERIE, f))
            entrees.append((meta.get("date", ""), meta))
    entrees.sort(key=lambda x: x[0], reverse=True)

    par_slug, noms, n = {}, {}, 0
    for _, meta in entrees:
        slug, nom = infos_categorie(meta)
        par_slug.setdefault(slug, []).append(figure_photo(meta, slug, nom))
        noms[slug] = nom
        n += 1

    album_path = os.path.join(ICI, "album.html")
    album = open(album_path, encoding="utf-8").read()

    # 1) rayons existants : injection entre leurs marqueurs
    for cat in GALERIE_CATS:
        figs = "\n".join(par_slug.get(cat, []))
        contenu = f"<!-- GALERIE:{cat}:START -->"
        if figs:
            contenu += "\n" + figs + "\n                    "
        contenu += f"<!-- GALERIE:{cat}:END -->"
        motif = re.compile(rf'<!-- GALERIE:{cat}:START -->.*?<!-- GALERIE:{cat}:END -->', re.DOTALL)
        album = motif.sub(lambda m: contenu, album)

    # 2) rayons inédits : sections créées automatiquement (bloc GALERIE-AUTO)
    nouveaux = [s for s in par_slug if s not in GALERIE_CATS]
    sections = []
    for idx, slug in enumerate(nouveaux):
        nom = html.escape(noms[slug])
        figs = "\n".join(par_slug[slug])
        classe = "section section-claire" if idx % 2 == 0 else "section"
        sections.append(f'''        <section class="{classe}" id="{slug}">
            <div class="container">
                <div class="entete-section fade-in">
                    <span class="surtitre">{nom}</span>
                    <h2>{nom}</h2>
                    <p class="lead">Nos chantiers « {nom} » à Nancy, Laxou et dans le Grand Est.</p>
                </div>
                <div class="album-grille">
{figs}
                </div>
            </div>
        </section>''')
    auto = "<!-- GALERIE-AUTO:START -->"
    if sections:
        auto += "\n" + "\n".join(sections) + "\n        "
    auto += "<!-- GALERIE-AUTO:END -->"
    album = re.sub(r'<!-- GALERIE-AUTO:START -->.*?<!-- GALERIE-AUTO:END -->', lambda m: auto, album, flags=re.DOTALL)

    open(album_path, "w", encoding="utf-8").write(album)
    return n

def main():
    articles = []
    if os.path.isdir(DOSSIER_ARTICLES):
        for f in sorted(os.listdir(DOSSIER_ARTICLES)):
            if f.endswith(".md"):
                meta, corps = parse_article(os.path.join(DOSSIER_ARTICLES, f))
                slug = slug_de(f)
                corps_html = md_to_html(corps)
                fichier, page = page_article(meta, corps_html, slug)
                open(os.path.join(ICI, fichier), "w", encoding="utf-8").write(page)
                articles.append((meta, slug, meta.get("date","")))
    # trier par date décroissante
    articles.sort(key=lambda x: x[2], reverse=True)
    cartes = "\n".join(carte_blog(m, s) for m, s, _ in articles)

    # injecter dans blog.html entre les marqueurs
    blog_path = os.path.join(ICI, "blog.html")
    blog = open(blog_path, encoding="utf-8").read()
    bloc = f"<!-- CMS:START -->\n{cartes}\n                <!-- CMS:END -->"
    if "<!-- CMS:START -->" in blog and "<!-- CMS:END -->" in blog:
        blog = re.sub(r'<!-- CMS:START -->.*?<!-- CMS:END -->', lambda m: bloc, blog, flags=re.DOTALL)
        open(blog_path, "w", encoding="utf-8").write(blog)
    nb_photos = galerie()
    print(f"build.py : {len(articles)} article(s) CMS généré(s), {nb_photos} photo(s) de galerie rangée(s)")

if __name__ == "__main__":
    main()
