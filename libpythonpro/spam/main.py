class SpamSender:

    def __init__(self, session, mailer):
        self.mailer = mailer
        self.session = session

    def send_email(self, sender, subject, content):
        for user in self.session.list():
            self.mailer.send(
                sender,
                user.email,
                subject,
                content
            )
