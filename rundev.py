from web import create_app
from werkzeug.serving import run_simple


instance = create_app()
instance.debug = True


if __name__ == '__main__':
    run_simple('localhost', 5000, instance,
               use_reloader=True, use_debugger=True, use_evalex=True)
