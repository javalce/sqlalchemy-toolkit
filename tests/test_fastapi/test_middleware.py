import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from sqlalchemy_repository import DatabaseManager
from sqlalchemy_repository.ext.fastapi import SQLAlchemyMiddleware


@pytest.fixture
def db():
    return DatabaseManager("sqlite:///:memory:")


@pytest.fixture
def app():
    return FastAPI()


@pytest.fixture
def client(app):
    return TestClient(app)


def test_sqlalchemy_middleware(db, app, client):
    @app.get("/")
    def root():
        return {"message": "Hello World"}

    app.add_middleware(SQLAlchemyMiddleware, db=db)

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
