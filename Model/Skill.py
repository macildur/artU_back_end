
class Skill:

    def __init__(self, title):
        super().__init__()
        self.title = title

    @staticmethod
    def validateImageTags(primaryCategory, subCategory, tags):

        if primaryCategory not in tags or subCategory not in tags:
            errorString = ''
            if primaryCategory not in tags:
                errorString.join(primaryCategory)
            elif subCategory not in tags:
                errorString.join('and ' + subCategory)

            raise Exception(f"{errorString} tag not found")
