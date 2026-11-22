# Centre d'assistance Netheret, étape 02 : mise en page

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un exemple pour enseigner. En seize étapes, nous construisons une application web de centre d'assistance pour Netheret, une entreprise imaginaire qui s'occupe de l'informatique de petites entreprises. Cette étape donne la même mise en page à toutes les pages : un gabarit de base Jinja, une feuille de style et un menu, conçus pour que tout le monde puisse s'en servir.

## Ce que cette étape ajoute

- `helpdesk/templates/base.html` : la mise en page que partagent toutes les pages. Les pages
  l'étendent avec `extend` et remplissent les blocs `title` et `content`.
- `helpdesk/templates/home.html` : la page d'accueil, devenue un gabarit.
- `helpdesk/static/css/style.css` : du CSS simple, avec les couleurs en variables.
- Une structure accessible dès le départ : `lang="en-GB"`, un lien d'évitement,
  les repères `header`, `nav`, `main` et `footer`, `aria-current` sur le lien du menu
  de la page où vous êtes, et un épais contour jaune pour le focus.

## Lancer l'application

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Ouvrez http://127.0.0.1:5000. Appuyez une fois sur Tab : le lien « Skip to main content »
apparaît. Appuyez sur Entrée et le focus saute par-dessus le menu.

## À regarder

- `{% extends "base.html" %}` et `{% block content %}` dans `home.html`.
- La macro `nav_link` dans `base.html` : un seul endroit qui écrit un lien du menu.
- `url_for('static', ...)` : Flask construit pour nous l'adresse du fichier CSS.
- La règle `:focus-visible` et `.skip-link` dans `style.css`.

## Apprendre cette étape

Voici l'étape 2 sur 16 de **Task 2. Developing the solution**, une série gratuite de leçons de T Level Digital Software Development, en anglais, qui construit le centre d'assistance Netheret en sprints agiles avec Python et Flask. Lisez la leçon de cette étape :
[Mise en page avec les gabarits Jinja et le CSS](https://mitsurutech.co.uk/resources/t-level/dsd-t2-02-layout).

- Étape précédente : [étape 01, mettre en place un projet Flask](https://github.com/mitsurutech/netheret-helpdesk-01-setup)
- Étape suivante : [étape 03, la base de données avec Flask-SQLAlchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- [Toutes les leçons gratuites de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseigner ces leçons à votre classe sur MitsuruTech](https://mitsurutech.co.uk/fr/learning), [voir les tarifs](https://mitsurutech.co.uk/fr/pricing) ou
  [commencer une année gratuite pour votre établissement](https://mitsurutech.co.uk/fr/signup)

## À propos

Écrit par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) (MitsuruTech) comme exemple pédagogique pour le T Level Digital
Software Development. Le cahier des charges Netheret IT Support Solutions provient du matériel d'évaluation type de Pearson ; ce code
et ses notes sont les nôtres, et ne sont ni publiés, ni soutenus, ni approuvés par Pearson ou le Department for Education.
« T Level » est une marque déposée du Department for Education.
