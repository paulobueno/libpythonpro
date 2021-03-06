from time import sleep


class Session:
    count = 0
    users = []

    def save(self, user):
        Session.count += 1
        user.id = Session.count
        self.users.append(user)

    def roll_back(self):
        self.users.clear()

    def close(self):
        pass

    def list(self):
        return self.users


class Connection:
    def __init__(self):
        sleep(2)

    def create_session(self):
        return Session()

    def close(self):
        pass
