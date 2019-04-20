class AuthorList:
    def __init__(self):
        self.author_list = []

    def get_author_list(self):
        return self.author_list

    def set_author_list(self, author):
        self.author_list.append(author)
