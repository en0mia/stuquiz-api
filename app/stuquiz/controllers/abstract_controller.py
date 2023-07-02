# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 02/07/23
from abc import ABC, abstractmethod
from flask import Response


class AbstractController(ABC):
    """Abstract class to represent the Controllers."""
    @abstractmethod
    def execute(self, data: dict) -> Response:
        """
        Abstract method called by the routes when starting the stack.
        :param data: a dict containing the data for the controller, or an empty dict if no data
            is requested.
        :return: HTTP Response.
        """
        pass
