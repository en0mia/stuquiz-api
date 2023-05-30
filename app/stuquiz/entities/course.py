# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23
from dataclasses import dataclass

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.entity import Entity


@dataclass
class Course(Entity):
    """
    This class represents a Course object.
    """
    id: int
    uuid: str
    university_id: str
    name: str
    description: str
    professor: str
    categories: list[Category]
