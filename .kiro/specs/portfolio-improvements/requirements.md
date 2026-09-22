# Requirements Document

## Introduction

Ce document décrit les améliorations à apporter au portfolio personnel de Wassim
(`index.html` — Single Page Application avec Tailwind CDN).
Les améliorations sont regroupées en trois niveaux de priorité :
**Critique** (dysfonctionnements bloquants), **Contenu/UX** (expérience et complétude),
et **Technique** (qualité de code et accessibilité).

## Glossary

- **Portfolio** : La page `index.html` constituant le portfolio personnel de Wassim.
- **Nav** : La barre de navigation fixe en haut de page.
- **Menu_Mobile** : Le menu de navigation affiché sur les écrans de largeur inférieure à 768 px.
- **Formulaire_Contact** : Le formulaire HTML de la section `#contact` soumis via Formspree.
- **Section_Skills** : La section `#skills` listant les compétences techniques par catégorie.
- **Section_Projets** : La section `#projects` listant les projets logiciels et embarqués.
- **Section_Experience** : Une nouvelle section présentant les expériences professionnelles.
- **Section_Langues** : Une nouvelle section listant les langues parlées et leurs niveaux.
- **Head** : L'élément `<head>` du document HTML.
- **Carte_Projet** : Un composant visuel représentant un projet dans la Section_Projets.
- **Image_Hero** : L'image de fond de la section principale (`#home`).

## Requirements

### Requirement 1: Lien GitHub dans la navigation

**User Story:** En tant que visiteur, je veux cliquer sur l'icône GitHub dans la nav pour accéder
au profil GitHub de Wassim, afin de consulter l'ensemble de ses dépôts publics.

#### Acceptance Criteria

1. WHEN un visiteur clique sur l'icône GitHub dans la Nav, THE Portfolio SHALL ouvrir l'URL
   `https://github.com/king-wassim` dans un nouvel onglet.
2. THE Nav SHALL afficher l'icône GitHub avec l'attribut `href` pointant vers
   `https://github.com/king-wassim` et non vers `#`.
3. THE Nav SHALL ajouter les attributs `target="_blank"` et `rel="noopener noreferrer"` sur
   ce lien pour garantir la sécurité de l'ouverture en nouvel onglet.

### Requirement 2: Navigation mobile (menu hamburger)

**User Story:** En tant que visiteur sur mobile, je veux accéder à tous les liens de navigation
sans avoir à scroller, afin de naviguer rapidement entre les sections du portfolio.

#### Acceptance Criteria

1. WHEN la largeur de l'écran est inférieure à 768 px, THE Portfolio SHALL afficher un bouton
   hamburger dans la Nav à la place du menu horizontal.
2. WHEN un visiteur clique sur le bouton hamburger, THE Menu_Mobile SHALL s'afficher en
   superposition au-dessus du contenu principal avec les liens : Home, About, Skills, Projects,
   Contact.
3. WHEN un visiteur clique sur un lien du Menu_Mobile, THE Menu_Mobile SHALL se fermer
   immédiatement après la navigation.
4. WHEN un visiteur clique en dehors du Menu_Mobile alors qu'il est ouvert, THE Menu_Mobile
   SHALL se fermer.
5. WHILE le Menu_Mobile est ouvert, THE Portfolio SHALL empêcher le scroll de la page
   principale (`overflow: hidden` sur le body).
6. THE Menu_Mobile SHALL respecter le thème "Digital Blueprint" : fond `surface-container`
   à 95 % d'opacité avec `backdrop-blur`, liens en `font-headline`.

### Requirement 3: Formulaire de contact fonctionnel

**User Story:** En tant que visiteur, je veux envoyer un message à Wassim via le formulaire
de contact, afin de pouvoir prendre contact sans quitter la page.

#### Acceptance Criteria

1. WHEN un visiteur soumet le Formulaire_Contact avec un nom, un email valide et un message
   non vide, THE Portfolio SHALL envoyer les données à l'endpoint Formspree
   `https://formspree.io/f/mykbjvzl` via une requête POST asynchrone (fetch API).
