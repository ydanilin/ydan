from flask import Blueprint, render_template


base = Blueprint('base', __name__)


@base.route("/")
def home():
    # return 'That will be Gan Eden here!'
    return render_template('root.html')
