from flask import Blueprint


root = Blueprint('root', __name__, template_folder='templates')

from . import routes
