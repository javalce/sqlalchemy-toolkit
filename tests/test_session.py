import pytest
from sqlalchemy.orm import Session

from sqlalchemy_repository.session import _session, get_session


def test_get_session():
    # Test when session is available
    session = Session()
    _session.set(session)
    assert get_session() == session

    # Test when session is not available
    _session.set(None)
    with pytest.raises(RuntimeError):
        get_session()


def test_set_session():
    session = Session()
    token = _session.set(session)
    assert _session.get() == session
    _session.reset(token)
    assert _session.get() is None
