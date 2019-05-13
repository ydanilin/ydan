from flask import render_template
from scratches import scratches


@scratches.route("/nginx-uwsgi-setup")
def home():
    return render_template(
        'nginx_uwsgi_setup.html', logo_text='Nginx+uWSGI setups'
    )
