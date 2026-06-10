/* =====================================================
   IPP RENOVARE - Script principal
   Toutes les interactions du site (menu, animations, formulaire, etc.)
   ===================================================== */

document.addEventListener('DOMContentLoaded', function () {

    /* --- 0. Injection automatique du bouton d'appel flottant + bandeau tel mobile --- */
    // Ajout du bandeau téléphone en haut (visible uniquement sur mobile)
    const bandeauTel = document.createElement('a');
    bandeauTel.href = 'tel:+33781222522';
    bandeauTel.className = 'bandeau-tel-mobile';
    bandeauTel.setAttribute('aria-label', 'Appeler IPP Renovare');
    bandeauTel.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg> Appeler maintenant : 07 81 22 25 22';
    document.body.insertBefore(bandeauTel, document.body.firstChild);

    // Ajout du bouton d'appel flottant en bas à droite (visible uniquement sur mobile)
    const boutonFlottant = document.createElement('a');
    boutonFlottant.href = 'tel:+33781222522';
    boutonFlottant.className = 'bouton-appel-flottant';
    boutonFlottant.setAttribute('aria-label', 'Appeler IPP Renovare');
    boutonFlottant.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg> Appeler';
    document.body.appendChild(boutonFlottant);

    /* --- 1. Header : ajoute une classe quand on scrolle pour effet visuel --- */
    const header = document.querySelector('.header');
    if (header) {
        const surveillerScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        };
        window.addEventListener('scroll', surveillerScroll, { passive: true });
        surveillerScroll();
    }

    /* --- 2. Menu mobile (bouton burger) --- */
    const burger = document.querySelector('.menu-burger');
    const navLiens = document.querySelector('.nav-liens');
    if (burger && navLiens) {
        burger.addEventListener('click', () => {
            burger.classList.toggle('ouvert');
            navLiens.classList.toggle('ouvert');
        });
        // Refermer le menu quand on clique sur un lien
        navLiens.querySelectorAll('a').forEach(lien => {
            lien.addEventListener('click', () => {
                burger.classList.remove('ouvert');
                navLiens.classList.remove('ouvert');
            });
        });
    }

    /* --- 3. Animations au scroll (fade-in quand l'élément devient visible) --- */
    const mouvementReduit = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const elementsAnimes = document.querySelectorAll('.fade-in');

    // Effet domino : dans une même grille, les cartes apparaissent l'une après l'autre
    if (!mouvementReduit) {
        document.querySelectorAll('.grille-services, .blog-grille, .galerie-grille, .benefices, .materiaux, .tarifs, .timeline, .grille').forEach(grille => {
            grille.querySelectorAll(':scope > .fade-in').forEach((el, i) => {
                el.style.transitionDelay = Math.min(i * 90, 540) + 'ms';
                el.dataset.delaiDomino = '1';
            });
        });
    }

    if ('IntersectionObserver' in window && elementsAnimes.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                    // Une fois l'entrée jouée, on retire le délai pour que le survol reste réactif
                    if (entry.target.dataset.delaiDomino) {
                        setTimeout(() => { entry.target.style.transitionDelay = ''; }, 1500);
                    }
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });

        elementsAnimes.forEach(el => observer.observe(el));
    } else {
        elementsAnimes.forEach(el => el.classList.add('visible'));
    }

    /* --- 3b. Parallaxe léger sur le hero (le contenu défile un peu moins vite) --- */
    const heroContenu = document.querySelector('.hero-contenu');
    if (heroContenu && !mouvementReduit) {
        let ticket = false;
        window.addEventListener('scroll', () => {
            if (!ticket) {
                requestAnimationFrame(() => {
                    const y = window.scrollY;
                    if (y < window.innerHeight) {
                        heroContenu.style.transform = 'translateY(' + (y * 0.18) + 'px)';
                        heroContenu.style.opacity = Math.max(1 - y / (window.innerHeight * 0.9), 0);
                    }
                    ticket = false;
                });
                ticket = true;
            }
        }, { passive: true });
    }

    /* --- 3c. Barre de progression de lecture (uniquement sur les articles) --- */
    const contenuArticle = document.querySelector('.article-contenu');
    if (contenuArticle && !mouvementReduit) {
        const barre = document.createElement('div');
        barre.className = 'progression-lecture';
        document.body.appendChild(barre);
        window.addEventListener('scroll', () => {
            const hauteurTotale = document.documentElement.scrollHeight - window.innerHeight;
            const progression = hauteurTotale > 0 ? (window.scrollY / hauteurTotale) * 100 : 0;
            barre.style.width = progression + '%';
        }, { passive: true });
    }

    /* --- 4. Compteurs animés (chiffres clés du bandeau confiance) --- */
    const compteurs = document.querySelectorAll('[data-compteur]');
    if (compteurs.length > 0 && 'IntersectionObserver' in window) {
        const animerCompteur = (el) => {
            const cible = parseInt(el.dataset.compteur, 10);
            const suffixe = el.dataset.suffixe || '';
            const duree = 1800;
            const debut = performance.now();

            const tick = (maintenant) => {
                const progres = Math.min((maintenant - debut) / duree, 1);
                const valeur = Math.floor(progres * cible);
                el.textContent = valeur + suffixe;
                if (progres < 1) {
                    requestAnimationFrame(tick);
                } else {
                    el.textContent = cible + suffixe;
                }
            };
            requestAnimationFrame(tick);
        };

        const obsCompteurs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animerCompteur(entry.target);
                    obsCompteurs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        compteurs.forEach(c => obsCompteurs.observe(c));
    }

    /* --- 5. Filtres de la galerie de réalisations --- */
    const filtreBoutons = document.querySelectorAll('.filtre-btn');
    const galerieItems = document.querySelectorAll('[data-categorie]');
    if (filtreBoutons.length > 0) {
        filtreBoutons.forEach(btn => {
            btn.addEventListener('click', () => {
                const filtre = btn.dataset.filtre;
                filtreBoutons.forEach(b => b.classList.remove('actif'));
                btn.classList.add('actif');

                galerieItems.forEach(item => {
                    if (filtre === 'tous' || item.dataset.categorie === filtre) {
                        item.style.display = '';
                        setTimeout(() => item.style.opacity = '1', 10);
                    } else {
                        item.style.opacity = '0';
                        setTimeout(() => item.style.display = 'none', 300);
                    }
                });
            });
        });
    }

    /* --- 6. Comparateur avant/après (slider sur photo de chantier) --- */
    document.querySelectorAll('.comparateur').forEach(comparateur => {
        const apres = comparateur.querySelector('.comparateur-apres');
        const poignee = comparateur.querySelector('.comparateur-poignee');
        let estActif = false;

        const deplacer = (clientX) => {
            const rect = comparateur.getBoundingClientRect();
            let pos = ((clientX - rect.left) / rect.width) * 100;
            pos = Math.max(0, Math.min(100, pos));
            apres.style.clipPath = `inset(0 0 0 ${pos}%)`;
            poignee.style.left = pos + '%';
        };

        comparateur.addEventListener('mousedown', (e) => { estActif = true; deplacer(e.clientX); });
        window.addEventListener('mousemove', (e) => { if (estActif) deplacer(e.clientX); });
        window.addEventListener('mouseup', () => { estActif = false; });

        comparateur.addEventListener('touchstart', (e) => { estActif = true; deplacer(e.touches[0].clientX); }, { passive: true });
        window.addEventListener('touchmove', (e) => { if (estActif) deplacer(e.touches[0].clientX); }, { passive: true });
        window.addEventListener('touchend', () => { estActif = false; });
    });

    /* --- 7. Formulaire de contact (validation côté navigateur) --- */
    const formulaire = document.querySelector('#formulaire-devis');
    if (formulaire) {
        const message = formulaire.querySelector('.formulaire-message');

        formulaire.addEventListener('submit', (e) => {
            // Vérification basique avant envoi
            const champsObligatoires = formulaire.querySelectorAll('[required]');
            let tousValides = true;
            champsObligatoires.forEach(champ => {
                if (!champ.value.trim()) {
                    champ.style.borderColor = 'var(--rouge)';
                    tousValides = false;
                } else {
                    champ.style.borderColor = '';
                }
            });

            if (!tousValides) {
                e.preventDefault();
                if (message) {
                    message.className = 'formulaire-message erreur';
                    message.textContent = 'Merci de remplir tous les champs obligatoires.';
                }
            }
            // Si tous valides, le formulaire s'envoie (Netlify Forms gère la suite)
        });
    }

    /* --- 8. Marquer le lien actif dans la navigation --- */
    const cheminActuel = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-liens a').forEach(lien => {
        const href = lien.getAttribute('href');
        if (href === cheminActuel || (cheminActuel === '' && href === 'index.html')) {
            lien.classList.add('actif');
        }
    });

});
