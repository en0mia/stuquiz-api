from abc import ABC, abstractmethod
from app.stuquiz.entities.entity import Entity
from app.stuquiz.db import get_db


class Repository(ABC):
    def __init__(self):
        self.db = get_db()

    @abstractmethod
    def insert(self, entity: Entity) -> bool:
        pass

    @abstractmethod
    def delete(self, entity: Entity) -> bool:
        pass

    @abstractmethod
    def update(self, entity: Entity) -> bool:
        pass

    @abstractmethod
    def select_by_id(self, id: int) -> Entity:
        pass
