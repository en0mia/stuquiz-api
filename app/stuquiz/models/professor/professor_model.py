# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from app.stuquiz.entities.professor import Professor
from app.stuquiz.repositories.professor_repository import ProfessorRepository


class ProfessorModel(object):
    def __init__(self, professor_repository: Optional[ProfessorRepository] = None):
        self.professor_repository = professor_repository or ProfessorRepository()

    def get_professors(self) -> list[Professor]:
        """A proxy for ProfessorRepository.select_professors()
        :return: A list of Professors.
        """
        return self.professor_repository.select_professors()
