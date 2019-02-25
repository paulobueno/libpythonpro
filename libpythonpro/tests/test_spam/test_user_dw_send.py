from unittest.mock import Mock
import pytest
from libpythonpro.spam.main import SpamSender
from libpythonpro.spam.models import User
from libpythonpro.spam.spam_sender import Mailer


class MailerMock(Mailer):

    def __init__(self):
        super().__init__()
        self.sending_parameters = None
        self.qty_sent_emails = 0

    def send(self, sender, receiver, subject, content):
        self.sending_parameters = (sender, receiver, subject, content)
        self.qty_sent_emails += 1


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
    mailer = Mock()
    spam_sender = SpamSender(session, mailer)
    spam_sender.send_email(
        'paulob.bruno@gmail.com',
        'Python pro Course',
        'Take a look into the lessons'
    )
    assert len(users) == mailer.send.call_count


def test_spam_parameters(session):
    user = User(name='Rafael', email='rafaelbuenobruno@gmail.com')
    session.save(user)
    mailer = Mock()
    spam_sender = SpamSender(session, mailer)
    spam_sender.send_email(
        'paulob.bruno@gmail.com',
        'Python pro Course',
        'Take a look into the lessons'
    )
    # noinspection PyStatementEffect
    mailer.send.assert_called_once_with == (
        'paulob.bruno@gmail.com',
        'rafaelbuenobruno@gmail.com',
        'Python pro Course',
        'Take a look into the lessons'
    )
