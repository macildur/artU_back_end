
class Skill:

    def __init__(self, title):
        super().__init__()
        self.title = title

    @staticmethod
    def validateImageTags(primaryCategory, secondaryCategory, tags):

        if primaryCategory not in tags or secondaryCategory not in tags:
            errorString = ''
            if primaryCategory not in tags:
                errorString.join(primaryCategory)
            elif secondaryCategory not in tags:
                errorString.join('and ' + secondaryCategory)

            raise NameError(f"{errorString} tag not found")
