# IPP Renovare — Site web

Site web professionnel de **IPP Renovare**, artisan plâtrier à Laxou (54520) intervenant dans le Grand Nancy et le Grand Est.

🌐 **Site en ligne** : [ipprenovare.com](https://ipprenovare.com)

## Stack technique

- HTML5 / CSS3 / JavaScript vanilla (aucun framework)
- Hébergement : **Netlify**
- Domaine : **IONOS**
- Admin CMS : **Decap CMS** (à l'adresse `/admin/`)
- Authentification : **Netlify Identity**

## Structure du projet

```
site-web/
├── index.html              # Accueil
├── services.html           # Hub services
├── service-*.html          # 6 pages services détaillées
├── platrier-*.html         # 3 pages locales SEO
├── article-*.html          # 15 articles de blog
├── blog.html               # Hub du blog
├── faq.html                # FAQ avec FAQSchema
├── pourquoi-nous-choisir.html
├── a-propos.html
├── avis.html
├── contact.html            # Formulaire de devis
├── realisations.html       # Galerie filtrable
├── 404.html
├── mentions-legales.html
├── politique-confidentialite.html
│
├── admin/                  # Interface admin Decap CMS
│   ├── index.html
│   └── config.yml
│
├── assets/
│   ├── css/styles.css
│   ├── js/script.js
│   └── images/
│
├── netlify.toml            # Configuration Netlify
├── robots.txt              # Bots IA autorisés
├── sitemap.xml
├── llms.txt                # Spec LLMs.txt pour les IA
└── favicon.ico
```

## Pour publier un nouvel article (depuis l'admin)

1. Aller sur [ipprenovare.com/admin/](https://ipprenovare.com/admin/)
2. Se connecter avec ses identifiants
3. Cliquer sur "📝 Articles de blog" → "New article"
4. Remplir titre, catégorie, contenu, etc.
5. Cliquer sur "Publish"

L'article est en ligne en 30 secondes.

## SEO & GEO

- 33 pages indexables, toutes avec meta + canonical + Open Graph + Twitter Cards
- Schema.org : LocalBusiness, BlogPosting, FAQPage, Service, Person, Reviews
- Robots.txt autorise GPTBot, ClaudeBot, PerplexityBot, Google-Extended
- llms.txt présent pour les IA
- 3 pages locales géographiques (Nancy, Laxou, Vandœuvre)

## Coordonnées entreprise

- **IPP Renovare** — Abelyan Arkadi
- 8 rue du grand parc, 54520 Laxou
- 📞 07 81 22 25 22 / 07 66 05 54 45
- ✉️ ipprenovare@gmail.com
- SIREN : 888 502 945
- Code APE : 4331Z (Travaux de plâtrerie)
- Garantie décennale : MAAF
