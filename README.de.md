# Netheret-Helpdesk, Schritt 02: Layout

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Ein Beispiel für den Unterricht. In sechzehn Schritten bauen wir eine Helpdesk-Webanwendung für Netheret, ein erfundenes Unternehmen, das die IT kleiner Firmen betreut. Dieser Schritt gibt allen Seiten dasselbe Layout: eine Jinja-Basisvorlage, ein Stylesheet und ein Menü, so gebaut, dass alle sie nutzen können.

## Was dieser Schritt hinzufügt

- `helpdesk/templates/base.html`: das Layout, das sich alle Seiten teilen. Seiten
  erweitern es mit `extend` und füllen die Blöcke `title` und `content`.
- `helpdesk/templates/home.html`: die Startseite, jetzt als Vorlage.
- `helpdesk/static/css/style.css`: schlichtes CSS mit den Farben als Variablen.
- Eine barrierefreie Struktur von Anfang an: `lang="en-GB"`, ein Sprunglink,
  die Landmarks `header`, `nav`, `main` und `footer`, `aria-current` am Menülink
  der Seite, auf der Sie sich befinden, und ein dicker gelber Fokusrahmen.

## Starten

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Öffnen Sie http://127.0.0.1:5000. Drücken Sie einmal die Tabulatortaste: Der Link „Skip to main content“
erscheint. Drücken Sie die Eingabetaste, und der Fokus springt über das Menü hinweg.

## Worauf Sie achten sollten

- `{% extends "base.html" %}` und `{% block content %}` in `home.html`.
- Das Makro `nav_link` in `base.html`: eine einzige Stelle, die einen Menülink schreibt.
- `url_for('static', ...)`: Flask baut für uns die Adresse der CSS-Datei.
- Die Regel `:focus-visible` und `.skip-link` in `style.css`.

## Diesen Schritt lernen

Dies ist Schritt 2 von 16 aus **Task 2. Developing the solution**, einer kostenlosen Reihe von Lektionen zu T Level Digital Software Development auf Englisch, die den Helpdesk von Netheret in agilen Sprints mit Python und Flask baut. Lesen Sie die Lektion zu diesem Schritt:
[Seitenlayout mit Jinja-Vorlagen und CSS](https://mitsurutech.co.uk/resources/t-level/dsd-t2-02-layout).

- Vorheriger Schritt: [Schritt 01, Ein Flask-Projekt einrichten](https://github.com/mitsurutech/netheret-helpdesk-01-setup)
- Nächster Schritt: [Schritt 03, Die Datenbank mit Flask-SQLAlchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- [Alle kostenlosen Lektionen zu T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Diese Lektionen mit Ihrer Klasse auf MitsuruTech unterrichten](https://mitsurutech.co.uk/de/learning), [die Preise ansehen](https://mitsurutech.co.uk/de/pricing) oder
  [ein kostenloses Jahr für Ihre Schule beginnen](https://mitsurutech.co.uk/de/signup)

## Über dieses Beispiel

Geschrieben von [Mitsuru Technologies](https://mitsurutech.co.uk/de) (MitsuruTech) als Unterrichtsbeispiel für T Level Digital
Software Development. Die Aufgabenstellung Netheret IT Support Solutions stammt aus dem Muster-Prüfungsmaterial von Pearson; dieser Code
und seine Erläuterungen sind unsere eigenen und werden weder von Pearson noch vom Department for Education veröffentlicht, unterstützt oder genehmigt.
„T Level“ ist eine eingetragene Marke des Department for Education.
