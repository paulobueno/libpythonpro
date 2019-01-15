import pytest
from libpythonpro.spam.spam_sender import Sender


def test_create_spam_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
            'sender',
            ['paulob.bruno@gmail.com','paulo.siqueira@amaro.com']
            )
def test_sender(sender):
    email_sender = Sender()
    result = email_sender.send(
        sender,
        'thaism.nishimoto@gmail.com',
        'Lista de compras',
        'Os itens a serem comprados'
    )
    assert sender in result
