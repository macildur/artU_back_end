from artU_back_end.Model.DOA.Factory.Factory import AbstractFactory


class DynamoFactory(AbstractFactory):

    def initUserDAO(self):
        return UserDAO()

    def initSkillDAO(self):
        pass

    def initModuleDAO(self):
        pass

    def initLessonDAO(self):
        pass