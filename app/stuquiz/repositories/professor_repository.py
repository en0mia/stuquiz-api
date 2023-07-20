# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from app.stuquiz.entities.professor import Professor
from app.stuquiz.repositories.abstract_repository import AbstractRepository


class ProfessorRepository(AbstractRepository):
    def create_professor(self, professor: Professor) -> bool:
        """Inserts the professor into the database.
        :param professor: The Professor to insert
        :return: bool
        """
        query = "INSERT INTO professor(id, name) VALUES(%s, %s)"
        return self.insert(query, (professor.id, professor.name))

    def update_professor(self, professor: Professor) -> bool:
        """Updates the professor into the database.
        :param professor: The Professor to update
        :return: bool
        """
        query = "UPDATE professor SET name = %s WHERE id = %s"
        return self.update(query, (professor.name, professor.id))

    def delete_professor(self, professor: Professor) -> bool:
        """Deletes the professor from the database.
        :param professor: The Professor to delete
        :return: bool
        """
        query = "DELETE FROM professor WHERE id = %s"
        return self.delete(query, (professor.id,))

    def select_professor_by_id(self, professor_id: str) -> Optional[Professor]:
        """Returns the professor with the provided id.
        :param professor_id: Professor's ID
        :return: Professor | None
        """
        query = "SELECT id, name FROM professor WHERE id = %s"
        result = self.select(query, (professor_id,))
        return Professor(*result[0]) if result and len(result) > 0 else None
