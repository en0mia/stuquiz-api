# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23

from dataclasses import dataclass
from app.stuquiz.entities.entity import Entity


@dataclass
class University(Entity):
    """
    This class represents a University object.
    """
    id: int
    uuid: str
    name: str
