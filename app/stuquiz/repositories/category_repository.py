from app.stuquiz.repositories.abstract_repository import Repository
from app.stuquiz.entities.category import Category


class CategoryRepository(Repository):

    def insert(self, category: Category) -> bool:
        try:
            query = "INSERT INTO category (name) VALUES (%s)"
            values = (category.name)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error inserting category :", e)
            self.db.rollback()
            return False

        return True

    def delete(self, category: Category) -> bool:
        try:
            query = "DELETE FROM category WHERE id = %s"
            values = (category.id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error deleting category:", e)
            self.db.rollback()
            return False

        return True

    def update(self, category: Category) -> bool:
        try:
            query = "UPDATE category SET name = %s WHERE id = %s"
            values = (category.name, category.id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error updating category:", e)
            self.db.rollback()
            return False

        return True

    def select_by_id(self, category_id: int) -> Category:
        try:
            query = "SELECT * FROM category WHERE id = %s"
            values = (category_id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            category_data = cursor.fetchone()

            if category_data:
                category = Category(*category_data)
                return category
            else:
                return None
        except Exception as e:
            print("Error selecting category by ID:", e)
            return None
