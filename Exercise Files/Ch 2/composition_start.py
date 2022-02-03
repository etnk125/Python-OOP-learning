# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


from functools import reduce


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        return reduce(lambda x, y: x + y, [i.pagecount for i in self.chapters])


class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} { self.lastname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


auth = Author('Leo', 'tolstoy')
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())
