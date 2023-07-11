# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
import hashlib
from typing import Optional

from flask import session

from app.stuquiz.entities.admin import Admin
from app.stuquiz.repositories.admin_repository import AdminRepository


class AdminModel(object):
    """The default length for the salt used to hash the participant's password.
    Remember that the salt length is fixed also in the database, so if you change the salt length here,
    it is important to remember to update it in the table definition.
    """
    PASSWORD_SALT_LENGTH = 20

    def __init__(self, admin_repository: Optional[AdminRepository] = None):
        self.admin_repository = admin_repository or AdminRepository()

    @staticmethod
    def hash_password(clear_password: str, salt: str) -> str:
        """Hashes the clear password using SHA256 algorithm.
        :param clear_password: the clear password to hash.
        :param salt: the salt to use.
        :return: the hash of the password obtained using the provided salt.
        """
        return hashlib.pbkdf2_hmac('sha256', clear_password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()

    @staticmethod
    def store_session(admin_id: str) -> None:
        """Stores the admin_id into the cookie session managed by the client.
        :param admin_id: Admin's id
        :return: void
        """
        session['admin_id'] = admin_id

    def get_admin_by_id(self, admin_id: str) -> Optional[Admin]:
        """Returns the admin with the provided id.
        :param admin_id: The admin's ID.
        :return: Admin | None if the ID does not exist.
        """
        return self.admin_repository.select_admin_by_id(admin_id)

    def login_admin(self, email: str, clear_password: str) -> Optional[str]:
        """Verifies admin's credentials and returns the corresponding admin ID.
        :param email: Admin's email.
        :param clear_password: Admin's password.
        :return: Admin ID | None if the credentials are invalid.
        """
        admin = self.admin_repository.select_admin_by_email(email)

        if admin is None:
            return None

        salt = admin.salt
        hashed_password = self.hash_password(clear_password, salt)

        admin = self.admin_repository.select_admin_by_email_password(email, hashed_password)

        if admin is None:
            return None
        return admin.id

    def is_admin_logged_in(self) -> bool:
        """Checks if the current user is an admin by getting their admin_id from the session and looking
        for it in the database.
        :return: bool
        """
        admin_id = session['admin_id'] if 'admin_id' in session else None

        if not admin_id:
            return False

        admin = self.get_admin_by_id(admin_id)

        return admin is not None
