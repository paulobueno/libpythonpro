from libpythonpro.spam.spam_sender import Sender


def test_create_spam_sender():
    sender = Sender()
    assert sender is not None

def test_sender():
    sender = Sender()
    result = sender.send(
        'paulob.bruno@gmail.com',
        'thaism.nishimoto@gmail.com',
        'Lista de compras',
        'Os itens a serem comprados'
    )
    assert 'paulob.bruno@gmail.com' in result
