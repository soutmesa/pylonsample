from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional
# from sqlalchemy import Table, select, update, delete
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_id(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj_in):
        db_obj = self.model(**obj_in.dict())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj, obj_in):
        obj_data = obj_in.dict(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def remove(self, id: int):
        obj = self.get_by_id(id)
        self.db.delete(obj)
        self.db.commit()
        return obj

    # def get_all(self) -> List[T]:
    #     query = select(self.table)
    #     result = self.db.execute(query)
    #     return [row._mapping for row in result]

    # def get_by_id(self, id: int) -> Optional[T]:
    #     query = select(self.table).where(self.table.id == id)
    #     result = self.db.execute(query).scalar_one_or_none()
    #     return dict(result._mapping) if result else None

    # def create(self, obj_in: T) -> T:
    #     self.db.add(obj_in)
    #     self.db.commit()
    #     self.db.refresh(obj_in)
    #     return obj_in

    # def update(self, id: int, obj_in: dict) -> Optional[T]:
    #     query = update(self.table).where(self.table.id == id).values(**obj_in).execution_options(synchronize_session="fetch")
    #     result = self.db.execute(query)
    #     if result.rowcount == 0:
    #         return None
    #     self.db.commit()
    #     return self.get_by_id(id)

    # def delete(self, id: int) -> bool:
    #     query = delete(self.table).where(self.table.id == id)
    #     result = self.db.execute(query)
    #     self.db.commit()
    #     return result.rowcount > 0
