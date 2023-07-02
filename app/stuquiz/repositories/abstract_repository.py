# @author Lorenzo Varese
# @created 2023-06-30

from typing import Optional, List
from mysql.connector import DatabaseError
from mysql.connector.cursor import MySQLCursor
from mysql.connector.types import RowType

from app.stuquiz.utils.database_provider import DatabaseProvider


class AbstractRepository(object):
    """This is the base repository class.
    All the repositories inherit the methods from this class.
    """
    def __init__(self, db_provider: Optional[DatabaseProvider] = None):
        db_provider = db_provider or DatabaseProvider()
        self.db = db_provider.get_db()

    def execute(self, query, args, cursor: Optional[MySQLCursor] = None):
        """Execute the given query.
        :param query: the query to execute.
        :param args: the args to substitute to the query. Note that the substitution is handled by the
            connector, so it is injection-safe.
        :param cursor: the cursor to use | None
        :return: True | False in case of database error.
            If the latter is the case, this method automatically performs a rollback of the last executed query.
        """
        cursor = cursor or self.db.cursor(buffered=True)
        try:
            cursor.execute(query, args)
        except DatabaseError:
            self.db.rollback()
            return False
        return True

    def select(self, query, args) -> Optional[List[RowType]]:
        """Perform a SELECT query.
        :param query: the query to perform
        :param args: the args to substitute to the query. Note that the substitution is handled by the
            connector, so it is injection-safe.
        :return: the result of the query.
        """
        cursor = self.db.cursor(buffered=True)
        if not self.execute(query, args, cursor):
            return None

        return cursor.fetchall()

    def insert(self, query, args) -> bool:
        """Perform a INSERT query.
        :param query: the query to perform
        :param args: the args to substitute to the query. Note that the substitution is handled by the
            connector, so it is injection-safe.
        :return: True | False in case of database error.
        """
        if not self.execute(query, args):
            return False
        self.db.commit()
        return True

    def update(self, query, args) -> bool:
        """Perform a UPDATE query.
        :param query: the query to perform
        :param args: the args to substitute to the query. Note that the substitution is handled by the
            connector, so it is injection-safe.
        :return: True | False in case of database error.
        """
        if not self.execute(query, args):
            return False
        self.db.commit()
        return True

    def delete(self, query, args):
        """Perform a DELETE query.
        :param query: the query to perform
        :param args: the args to substitute to the query. Note that the substitution is handled by the
            connector, so it is injection-safe.
        :return: True | False in case of database error.
        """
        if not self.execute(query, args):
            return False
        self.db.commit()
        return True