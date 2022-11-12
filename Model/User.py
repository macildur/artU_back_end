import uuid

class User:

    def __init__(self, username, firstname, lastname, password):
        self.id = uuid.uuid4()
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.profilePictureUrl = 'default'
        self.currentModule = 0
        self.currentStreak = 0

    def __init__(self, username, firstname, lastname, password, profilePictureUrl):
        self.id = uuid.uuid4()
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.profilePictureUrl = profilePictureUrl
        self.currentModule = 0
        self.currentStreak = 0