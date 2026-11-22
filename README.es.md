# Servicio de asistencia de Netheret, paso 02: diseño de página

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un ejemplo para enseñar. En dieciséis pasos construimos una aplicación web de servicio de asistencia para Netheret, una empresa inventada que da soporte informático a pequeñas empresas. Este paso da a todas las páginas el mismo diseño: una plantilla base de Jinja, una hoja de estilos y un menú, pensados para que todo el mundo pueda usarlos.

## Qué añade este paso

- `helpdesk/templates/base.html`: el diseño que comparten todas las páginas. Las páginas
  lo amplían con `extend` y rellenan los bloques `title` y `content`.
- `helpdesk/templates/home.html`: la página de inicio, ahora como plantilla.
- `helpdesk/static/css/style.css`: CSS sencillo, con los colores como variables.
- Una estructura accesible desde el principio: `lang="en-GB"`, un enlace para saltar al contenido,
  las regiones `header`, `nav`, `main` y `footer`, `aria-current` en el enlace del menú
  de la página en la que estás y un contorno de foco amarillo y grueso.

## Ejecútalo

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

Abre http://127.0.0.1:5000. Pulsa Tab una vez: aparece el enlace "Skip to main content".
Pulsa Intro y el foco salta por encima del menú.

## En qué fijarse

- `{% extends "base.html" %}` y `{% block content %}` en `home.html`.
- La macro `nav_link` en `base.html`: un solo sitio que escribe un enlace del menú.
- `url_for('static', ...)`: Flask construye por nosotros la dirección del archivo CSS.
- La regla `:focus-visible` y `.skip-link` en `style.css`.

## Aprende este paso

Este es el paso 2 de 16 de **Task 2. Developing the solution**, una serie gratuita de lecciones de T Level Digital Software Development, en inglés, que construye el servicio de asistencia de Netheret en sprints ágiles con Python y Flask. Lee la lección de este paso:
[Diseño de página con plantillas Jinja y CSS](https://mitsurutech.co.uk/resources/t-level/dsd-t2-02-layout).

- Paso anterior: [paso 01, preparar un proyecto Flask](https://github.com/mitsurutech/netheret-helpdesk-01-setup)
- Paso siguiente: [paso 03, la base de datos con Flask-SQLAlchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- [Todas las lecciones gratuitas de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseña estas lecciones a tu clase en MitsuruTech](https://mitsurutech.co.uk/es/learning), [mira los precios](https://mitsurutech.co.uk/es/pricing) o
  [empieza un año gratis para tu centro](https://mitsurutech.co.uk/es/signup)

## Acerca de

Escrito por [Mitsuru Technologies](https://mitsurutech.co.uk/es) (MitsuruTech) como ejemplo para enseñar T Level Digital
Software Development. El encargo de Netheret IT Support Solutions procede del material de evaluación de muestra de Pearson; este código
y sus notas son nuestros, y no los publica, respalda ni aprueba Pearson ni el Department for Education.
"T Level" es una marca registrada del Department for Education.
