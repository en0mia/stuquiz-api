# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
from dataclasses import dataclass

from app.stuquiz.entities.entity import Entity


@dataclass
class Admin(Entity):
    """
    This class represents an Admin object.
    """
    id: str
    username: str
    email: str
    password: str
    salt: str

    def dump(self) -> dict:
        """The dump method returns only the public fields without the password and the salt
        to avoid to disclose them.
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
