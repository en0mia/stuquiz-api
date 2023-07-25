# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23
from dataclasses import dataclass, field
from typing import Optional

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.entity import Entity


@dataclass
class Course(Entity):
    """
    This class represents a Course object.
    """
    id: str
    university_id: str
    name: str
    description: str
    professor_id: str
    code: str
    categories: Optional[list[Category]] = field(default_factory=list)

    def dump(self) -> dict:
        return {
            'id': self.id,
            'university_id': self.university_id,
            'name': self.name,
            'description': self.description,
            'professor_id': self.professor_id,
            'categories': [category.dump() for category in self.categories],
            'code': self.code
        }
