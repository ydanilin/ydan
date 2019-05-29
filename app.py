from flask import Flask
from config import Config
from flask_migrate import Migrate
from root import root
from root.models import db as root_db
from articles import articles
from scratches import scratches


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    root_db.init_app(app)
    migrate.init_app(app, root_db)

    app.register_blueprint(root)
    app.register_blueprint(articles, url_prefix='/articles')
    app.register_blueprint(scratches, url_prefix='/scratches')

    return app

# put models inside blueprints:
# https://stackoverflow.com/a/47964689
#
# migrate inside create_app():
# https://stackoverflow.com/a/29882346
