from flask import render_template
from . import scratches


@scratches.route("/nginx-uwsgi-setup")
def show_nginx_setups():
    return render_template(
        'nginx_uwsgi_setup.html', logo_text='Nginx+uWSGI setups'
    )
