class Sender:
    def __init__(self):
        self.qty_sent_emails = 0

    def send(self, sender, receiver, subject, content):
        if '@' not in sender:
            raise InvalidEmail(f'Invalid sender {sender}')
        self.qty_sent_emails += 1
        return sender


class InvalidEmail(Exception):
    pass
