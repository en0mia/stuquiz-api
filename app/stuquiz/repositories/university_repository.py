# @author Lorenzo Varese
# @created 2023-06-30
from typing import Optional

from app.stuquiz.repositories.abstract_repository import AbstractRepository
from app.stuquiz.entities.university import University


class UniversityRepository(AbstractRepository):

    def create_university(self, university: University) -> bool:
        query = "INSERT INTO university (name) VALUES (%s)"
        return self.insert(query, university.name)

    def delete_university(self, university: University) -> bool:
        query = "DELETE FROM university WHERE id = %s"
        return self.delete(query, university.id)

    def update_university(self, university: University) -> bool:
        query = "UPDATE university SET name = %s WHERE id = %s"
        return self.update(query, (university.name, university.id))

    def select_university_by_id(self, university_id: str) -> Optional[University]:
        query = "SELECT * FROM university WHERE id = %s"
        result = self.select(query, university_id)
        return University(*result[0]) if result and len(result) > 0 else None

    def select_universities(self) -> list[University]:
        query = 'SELECT id, name FROM university;'
        records = self.select(query, ())
        result = []

        if not records:
            return []

        for record in records:
            result.append(University(*record))

        return result
