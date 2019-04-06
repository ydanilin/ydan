from flask import Flask
from routes.base import base
from routes.articles import articles


def create_app():
    app = Flask(__name__)

    app.register_blueprint(base)
    app.register_blueprint(articles)

    return app


app = create_app()
