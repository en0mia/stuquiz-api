# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 26/07/23
from typing import Optional

from easy_route.middlewares.data_validator_middleware import DataProvider
from flask import Request


class ArgsDataProvider(DataProvider):
    """This Data provider extracts the data from request.args"""
    def get_data(self, request: Request) -> Optional[dict]:
        return request.args
