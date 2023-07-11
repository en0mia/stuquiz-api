# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import uuid
from typing import Optional

from app.stuquiz.entities.university import University
from app.stuquiz.repositories.university_repository import UniversityRepository


class UniversityModel(object):
    def __init__(self, university_repository: Optional[UniversityRepository] = None):
        self.university_repository = university_repository or UniversityRepository()

    def get_universities(self) -> list[University]:
        return self.university_repository.select_universities()

    def get_university_by_id(self, university_id: str) -> Optional[University]:
        return self.university_repository.select_university_by_id(university_id)

    def add_university(self, university_name: str) -> bool:
        university = University(str(uuid.uuid4()), university_name)

        return self.university_repository.create_university(university)
