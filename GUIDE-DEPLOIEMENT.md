# 🚀 Guide de mise en ligne du site IPP Renovare

Ce guide explique **comment mettre votre nouveau site sur internet**, étape par étape, sans aucune connaissance technique requise.

Durée totale estimée : **30 minutes**.

---

## ✅ Avant de commencer : récapitulatif

Tout votre site est prêt dans le dossier :
```
C:\Users\gevor\OneDrive\Bureau\IPP Renovare\Logiciels\site-web\
```

Ce dossier contient **toutes les pages** (accueil, services, réalisations, avis, contact, etc.) et tous les fichiers nécessaires. **Vous n'avez RIEN à modifier.**

---

## 📦 ÉTAPE 1 — Compresser le dossier en ZIP (2 min)

Netlify accepte les sites sous forme de fichier ZIP. Voici comment faire :

1. Ouvrez l'**Explorateur de fichiers** Windows
2. Allez dans `C:\Users\gevor\OneDrive\Bureau\IPP Renovare\Logiciels\`
3. **Clic droit** sur le dossier `site-web`
4. Choisissez **« Envoyer vers » → « Dossier compressé »**
5. Un fichier `site-web.zip` apparaît juste à côté

C'est ce fichier que vous allez glisser sur Netlify dans 2 minutes.

---

## 🌐 ÉTAPE 2 — Créer un compte Netlify gratuit (3 min)

Netlify est l'**hébergeur** : c'est l'entreprise qui va stocker votre site et le rendre accessible sur internet.

C'est **100 % gratuit** pour votre cas (jusqu'à 100 Go de bande passante/mois — vous n'atteindrez jamais cette limite).

1. Allez sur **https://www.netlify.com/**
2. Cliquez sur **« Sign up »** (en haut à droite)
3. Choisissez **« Sign up with email »** (avec votre email)
4. Entrez : `ipprenovare@gmail.com` + un mot de passe que vous notez bien
5. Vérifiez votre boîte mail — Netlify vous envoie un email de confirmation
6. Cliquez sur le lien dans l'email → vous êtes connecté

---

## 🚀 ÉTAPE 3 — Mettre votre site en ligne (2 min)

C'est ici que la magie opère.

1. Une fois connecté à Netlify, vous arrivez sur le tableau de bord (« Sites »)
2. Au milieu de la page, vous voyez un **encadré gris en pointillés** avec écrit :
   > **« Drag and drop your site folder here »**
3. **Glissez votre fichier `site-web.zip`** depuis l'Explorateur Windows directement dans cet encadré
4. Patientez **30 secondes** : Netlify déploie automatiquement votre site

🎉 **Votre site est en ligne !** Netlify lui donne automatiquement une adresse temporaire du genre :
```
https://magnifique-tournesol-1234.netlify.app
```

Cliquez dessus pour vérifier qu'il s'affiche bien. Toutes les pages doivent fonctionner.

---

## 🌍 ÉTAPE 4 — Brancher votre nom de domaine ipprenovare.com (15 min)

L'adresse temporaire `xxx.netlify.app` n'est pas pro. On va la remplacer par **ipprenovare.com**.

### 4.1 — Côté Netlify

1. Sur le tableau de bord de votre site Netlify, cliquez sur **« Domain settings »** (« Paramètres du domaine »)
2. Cliquez sur **« Add custom domain »** (« Ajouter un domaine personnalisé »)
3. Tapez : `ipprenovare.com`
4. Validez. Netlify vous demande peut-être de prouver que vous possédez ce domaine — confirmez « Yes, add domain »
5. Netlify affiche maintenant **2 informations DNS à configurer** :
   - Soit une adresse IP (genre `75.2.60.5`)
   - Soit des « nameservers » (genre `dns1.p07.nsone.net`)
6. **Copiez ces informations** dans un fichier texte ou notez-les

### 4.2 — Côté votre hébergeur actuel (où ipprenovare.com est enregistré)

Votre nom de domaine `ipprenovare.com` est aujourd'hui enregistré chez un registrar (probablement OVH, Gandi, IONOS, ou GoDaddy — vous le savez via votre WordPress actuel).

1. **Connectez-vous chez votre registrar** (l'endroit où vous payez votre nom de domaine)
2. Trouvez la rubrique **« DNS »** ou **« Zone DNS »** ou **« Gérer les DNS »**
3. Modifiez les **enregistrements DNS** :

#### Option A (recommandée) — Méthode « nameservers » :
   - Remplacez les nameservers actuels par ceux de Netlify (les `dns1.p07.nsone.net` etc.)
   - Sauvegardez

#### Option B — Méthode « enregistrement A » :
   - Créez un enregistrement de type **A** pointant `@` vers l'IP donnée par Netlify
   - Créez un enregistrement de type **CNAME** pointant `www` vers `votre-site.netlify.app`
   - Sauvegardez

4. **Patientez 1 à 24h** : la propagation DNS peut prendre du temps. Pendant ce délai, l'ancien site WordPress est encore visible.

5. Une fois propagé, **ipprenovare.com affiche votre nouveau site**, en HTTPS sécurisé (Netlify active SSL automatiquement, gratuit).

> 💡 **Si vous avez peur de toucher aux DNS** : appelez le support de votre registrar (OVH, Gandi, etc.) et dites-leur :
> *« Je veux pointer mon domaine ipprenovare.com vers Netlify, voici les nameservers à mettre : [...] »*. Ils le font en 5 min.

---

## ✉️ ÉTAPE 5 — Activer la réception des devis par email (5 min)

Le formulaire de devis sur la page Contact est déjà configuré pour fonctionner avec **Netlify Forms** — gratuit jusqu'à 100 soumissions/mois.

1. Sur le tableau de bord Netlify, cliquez sur votre site
2. Allez dans l'onglet **« Forms »** dans le menu
3. Vous voyez automatiquement la liste des formulaires détectés (« contact »)
4. Cliquez sur **« Form notifications »** → **« Add notification »** → **« Email notification »**
5. Entrez votre email : `ipprenovare@gmail.com`
6. Sauvegardez

À partir de maintenant, **chaque demande de devis vous arrive par email** automatiquement, avec toutes les infos remplies par le client.

---

## 🔄 ÉTAPE 6 — Désactiver l'ancien WordPress (5 min)

Une fois que `ipprenovare.com` pointe bien vers Netlify et que vous avez vérifié que le nouveau site fonctionne :

1. Connectez-vous à votre **ancien WordPress** (`/wp-admin`)
2. **Sauvegardez les anciens contenus** au cas où (export → tools → Export)
3. Vous pouvez ensuite **résilier votre hébergement WordPress** (économie : ~5-15€/mois)
4. **Gardez votre nom de domaine** chez le registrar — il continue d'exister, juste qu'il pointe vers Netlify

---

## 🆘 Que faire si ça coince ?

**Le site ne s'affiche pas après changement DNS ?**
- Patientez 24h. Si toujours pas, vérifiez les nameservers chez votre registrar.

**Le formulaire de devis ne marche pas ?**
- Allez sur Netlify → onglet Forms → vérifiez que « contact » est listé.
- Vérifiez que vous avez bien activé la notification email.

**Vous voulez modifier un texte ou ajouter des photos plus tard ?**
- Dites-le moi, je modifie les fichiers, vous re-uploadez le ZIP sur Netlify (drag & drop, ça écrase l'ancien). 1 min chrono.

---

## 📋 Récapitulatif des 6 étapes

| # | Étape | Durée |
|---|---|---|
| 1 | Compresser le dossier en ZIP | 2 min |
| 2 | Créer un compte Netlify gratuit | 3 min |
| 3 | Drag & drop du ZIP sur Netlify | 2 min |
| 4 | Pointer ipprenovare.com vers Netlify (DNS) | 15 min |
| 5 | Activer les emails de devis | 5 min |
| 6 | Désactiver l'ancien WordPress | 5 min |

**Total : 32 minutes** — votre site est en ligne, professionnel, ultra-rapide, gratuit à héberger.
