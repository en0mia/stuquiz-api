# @author Lorenzo Varese
# @created 2023-06-30

from app.stuquiz.repositories.abstract_repository import AbstractRepository
from app.stuquiz.entities.category import Category


class CategoryRepository(AbstractRepository):

    def create_category(self, category: Category) -> bool:
        query = "INSERT INTO category (name) VALUES (%s)"
        return self.insert(query, category.name)

    def delete_category(self, category: Category) -> bool:
        query = "DELETE FROM category WHERE id = %s"
        return self.delete(query, category.id)

    def update_category(self, category: Category) -> bool:
        query = "UPDATE category SET name = %s WHERE id = %s"
        return self.update(query, category.name, category.id)

    def select_category_by_id(self, category_id: int) -> Category:
        query = "SELECT * FROM category WHERE id = %s"
        return self.update(query, category_id)
