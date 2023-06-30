# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 30/05/23
from dataclasses import dataclass
from app.stuquiz.entities.entity import Entity


@dataclass
class Category(Entity):
    """
    This class represents a Category object.
    """
    id: str
    name: str
