from flask import Flask
from root import root
from articles import articles
from scratches import scratches


def create_app():
    app = Flask(__name__)

    app.register_blueprint(root)
    app.register_blueprint(articles, url_prefix='/articles')
    app.register_blueprint(scratches, url_prefix='/scratches')

    return app


app = create_app()
