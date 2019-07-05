from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from .root import root
from .root.models import db as root_db, User, Post
from .articles import articles
from .scratches import scratches
from .sampleapi.register import connexion_register_blueprint


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    root_db.init_app(app)
    migrate.init_app(app, root_db)
    login = LoginManager()
    login.login_view = 'login'
    login.init_app(app)

    app.register_blueprint(root)
    app.register_blueprint(articles, url_prefix='/articles')
    app.register_blueprint(scratches, url_prefix='/scratches')
    connexion_register_blueprint(app, 'sampleapi/main.yaml')

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.shell_context_processor
    def make_shell_context():
        return {'db': root_db, 'User': User, 'Post': Post}

    return app

# put models inside blueprints:
# https://stackoverflow.com/a/47964689
#
# migrate inside create_app():
# https://stackoverflow.com/a/29882346
