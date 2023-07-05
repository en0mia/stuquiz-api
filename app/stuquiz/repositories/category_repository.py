# @author Lorenzo Varese
# @created 2023-06-30
from typing import Optional

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
        return self.update(query, (category.name, category.id))

    def select_category_by_id(self, category_id: str) -> Optional[Category]:
        query = "SELECT id, name FROM category WHERE id = %s"
        result = self.select(query, category_id)
        return Category(*result[0]) if result and len(result) > 0 else None

    def select_categories(self) -> list[Category]:
        query = 'SELECT id, name FROM category;'
        records = self.select(query, ())
        result = []

        if not records:
            return []

        for record in records:
            result.append(Category(*record))

        return result
