from app.stuquiz.repositories.abstract_repository import Repository
from app.stuquiz.entities.university import University


class UniversityRepository(Repository):

    def insert(self, university: University) -> bool:
        try:
            query = "INSERT INTO university (name, description, professor, university_id) VALUES (%s)"
            values = (university.name)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error inserting university :", e)
            self.db.rollback()
            return False

        return True

    def delete(self, university: University) -> bool:
        try:
            query = "DELETE FROM university WHERE id = %s"
            values = (university.id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error deleting university:", e)
            self.db.rollback()
            return False

        return True

    def update(self, university: University) -> bool:
        try:
            query = "UPDATE university SET name = %s WHERE id = %s"
            values = (university.name, university.id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error updating university:", e)
            self.db.rollback()
            return False

        return True

    def select_by_id(self, university_id: int) -> University:
        try:
            query = "SELECT * FROM university WHERE id = %s"
            values = (university_id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            university_data = cursor.fetchone()

            if university_data:
                university = University(*university_data)
                return university
            else:
                return None
        except Exception as e:
            print("Error selecting university by ID:", e)
            return None
