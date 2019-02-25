class Sender:

    def send(self, sender, receiver, subject, content):
        if '@' not in sender:
            raise InvalidEmail(f'Invalid sender {sender}')
        return sender


class InvalidEmail(Exception):
    pass
