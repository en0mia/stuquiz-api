# @author Lorenzo Varese
# @created 2023-06-30

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
        return self.update(query, university.name)

    def select_university_by_id(self, university_id: int) -> University:
        query = "SELECT * FROM university WHERE id = %s"
        return self.select(query, university_id)
