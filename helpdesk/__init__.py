"""The Netheret help desk web app.

create_app() builds the Flask app. Flask looks for a function with this
name when you run `flask --app helpdesk run`.
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Tidy the HTML that templates produce: drop the blank lines left by
    # {% ... %} tags.
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # Each part of the app is a blueprint: a group of pages in its own file.
    from . import main
    app.register_blueprint(main.bp)

    return app