2. WHEN la soumission Formspree réussit (réponse HTTP 200), THE Portfolio SHALL remplacer
   le Formulaire_Contact par un message de confirmation visible indiquant que le message a
   bien été envoyé.
3. IF la soumission Formspree échoue (code HTTP différent de 200 ou erreur réseau), THEN THE
   Portfolio SHALL afficher un message d'erreur lisible invitant le visiteur à réessayer ou à
   contacter directement par email.
4. WHILE la soumission est en cours, THE Formulaire_Contact SHALL désactiver le bouton
   d'envoi et afficher un indicateur de chargement pour prévenir les soumissions multiples.
5. IF un visiteur tente de soumettre le Formulaire_Contact avec un champ requis vide, THEN THE
   Portfolio SHALL afficher un message de validation sur le champ concerné sans soumettre
   le formulaire.

### Requirement 4: Remplacement de l'image hero externe

**User Story:** En tant que visiteur, je veux que le fond de la section principale se charge
de manière fiable, afin que la présentation visuelle du portfolio ne soit pas dégradée par une
panne d'un CDN externe.

#### Acceptance Criteria

1. THE Image_Hero SHALL être une ressource locale présente dans le répertoire du projet,
   et non une URL hébergée sur un CDN Google externe (`lh3.googleusercontent.com`).
2. THE Image_Hero SHALL posséder un attribut `alt` descriptif conforme aux normes WCAG 2.1 AA,
   décrivant le contenu de l'image pour les lecteurs d'écran.
3. IF l'Image_Hero ne peut pas être chargée, THEN THE Portfolio SHALL afficher un fond de
   couleur `surface-container-high` en remplacement, de sorte que la section reste visuellement
   cohérente.

### Requirement 5: Correction des attributs alt manquants

**User Story:** En tant que visiteur utilisant un lecteur d'écran, je veux que toutes les images
du portfolio possèdent une description textuelle, afin d'accéder au même contenu que les
visiteurs voyants.

#### Acceptance Criteria

1. THE Portfolio SHALL remplacer chaque attribut `data-alt` par un attribut `alt` valide sur
   toutes les balises `<img>` du document.
2. THE Portfolio SHALL garantir qu'aucune balise `<img>` ne présente un attribut `alt` absent,
   sauf pour les images purement décoratives qui recevront `alt=""`.
3. WHEN un lecteur d'écran parcourt une Carte_Projet, THE Portfolio SHALL lui fournir un texte
   alternatif décrivant le contenu de la capture d'écran du projet.

### Requirement 6: Suppression du doublon de balise Material Symbols

**User Story:** En tant que développeur maintenant le code, je veux un `<head>` sans
ressources dupliquées, afin d'éviter des requêtes réseau inutiles et des comportements
inattendus.

#### Acceptance Criteria

1. THE Head SHALL contenir exactement une seule balise `<link>` chargeant la police
   Material Symbols Outlined.
2. THE Portfolio SHALL continuer à afficher correctement toutes les icônes Material Symbols
   après la suppression du doublon.

### Requirement 7: Ajout des meta tags SEO et Open Graph

**User Story:** En tant que recruteur qui partage le lien du portfolio sur LinkedIn ou Twitter,
je veux voir une prévisualisation enrichie (titre, description, image), afin d'identifier
rapidement le profil de Wassim.

#### Acceptance Criteria

1. THE Head SHALL contenir une balise `<meta name="description">` dont le contenu décrit
   Wassim en 150 à 160 caractères, mentionnant son statut d'étudiant ingénieur, l'INSAT et ses
   spécialités (logiciel et systèmes embarqués).
2. THE Head SHALL contenir les balises Open Graph suivantes : `og:title`, `og:description`,
   `og:type` (valeur `"website"`), et `og:url` avec l'URL publique du portfolio.
3. WHERE une image de prévisualisation est disponible localement, THE Head SHALL contenir une
   balise `og:image` pointant vers cette image de dimensions minimales 1200 × 630 px.
4. THE Head SHALL contenir les balises Twitter Card équivalentes (`twitter:card`,
   `twitter:title`, `twitter:description`) pour assurer la compatibilité avec la prévisualisation
   Twitter/X.

