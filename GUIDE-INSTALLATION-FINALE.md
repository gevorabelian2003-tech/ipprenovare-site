# 🚀 Guide d'installation finale — IPP Renovare

**Durée totale : ~2 heures**
**Niveau : pédagogique, conçu pour quelqu'un qui ne touche jamais au code**

---

## 📋 Vue d'ensemble en 3 phases

| Phase | Durée | Ce qu'on fait |
|---|---|---|
| **Phase 1** | 30 min | Mettre le site sur GitHub |
| **Phase 2** | 30 min | Connecter Netlify + brancher le domaine IONOS |
| **Phase 3** | 30 min | Activer l'interface admin Decap CMS |
| **Tests** | 30 min | Vérifier que tout fonctionne |

---

# 🔧 PHASE 1 — GitHub (30 min)

## 1.1 Créer un compte GitHub

1. Allez sur **[github.com](https://github.com/signup)**
2. Cliquez sur **"Sign up"** en haut à droite
3. Email : `gevorabelian2003@gmail.com`
4. Choisissez un mot de passe fort (notez-le précieusement)
5. Choisissez un **username** : `ipprenovare` (ou `gevorabelian` si pris)
6. Suivez les vérifications anti-robot
7. Confirmez votre email (clic dans le mail reçu)

**Plan** : choisissez le **plan Free** (suffit largement pour notre besoin).

## 1.2 Installer GitHub Desktop (le plus simple)

GitHub Desktop est une **application Windows** qui permet d'envoyer votre site sur GitHub **sans toucher au code**, juste avec des clics.

1. Allez sur **[desktop.github.com](https://desktop.github.com)**
2. Cliquez sur **"Download for Windows"**
3. Installez (le setup est classique : Suivant, Suivant, OK)
4. Lancez l'application
5. Connectez-vous avec votre compte GitHub fraîchement créé

## 1.3 Créer un nouveau dépôt (repository) pour le site

Dans GitHub Desktop :

1. **File** → **Add Local Repository...**
2. Cliquez sur **Choose...** et sélectionnez le dossier :
   `C:\Users\gevor\OneDrive\Bureau\IPP Renovare\Logiciels\site-web`
3. GitHub Desktop dit *"This directory is not a Git repository. Create a repository?"* → cliquez sur **"create a repository"**
4. Nom du repo : `ipprenovare-site` (ou similaire)
5. Description : `Site web IPP Renovare`
6. Git Ignore : laissez vide (on a déjà notre `.gitignore`)
7. License : laissez vide
8. Cliquez sur **"Create Repository"**

## 1.4 Premier "commit" et publication sur GitHub

Toujours dans GitHub Desktop :

1. À gauche, vous voyez la liste des fichiers (toutes les cases doivent être cochées)
2. En bas à gauche, dans **"Summary (required)"** : tapez `Initial commit — IPP Renovare site complet`
3. Cliquez sur le bouton bleu **"Commit to main"**
4. En haut, cliquez sur **"Publish repository"**
5. **Décochez** la case "Keep this code private" si vous voulez que le code soit public (ce n'est pas obligatoire pour le SEO mais ça simplifie certaines configurations gratuites de Netlify). Si vous préférez privé, laissez cochée — Netlify gérera quand même.
6. Cliquez sur **"Publish Repository"**

✅ **Votre site est maintenant sur GitHub !** Vous pouvez vérifier en allant sur [github.com](https://github.com) dans votre navigateur — vous verrez votre repo `ipprenovare-site`.

---

# 🌐 PHASE 2 — Netlify + Domaine IONOS (30 min)

## 2.1 Créer un site Netlify depuis GitHub

1. Connectez-vous à **[app.netlify.com](https://app.netlify.com)**
2. En haut, cliquez sur **"Add new site"** → **"Import an existing project"**
3. Choisissez **"Deploy with GitHub"**
4. Autorisez Netlify à accéder à votre GitHub (clic sur "Authorize netlify")
5. Sélectionnez le repository **`ipprenovare-site`** dans la liste
6. **Branch to deploy** : laissez `main`
7. **Build command** : laissez vide
8. **Publish directory** : laissez vide ou tapez `.`
9. Cliquez sur **"Deploy ipprenovare-site"**

⏱️ Patientez **~30 secondes**. Netlify déploie votre site.

À la fin, vous voyez une URL temporaire du genre :
`https://magnifique-tournesol-1234.netlify.app`

✅ **Cliquez dessus pour vérifier que votre site fonctionne !** Toutes les pages, le blog, le contact, le bouton appel mobile…

## 2.2 Brancher votre domaine ipprenovare.com

### 2.2.1 Côté Netlify

1. Toujours dans Netlify, sur votre site, cliquez sur **"Domain settings"**
2. Cliquez sur **"Add a domain"** ou **"Add a custom domain"**
3. Tapez `ipprenovare.com` et validez
4. Netlify vous demande de prouver que c'est votre domaine → cliquez sur **"Yes, add domain"**

Netlify vous propose **2 méthodes** pour configurer le DNS. **On va utiliser la plus simple : changer les nameservers chez IONOS**.

5. Notez les **4 nameservers Netlify** (genre `dns1.p07.nsone.net`, `dns2.p07.nsone.net`, etc.) — Netlify vous les affiche.

### 2.2.2 Côté IONOS

1. Connectez-vous à **[my.ionos.fr](https://my.ionos.fr)** (votre espace client IONOS)
2. Allez dans **"Domaines & SSL"** → cliquez sur `ipprenovare.com`
3. Trouvez la section **"DNS"** ou **"Serveurs de noms"** (parfois "Nameserver")
4. Choisissez **"Utiliser des serveurs de noms personnalisés"** (pas IONOS par défaut)
5. **Remplacez** les 2 ou 4 nameservers actuels par ceux de Netlify
6. Sauvegardez

⏱️ **Patientez 1 à 24 h** : la propagation DNS peut prendre du temps. Pendant cette période, votre ancien WordPress reste visible sur ipprenovare.com.

> 💡 **Si vous bloquez côté IONOS** : leur support est très réactif. Appelez-les ou utilisez le chat en disant : *« Je veux pointer mon domaine vers Netlify, voici les 4 nameservers : [...] »*. Ils le font en 5 min.

## 2.3 Activer HTTPS (gratuit, automatique)

Une fois le DNS propagé (vous le verrez dans Netlify : "DNS verification successful"), Netlify active automatiquement le **certificat SSL Let's Encrypt** (HTTPS gratuit).

✅ Votre site est maintenant en ligne sur `https://ipprenovare.com`

---

# 🔐 PHASE 3 — Activer l'interface admin Decap CMS (30 min)

## 3.1 Activer Netlify Identity

1. Sur Netlify, dans votre site, cliquez sur **"Site configuration"** dans le menu de gauche
2. Cliquez sur **"Identity"**
3. Cliquez sur le bouton **"Enable Identity"**

C'est fait : Netlify Identity est actif.

## 3.2 Configurer l'inscription

1. Toujours dans **"Identity"** → **"Settings and usage"**
2. Section **"Registration preferences"** :
   - Choisissez **"Invite only"** (recommandé) — comme ça personne ne peut s'inscrire sans votre invitation
3. Section **"External providers"** (optionnel) :
   - Vous pouvez activer **Google** pour vous connecter avec votre compte Google directement (pratique)
4. Sauvegardez

## 3.3 Activer Git Gateway

C'est le pont entre Decap CMS et votre code GitHub :

1. Dans **"Identity"**, descendez jusqu'à **"Services"**
2. Cliquez sur **"Enable Git Gateway"**
3. Netlify se connecte automatiquement à votre repo GitHub

✅ Git Gateway activé.

## 3.4 Vous inviter en tant qu'utilisateur

1. Dans **"Identity"**, cliquez sur **"Invite users"**
2. Email : `gevorabelian2003@gmail.com`
3. Cliquez sur **"Send"**
4. Vous recevez un email **"You've been invited to ipprenovare.com"**
5. Cliquez sur le lien dans l'email
6. Définissez votre **mot de passe** (notez-le)

## 3.5 Tester l'accès admin

1. Allez sur **`https://ipprenovare.com/admin/`** (ou l'URL Netlify temporaire si DNS pas encore propagé)
2. Cliquez sur **"Login with Netlify Identity"**
3. Entrez votre email + mot de passe
4. ✅ **Vous êtes dans l'interface admin !**

Vous voyez 3 collections :
- **📝 Articles de blog** : créer/modifier des articles
- **📄 Pages principales** : modifier les contenus de l'accueil et du contact
- **⭐ Avis clients** : ajouter de nouveaux avis

## 3.6 Test : créer votre premier article

1. Cliquez sur **"📝 Articles de blog"**
2. Cliquez sur **"New 📝 Articles de blog"** (en haut à droite)
3. Remplissez :
   - **Titre** : *« Test : mon premier article »*
   - **Description** : *« Test de l'interface admin »*
   - **Catégorie** : Guide
   - **Date** : aujourd'hui
   - **Auteur** : Abelyan Arkadi
   - **Contenu** : tapez quelques lignes (titre, paragraphes, gras…)
4. Cliquez sur **"Publish"** → **"Publish now"**

⏱️ Patientez **30 secondes** : Netlify déploie automatiquement.

✅ Votre article est en ligne ! Vérifiez sur le site (ou rafraîchissez la page Blog).

> ⚠️ **Note importante** : pour l'instant, la création d'articles **via Decap CMS génère un fichier Markdown** dans le dossier `_articles/` du repo, pas directement un fichier HTML. Pour que ce Markdown devienne un vrai article HTML visible sur le site, il faudra une étape supplémentaire : un **script de génération automatique**. Cette étape sera ajoutée dans une **Phase 4** ultérieure (1h de configuration). En attendant, vous pouvez :
> - **Créer/modifier les avis** ✅ fonctionne directement
> - **Modifier les pages principales** ✅ fonctionne directement
> - **Pour de nouveaux articles** : on continue temporairement avec ma méthode (vous me dites le sujet, je crée l'article HTML — vous le voyez sur le site automatiquement)

---

# ✅ PHASE 4 — Vérifications finales (30 min)

## 4.1 Activer le formulaire de devis (Netlify Forms)

1. Sur Netlify, allez dans **"Forms"**
2. Vous devez voir un formulaire détecté **"contact"**
3. Cliquez sur **"Form notifications"** → **"Add notification"** → **"Email notification"**
4. Email : `ipprenovare@gmail.com`
5. Sauvegardez

✅ À partir de maintenant, **chaque demande de devis vous arrive par email** automatiquement.

## 4.2 Tester le site

Visitez **`https://ipprenovare.com`** depuis :

- 🖥️ Un ordinateur (Chrome, Firefox, Edge, Safari)
- 📱 Un mobile (test absolument essentiel : bouton Appeler doit pulser)
- 🔍 Test du formulaire contact (envoyez-vous un faux devis pour vérifier que vous recevez l'email)
- 🔍 Test des liens de toutes les pages

## 4.3 Soumettre le sitemap à Google

1. Allez sur **[search.google.com/search-console](https://search.google.com/search-console)**
2. Connectez-vous avec votre compte Google
3. Ajoutez la propriété **`https://ipprenovare.com`**
4. Validez la propriété (Netlify peut le faire via DNS automatiquement, sinon copiez le code de vérification dans Netlify → Domain settings → DNS)
5. Une fois validé, allez dans **"Sitemaps"** et soumettez : `sitemap.xml`

⏱️ Google indexera vos 33 pages en **3 à 15 jours**.

## 4.4 Désactiver l'ancien WordPress

Une fois que `ipprenovare.com` pointe vers Netlify ET que tout fonctionne :

1. Connectez-vous à votre **ancien hébergement WordPress**
2. **Sauvegardez** d'abord les données (export → Tools → Export)
3. Vous pouvez **résilier l'hébergement WordPress** (économie : ~5-15€/mois)

> ⚠️ **Gardez votre nom de domaine chez IONOS** — il continue d'exister, juste qu'il pointe vers Netlify maintenant.

---

# 🎓 Comment publier un avis client (depuis l'admin)

1. Allez sur `ipprenovare.com/admin/`
2. Connectez-vous
3. Cliquez sur **"⭐ Avis clients"** → **"New ⭐ Avis clients"**
4. Remplissez :
   - **Auteur** : "Marie L."
   - **Ville** : "Nancy"
   - **Prestation** : "Plâtrerie"
   - **Note** : 5
   - **Texte** : « ... »
   - **Source** : Google
   - **Date** : aujourd'hui
5. Cliquez sur **"Publish"**

✅ Avis ajouté en 30 secondes.

---

# 🆘 SOS : que faire si ça coince ?

| Problème | Solution |
|---|---|
| Le site ne s'affiche pas après changement DNS | Patienter 24h. Vérifier les nameservers chez IONOS. |
| L'admin `/admin/` affiche une page blanche | Vérifier que Netlify Identity ET Git Gateway sont activés. |
| Le formulaire de devis ne marche pas | Vérifier dans Netlify → Forms que le formulaire "contact" est listé. Vérifier la notification email. |
| Je veux ajouter un article mais Decap CMS ne crée pas le HTML | Pour l'instant Decap CMS crée des fichiers Markdown — la génération HTML sera implémentée en Phase 4. En attendant, demandez-moi. |
| Je veux modifier un texte d'une page existante | Allez sur GitHub, trouvez le fichier, cliquez sur ✏️ "Edit", modifiez, "Commit changes". Netlify redéploie automatiquement. |

---

# 🎯 Récap : qu'est-ce qui change pour vous au quotidien

| Avant | Après |
|---|---|
| Site WordPress lent et mal optimisé | Site statique ultra-rapide |
| Modifier un article : aller dans WP-admin, lent | Modifier un article : interface admin Decap CMS, immédiat |
| Pas de sauvegarde | Historique complet sur GitHub (toutes les modifs gardées) |
| Pas de SEO IA | Optimisé pour ChatGPT, Claude, Perplexity |
| Pas de bouton "Appeler" mobile | Bouton flottant pulsant rouge, conversion mobile maximale |

---

**Une fois cette installation terminée, vous serez 100 % autonome pour publier des avis et modifier les pages principales. Pour les nouveaux articles complets, on optimisera la Phase 4 ensemble (script de génération automatique).**

Bonne installation ! 🚀
