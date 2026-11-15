"""General pages that do not belong to one feature."""
from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    # render_template finds home.html in the templates folder.
    return render_template("home.html")
