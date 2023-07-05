# @author Lorenzo Varese
# @created 2023-07-05

from typing import Optional

from app.stuquiz.entities.category import Category
from app.stuquiz.repositories.category_repository import CategoryRepository


class CategoryModel(object):
    def __init__(self, category_repository: Optional[CategoryRepository] = None):
        self.category_repository = category_repository or CategoryRepository()

    def get_categories(self) -> list[Category]:
        return self.category_repository.select_categories()

    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        return self.category_repository.select_category_by_id(category_id)
