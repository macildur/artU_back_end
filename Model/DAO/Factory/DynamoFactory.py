from Model.DAO.Factory.Factory import AbstractFactory
from Model.DAO.UserDAO import UserDAO


class DynamoFactory(AbstractFactory):

    def initUserDAO(self):
        return UserDAO()

    def initSkillDAO(self):
        pass

    def initModuleDAO(self):
        pass

    def initLessonDAO(self):
        pass
