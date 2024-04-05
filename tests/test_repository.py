import pytest
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, clear_mappers, mapped_column

from sqlalchemy_toolkit import DatabaseManager, Entity, SQLAlchemyRepository


@pytest.fixture
def db():
    return DatabaseManager("sqlite:///:memory:")


@pytest.fixture
def DummyEntity():
    class DummyEntity(Entity):
        __tablename__ = "dummy"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)

    return DummyEntity


@pytest.fixture
def repository(DummyEntity):
    class DummyRepository(SQLAlchemyRepository[DummyEntity, int]):  # type: ignore
        entity_class = DummyEntity

    return DummyRepository()


@pytest.fixture(autouse=True)
def before_each(db, DummyEntity):
    with db.session_ctx():
        Entity.metadata.create_all(db.engine)
    yield
    with db.session_ctx():
        Entity.metadata.create_all(db.engine)
    Entity.metadata.clear()
    clear_mappers()


def test_find_all(db, DummyEntity, repository):
    with db.session_ctx() as session:
        session.add(DummyEntity())
        session.add(DummyEntity())
        session.add(DummyEntity())
        session.commit()

    with db.session_ctx():
        result = repository.find_all()

    assert len(result) == 3


def test_find_by_id(db, DummyEntity, repository):
    with db.session_ctx() as session:
        session.add(DummyEntity(id=1))
        session.commit()

    with db.session_ctx():
        result = repository.find_by_id(1)

    assert result.id == 1


def test_find_by_id_not_found(db, repository):
    with db.session_ctx():
        result = repository.find_by_id(1)

    assert result is None


def test_save(db, DummyEntity, repository):
    dummy_entity = DummyEntity()

    with db.session_ctx():
        result = repository.save(dummy_entity)

    assert result == dummy_entity
    assert result.id == 1


def test_delete(db, DummyEntity, repository):
    dummy_entity = DummyEntity()

    with db.session_ctx() as session:
        session.add(dummy_entity)
        session.commit()

    with db.session_ctx():
        result = repository.delete(dummy_entity)

    assert result == dummy_entity

    with db.session_ctx():
        result = repository.find_by_id(1)

    assert result is None


def test_delete_by_id(db, DummyEntity, repository):
    dummy_entity = DummyEntity()

    with db.session_ctx() as session:
        session.add(dummy_entity)
        session.commit()

    with db.session_ctx():
        result = repository.delete_by_id(1)

    with db.session_ctx():
        result = repository.find_by_id(1)

    assert result is None
