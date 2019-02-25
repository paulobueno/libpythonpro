import pytest
from libpythonpro.spam.spam_sender import Mailer, InvalidEmail


def test_create_spam_sender():
    mailer = Mailer()
    assert mailer is not None


@pytest.mark.parametrize(
            'sender',
            ['paulob.bruno@gmail.com', 'paulo.siqueira@amaro.com']
            )
def test_sender(sender):
    mailer = Mailer()
    result = mailer.send(
        sender,
        'thaism.nishimoto@gmail.com',
        'Lista de compras',
        'Os itens a serem comprados'
    )
    assert sender in result


@pytest.mark.parametrize(
            'sender',
            [' ', 'paulo.siqueiraamaro.com']
            )
def test_invalidemail(sender):
    mailer = Mailer()
    with pytest.raises(InvalidEmail):
        mailer.send(
            sender,
            'thaism.nishimoto@gmail.com',
            'Lista de compras',
            'Os itens a serem comprados'
        )
