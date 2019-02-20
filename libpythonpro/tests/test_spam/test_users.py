from libpythonpro.spam.models import User


def test_save_user(session):
    user = User(name='Paulo', email='paulob.bruno@gmail.com')
    session.save(user)
    assert isinstance(user.id, int)


def test_users_list(session):
    users = [User(name='Paulo', email='paulob.bruno@gmail.com'), User(name='Rafael', email='paulob.bruno@gmail.com')]
    for user in users:
        session.save(user)
    assert users == session.list()
