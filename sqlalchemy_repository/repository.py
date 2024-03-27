from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from .entity import Entity
from .session import get_session

T = TypeVar("T", bound=Entity)
K = TypeVar("K")


class SQLAlchemyRepository(Generic[T, K]):
    entity_class: Type[T]

    @property
    def session(self) -> Session:
        return get_session()

    def find_all(self) -> List[T]:
        stm = select(self.entity_class)
        result = self.session.scalars(stm).all()
        return list(result)

    def find_by_id(self, id: K) -> Optional[T]:
        return self.session.get(self.entity_class, id)

    def save(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, entity: T) -> T:
        self.session.delete(entity)
        self.session.commit()
        return entity

    def delete_by_id(self, id: K) -> None:
        entity = self.find_by_id(id)
        if entity:
            self.delete(entity)
