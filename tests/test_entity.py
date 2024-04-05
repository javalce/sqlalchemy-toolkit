import pytest
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, clear_mappers, mapped_column

from sqlalchemy_toolkit import Entity


@pytest.fixture(autouse=True)
def before_each():
    yield
    Entity.metadata.clear()
    clear_mappers()


def test_entity():
    class DummyModel(Entity):
        __tablename__ = "dummy"
        id: Mapped[int] = mapped_column(Integer, primary_key=True)

    assert issubclass(DummyModel, DeclarativeBase)
