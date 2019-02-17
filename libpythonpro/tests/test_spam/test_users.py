import pytest
from libpythonpro.spam.db import Connection
from libpythonpro.spam.models import User


@pytest.fixture
def connection():
    # Setup
    connection_obj = Connection()
    yield connection_obj
    # Tear Down
    connection_obj.close()


@pytest.fixture
def session(connection):
    session_obj = connection.create_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()


def test_save_user(session):
    user = User(name='Paulo')
    session.save(user)
    assert isinstance(user.id, int)


def test_users_list(session):
    users = [User(name='Paulo'), User(name='Rafael')]
    for user in users:
        session.save(user)
    assert users == session.list()
