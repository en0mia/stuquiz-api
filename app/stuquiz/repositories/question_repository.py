# @author Lorenzo Varese
# @created 2023-06-30

from app.stuquiz.entities.question import Question
from app.stuquiz.repositories.abstract_repository import AbstractRepository


class QuestionRepository(AbstractRepository):

    def create_question(self, question: Question) -> bool:
        query = "INSERT INTO question (question, rating, course_id) VALUES (%s, %s, %s)"
        return self.insert(query, (question.question, question.rating, question.course_id))

    def delete_question(self, question: Question) -> bool:
        query = "DELETE FROM question WHERE id = %s"
        return self.delete(query, (question.id, ))

    def update_question_text(self, question: Question) -> bool:
        query = "UPDATE question SET question = %s WHERE id = %s"
        return self.update(query, (question.question, question.id))

    def select_question_by_id(self, question_id: str) -> Question:
        query = "SELECT id, course_id, question, creation_date, rating FROM question WHERE id = %s"
        result = self.select(query, (question_id, ))
        return Question(*result[0]) if result and len(result) > 0 else None
