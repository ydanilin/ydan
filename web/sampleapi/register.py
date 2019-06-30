"""Implement load api from swagger using template import yam."""
import yaml
import connexion
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def connexion_register_blueprint(app, swagger_file, **kwargs):
    con = connexion.FlaskApp("api", app.instance_path)
    # env = Environment(loader=FileSystemLoader(
    #     app.config.get('SWAGGER_ROOT_TEMPLATE') or
    #     app.config['PROJECT_ROOT']
    # ))
    # swagger_string = env.get_template(swagger_file).render(**kwargs)
    # specification = yaml.safe_load(swagger_string)
    # api = super(connexion.FlaskApp, con).add_api(specification, **kwargs)
    api = super(connexion.FlaskApp, con).add_api(
        'web/sampleapi/main.yaml', **kwargs)
    app.register_blueprint(api.blueprint)
    return api
