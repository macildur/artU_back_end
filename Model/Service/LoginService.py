from DynamoFactory import DynamoFactory
#import bcrypt

class LoginService:
    factory = DynamoFactory()

    def login(self, username, password):
        salt = username[1] + username[0] + username[2]
        safePassword = self.encryptPassword(password, salt)
        response = self.factory.initUserDAO().getUser(username, safePassword)
        return response

    def encryptPassword(self, password, salt):
        safePassword = "encrypted"  #bcrypt.hashpw(password, salt)
        return safePassword

    def insertUser(self, newUser):
        safePassword = self.encryptPassword(newUser.password)
        newUser.password = safePassword
        response = self.factory.initUserDAO().addUser(newUser)
        return response
