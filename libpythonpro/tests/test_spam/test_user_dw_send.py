import pytest
from libpythonpro.spam.main import SpamSender
from libpythonpro.spam.models import User
from libpythonpro.spam.spam_sender import Sender


@pytest.mark.parametrize(
    'users', [
        [
            User(name='Paulo', email='paulob.bruno@gmail.com'),
            User(name='Rafael', email='rafaelbuenobruno@gmail.com')
        ],
        [
            User(name='Paulo', email='paulob.bruno@gmail.com'),
        ]
    ]
)
def test_qty_spam_sender(session, users):
    for user in users:
        session.save(user)
    sender = Sender()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_email(
        'paulob.bruno@gmail.com',
        'Python pro Course',
        'Take a look into the lessons'
    )
    assert len(users) == sender.qty_sent_emails
