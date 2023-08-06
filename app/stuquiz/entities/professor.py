# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from dataclasses import dataclass

from app.stuquiz.entities.entity import Entity


@dataclass
class Professor(Entity):
    """
    This class represents a Professor object.
    """
    id: str
    name: str

    def dump(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }
