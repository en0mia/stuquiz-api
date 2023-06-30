# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23

from dataclasses import dataclass
from datetime import datetime
from app.stuquiz.entities.entity import Entity


@dataclass
class Answer(Entity):
    """
    This class represents an Answer object.
    """
    id: str
    question_id: str
    answer: str
    creation_date: datetime
    correct: bool
    points: float
