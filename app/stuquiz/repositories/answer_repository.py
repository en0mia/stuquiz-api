from app.stuquiz.repositories.abstract_repository import Repository
from app.stuquiz.entities.answer import Answer


class AnswerRepository(Repository):

    def insert(self, answer: Answer) -> bool:
        try:
            query = "INSERT INTO answer (answer, correct, points, question_id) VALUES (%s, %s, %s, %s)"
            values = (answer.answer, answer.correct, answer.points, answer.question_id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error inserting answer :", e)
            self.db.rollback()
            return False

        return True

    def delete(self, answer: Answer) -> bool:
        try:
            query = "DELETE FROM answer WHERE id = %s"
            values = (answer.id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error deleting answer:", e)
            self.db.rollback()
            return False

        return True

    def update(self, answer: Answer) -> bool:
        try:
            query = "UPDATE answer SET answer = %s WHERE id = %s"
            values = (answer.answer, answer.id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error updating answer:", e)
            self.db.rollback()
            return False

        return True

    def select_by_id(self, answer_id: int) -> Answer:
        try:
            query = "SELECT * FROM answer WHERE id = %s"
            values = (answer_id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            answer_data = cursor.fetchone()

            if answer_data:
                answer = Answer(*answer_data)
                return answer
            else:
                return None
        except Exception as e:
            print("Error selecting answer by ID:", e)
            return None
