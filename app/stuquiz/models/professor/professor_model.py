# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import uuid
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

    def get_professor_by_id(self, professor_id: str) -> Optional[Professor]:
        """A proxy for ProfessorRepository.select_professor_by_id()
        :return: Professor | None.
        """
        return self.professor_repository.select_professor_by_id(professor_id)

    def add_professor(self, professor_name: str) -> bool:
        """A proxy for ProfessorRepository.create_professor()
        :return: bool.
        """
        professor = Professor(str(uuid.uuid4()), professor_name)
        return self.professor_repository.create_professor(professor)

    def update_professor(self, professor: Professor) -> bool:
        """A proxy for ProfessorRepository.update_professor()
        :return: bool.
        """
        return self.professor_repository.update_professor(professor)

    def delete_professor(self, professor: Professor) -> bool:
        """A proxy for ProfessorRepository.delete_professor()
        :return: bool.
        """
        return self.professor_repository.delete_professor(professor)
