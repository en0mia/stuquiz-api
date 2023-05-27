# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23

from dataclasses import dataclass
from datetime import datetime
from app.stuquiz.entities.entity import Entity


@dataclass
class Question(Entity):
    """
    This class represents a Question object.
    """
    id: int
    uuid: str
    course_id: str
    question: str
    creation_date: datetime
    rating: int
