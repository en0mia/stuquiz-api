# @author Lorenzo Varese
# @created 2023-07-05

import uuid
from typing import Optional

from app.stuquiz.entities.category import Category
from app.stuquiz.repositories.category_repository import CategoryRepository


class CategoryModel(object):
    def __init__(self, category_repository: Optional[CategoryRepository] = None):
        self.category_repository = category_repository or CategoryRepository()

    def get_categories(self) -> list[Category]:
        """A proxy for CategoryRepository.select_category()
        :return: A list of Categories.
        """
        return self.category_repository.select_categories()

    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        """A proxy for CategoryRepository.select_category_by_id()
        :return: Category | None
        """
        return self.category_repository.select_category_by_id(category_id)

    def add_category(self, category_name: str) -> bool:
        """A proxy for CategoryRepository.create_category()
        :return: bool
        """
        category = Category(str(uuid.uuid4()), category_name)

        return self.category_repository.create_category(category)

    def update_category(self, category: Category) -> bool:
        """A proxy for CategoryRepository.update_category()
        :return: bool
        """
        return self.category_repository.update_category(category)

    def delete_category(self, category: Category) -> bool:
        """A proxy for CategoryRepository.delete_category()
        :return: bool
        """
        return self.category_repository.delete_category(category)