### Requirement 8: Complétion de la section Skills

**User Story:** En tant que recruteur consultant le portfolio, je veux voir la liste complète
des technologies maîtrisées par Wassim dans la section Skills, afin d'évaluer ses compétences
sans avoir à lire chaque description de projet.

#### Acceptance Criteria

1. THE Section_Skills SHALL afficher React dans une catégorie "Web / Frameworks" ou
   équivalente.
2. THE Section_Skills SHALL afficher NestJS dans une catégorie "Backend" ou "Web / Frameworks".
3. THE Section_Skills SHALL afficher Flutter dans une catégorie "Mobile" ou "Cross-platform".
4. THE Section_Skills SHALL afficher TypeScript dans la catégorie "Programming" aux côtés
   de JavaScript.
5. THE Section_Skills SHALL organiser les compétences en catégories cohérentes avec les
   projets présentés dans la Section_Projets, de sorte qu'aucune technologie visible dans les
   badges de projet ne soit absente de la Section_Skills.

### Requirement 9: Ajout d'une section Expérience professionnelle

**User Story:** En tant que recruteur, je veux consulter les expériences professionnelles de
Wassim (stages, bénévolat, projets associatifs), afin d'évaluer son exposition au monde
professionnel au-delà des projets académiques.

#### Acceptance Criteria

1. THE Portfolio SHALL contenir une Section_Experience placée entre la section About et la
   section Skills dans l'ordre de navigation de la page.
2. THE Section_Experience SHALL afficher chaque expérience avec au minimum : l'intitulé du
   poste, le nom de l'organisation, la période (date de début et date de fin ou "Présent"), la
   localisation, et une description des responsabilités ou réalisations.
3. WHEN la Section_Experience ne contient aucune entrée, THE Portfolio SHALL masquer la
   section entièrement plutôt que d'afficher un état vide visible.
4. THE Section_Experience SHALL respecter le Design System "Digital Blueprint" : cartes
   `surface-container-high` avec bordure gauche de couleur `tertiary`, typographie `font-headline`.

### Requirement 10: Ajout d'une section Langues parlées

**User Story:** En tant que recruteur international, je veux connaître les langues parlées par
Wassim et son niveau dans chacune, afin d'évaluer sa capacité à travailler dans un contexte
multilingue.

#### Acceptance Criteria

1. THE Portfolio SHALL contenir une Section_Langues visible depuis la page, avec au minimum
   les langues : Arabe (langue maternelle), Français et Anglais.
2. THE Section_Langues SHALL afficher le niveau de chaque langue selon le référentiel CECRL
   (A1 à C2) ou un équivalent descriptif (Natif, Courant, Intermédiaire).
3. THE Section_Langues SHALL être intégrée visuellement dans la section About ou la section
   Skills, sans créer une entrée de navigation dédiée, afin de ne pas alourdir la structure
   de la page.

### Requirement 11: Liens Live Demo sur les projets déployés

**User Story:** En tant que visiteur, je veux accéder à une démonstration en ligne d'un projet
directement depuis sa carte, afin d'en évaluer le résultat sans avoir à cloner le dépôt.

#### Acceptance Criteria

1. WHERE un projet dispose d'une URL de démo publique, THE Carte_Projet SHALL afficher un
   lien "Live Demo" aux côtés du lien GitHub existant.
2. WHEN un visiteur clique sur "Live Demo", THE Portfolio SHALL ouvrir l'URL de démo dans un
   nouvel onglet avec `target="_blank"` et `rel="noopener noreferrer"`.
3. THE Carte_Projet SHALL différencier visuellement le lien "Live Demo" du lien "GitHub" :
   le lien "Live Demo" utilisera la couleur `primary` et l'icône `open_in_new`, tandis que le
   lien "GitHub" conserve sa couleur `tertiary` existante.
4. WHERE un projet ne dispose pas de démo publique, THE Carte_Projet SHALL ne pas afficher
   de lien "Live Demo", de sorte qu'aucun lien brisé n'apparaisse dans le Portfolio.
