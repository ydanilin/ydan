import os
from flask import render_template, send_from_directory
from articles import articles


@articles.route("/declarative-testing-with-gabbi")
def declarative_testing():
    # return "Huj-huj!!!"
    # return render_template('articles/decl_testing/decl_testing.html')
    return render_template('decl_testing/decl_testing.html')


# this route is a fallback in case nginx is unable to send static
@articles.route("/<path:filepath>")
def send_static(filepath):
    dirname = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    return send_from_directory(f"static/{dirname}", filename)
