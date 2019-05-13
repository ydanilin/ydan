from flask import render_template
from root import root


@root.route("/")
def home():
    return render_template('home.html', logo_text='Home')
