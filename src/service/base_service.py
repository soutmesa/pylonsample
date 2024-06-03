from typing import TypeVar, Generic
from src.repository.base_repository import BaseRepository

ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType", bound=BaseRepository)

class BaseService(Generic[ModelType, RepositoryType]):
    def __init__(self, repository: RepositoryType):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def create(self, obj_in):
        return self.repository.create(obj_in)

    def update(self, db_obj, obj_in):
        return self.repository.update(db_obj, obj_in)

    def remove(self, id: int):
        return self.repository.remove(id)

