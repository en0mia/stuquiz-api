# @author Lorenzo Varese
# @created 2023-06-30

from flask import g, current_app
import mysql.connector


class DatabaseProvider(object):
    """This class is used to connect to the database.
    It is particularly useful to mock the database object when testing.
    """
    @staticmethod
    def get_db():
        """This method acts as a singleton provider for the database object.
        :return: the database instance.
        """
        if 'db' not in g:
            db = mysql.connector.connect(
                host=current_app.config.get('MYSQL_HOST'),
                user=current_app.config.get('MYSQL_USER'),
                password=current_app.config.get('MYSQL_PASSWORD'),
                database=current_app.config.get('MYSQL_DATABASE')
            )
            g.db = db
        return g.db

    @staticmethod
    def close_db():
        """Unsets the db object and closes the connection if it was active."""
        db = g.pop('db', None)
        if db is not None:
            db.close()