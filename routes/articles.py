import os
from flask import Blueprint, render_template, send_from_directory


articles = Blueprint('articles', __name__)


@articles.route("/articles/declarative-testing-with-gabbi")
def declarative_testing():
    return render_template('articles/decl_testing/decl_testing.html')


# this route is a fallback in case nginx is unable to send static
@articles.route("/articles/<path:filepath>")
def send_static(filepath):
    dirname = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    return send_from_directory(f"static/articles/{dirname}", filename)
