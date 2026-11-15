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

<!-- links -->
