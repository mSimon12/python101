import os

from flask import Flask
from . import db
from . import auth
from . import blog

def create_app(test_config=None):
    """ Flask Constructor
        __name__ = the app needs to know where it’s located to set up some paths
        instance_relative_config=True tells the app that cfg files are relative to the instance folder outside flaskr.
    """
    app = Flask(__name__, instance_relative_config=True)

    """ sets some default configuration that the app will use
        SECRET_KEY is used by Flask and extensions to keep data safe. It should be set with a random value when deploying.
        DATABASE is the path where the SQLite database file will be saved. 
    """
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello_page():
        return "Hello World"

    db.init_app_db(app)

    app.register_blueprint(auth.bp)     # add Authentication blueprint
    app.register_blueprint(blog.bp)     # add Blog blueprint
    app.add_url_rule('/', endpoint='index')

    return app

