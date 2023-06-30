# @author Lorenzo Varese
# @created 2023-06-30

from app.stuquiz.repositories.abstract_repository import AbstractRepository
from app.stuquiz.entities.answer import Answer


class AnswerRepository(AbstractRepository):

    def create_answer(self, answer: Answer) -> bool:
        query = 'INSERT INTO answer(id, question_id, answer, creation_date, correct, points) ' \
                            'VALUES (%s, %s, %s, %s, %s, %s);'
        return self.insert(query, (answer.id, answer.question_id, answer.answer, answer.creation_date, answer.correct,
                                   answer.points))

    def delete_answer(self, answer: Answer) -> bool:
        query = "DELETE FROM answer WHERE id = %s"
        return self.delete(query, answer.id)

    def update_answer_text(self, answer: Answer) -> bool:
        query = "UPDATE answer SET answer = %s WHERE id = %s"
        return self.update(query, answer.answer, answer.id)

    def select_answer_by_id(self, answer_id: int) -> Answer:
        query = "SELECT * FROM answer WHERE id = %s"
        return self.select(query, answer_id)
