from app.stuquiz.repositories.abstract_repository import Repository
from app.stuquiz.entities.question import Question


class QuestionRepository(Repository):

    def insert(self, question: Question) -> bool:
        try:
            query = "INSERT INTO question (question, rating, course_id) VALUES (%s)"
            values = (question.question, question.rating, question.course_id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error inserting question :", e)
            self.db.rollback()
            return False

        return True

    def delete(self, question: Question) -> bool:
        try:
            query = "DELETE FROM question WHERE id = %s"
            values = (question.id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error deleting question:", e)
            self.db.rollback()
            return False

        return True

    def update(self, question: Question) -> bool:
        try:
            query = "UPDATE question SET question = %s WHERE id = %s"
            values = (question.question, question.id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error updating question:", e)
            self.db.rollback()
            return False

        return True

    def select_by_id(self, question_id: int) -> Question:
        try:
            query = "SELECT * FROM question WHERE id = %s"
            values = (question_id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            question_data = cursor.fetchone()

            if question_data:
                question = Question(*question_data)
                return question
            else:
                return None
        except Exception as e:
            print("Error selecting question by ID:", e)
            return None
