# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
from typing import Optional

from app.stuquiz.entities.university import University
from app.stuquiz.repositories.university_repository import UniversityRepository


class UniversityModel(object):
    def __init__(self, university_repository: Optional[UniversityRepository] = None):
        self.university_repository = university_repository or UniversityRepository()

    def get_universities(self) -> list[University]:
        return self.university_repository.select_universities()


