# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 22/05/23
import os
from flask import Flask
import toml

from app.stuquiz.routes.router import register_routes
from app.stuquiz.utils.database_provider import DatabaseProvider


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_file('../config.toml', load=toml.load)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    if 'MYSQL_PASSWORD' in os.environ:
        app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
    if 'SECRET_KEY' in os.environ:
        app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.teardown_appcontext
    def close_connection(exception=None):
        """On app teardown, close the database connection."""
        DatabaseProvider.close_db()

    register_routes(app)

    return app
