# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
from typing import Optional

from app.stuquiz.entities.admin import Admin
from app.stuquiz.repositories.abstract_repository import AbstractRepository


class AdminRepository(AbstractRepository):
    def select_admin_by_id(self, admin_id: str) -> Optional[Admin]:
        query = "SELECT id, username, email, password, salt FROM admin WHERE id = %s"
        result = self.select(query, admin_id)
        return Admin(*result[0]) if result and len(result) > 0 else None

    def select_admin_by_email(self, email: str) -> Optional[Admin]:
        query = "SELECT id, username, email, password, salt FROM admin WHERE email = %s"
        result = self.select(query, email)
        return Admin(*result[0]) if result and len(result) > 0 else None
