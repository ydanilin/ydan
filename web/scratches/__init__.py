from flask import Blueprint


scratches = Blueprint(
    'scratches', __name__, template_folder='templates', static_folder='static'
)

from . import routes
