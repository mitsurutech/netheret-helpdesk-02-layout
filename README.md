# Netheret help desk, step 02: layout

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step gives every page the same layout: a Jinja base template, a stylesheet
and a menu, built so that everybody can use it.

## What this step adds

- `helpdesk/templates/base.html`: the layout every page shares. Pages
  `extend` it and fill in the `title` and `content` blocks.
- `helpdesk/templates/home.html`: the home page, now a template.
- `helpdesk/static/css/style.css`: plain CSS, with the colours as variables.
- An accessible structure from the start: `lang="en-GB"`, a skip link,
  `header`, `nav`, `main` and `footer` landmarks, `aria-current` on the menu
  link for the page you are on, and a thick yellow focus ring.

## Run it

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Open http://127.0.0.1:5000. Press Tab once: the "Skip to main content" link
appears. Press Enter and the focus jumps past the menu.

## What to look at

- `{% extends "base.html" %}` and `{% block content %}` in `home.html`.
- The `nav_link` macro in `base.html`: one place that writes a menu link.
- `url_for('static', ...)`: Flask builds the address of the CSS file for us.
- The `:focus-visible` rule and `.skip-link` in `style.css`.

## Learn this step

This is step 2 of 16 of **Task 2. Developing the solution**, a free series of T Level Digital Software Development
lessons that builds the Netheret help desk in agile sprints with Python and Flask. Read the lesson for this step:
[Page layout with Jinja templates and CSS](https://mitsurutech.co.uk/resources/t-level/dsd-t2-02-layout).

- Previous step: [step 01, setting up a flask project](https://github.com/mitsurutech/netheret-helpdesk-01-setup)
- Next step: [step 03, the database with flask-sqlalchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- [Every free T Level Digital lesson](https://mitsurutech.co.uk/resources/t-level)
- [Teach these lessons to your class on MitsuruTech](https://mitsurutech.co.uk/learning), [see the pricing](https://mitsurutech.co.uk/pricing) or
  [start a free year for your college](https://mitsurutech.co.uk/signup)

## About

Written by [Mitsuru Technologies](https://mitsurutech.co.uk) (MitsuruTech) as a teaching example for T Level Digital
Software Development. The Netheret IT Support Solutions brief is from Pearson's sample assessment material; this code
and its notes are our own, and are not published, endorsed or approved by Pearson or the Department for Education.
'T Level' is a registered trade mark of the Department for Education.

