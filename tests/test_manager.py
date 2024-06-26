import pytest
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from sqlalchemy_toolkit import DatabaseManager


def test_session_ctx():
    db = DatabaseManager("sqlite:///:memory:")
    with db.session_ctx() as session:
        assert isinstance(session, Session)


def test_session_ctx_rollback():
    db = DatabaseManager("sqlite:///:memory:")

    with pytest.raises(OperationalError):
        with db.session_ctx() as session:
            session.execute(text("SELECT * FROM non_existent_table"))
