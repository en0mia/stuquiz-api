# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 22/05/23
import mysql.connector
from flask import current_app, g


def get_db():
    if 'db' not in g:
        db = mysql.connector.connect(
            host=current_app.config.get('MYSQL_HOST'),
            user=current_app.config.get('MYSQL_USER'),
            password=current_app.config.get('MYSQL_PASSWORD'),
            database=current_app.config.get('MYSQL_DATABASE')
        )
        g.db = db
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_cursor():
    return get_db().cursor()
