class Book:
    def __init__(self, id, title=None, author=None):
        self._id = id
        self._title = title
        self._author = author

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
