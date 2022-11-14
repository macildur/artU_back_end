from Model.DOA.Factory import Factory

class SkillService:
    factory = Factory.AbstactFactory()

    def getMatchingImages(self, category, subCategories):
        return self.factory.initSkillDAO().getMatchingImages((category, subCategories))
