class SpamSender:

    def __init__(self, session, sender):
        self.sender = sender
        self.session = session

    def send_email(self, sender, subject, content):
        for user in self.session.list():
            self.sender.send(
                sender,
                user.email,
                subject,
                content
            )
