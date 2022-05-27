class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author


class Library:
    def __init__(self):
        self.books = []

    def add(self, title, author):
        self.books.append(Book(title, author))

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def by_author(self, author):
        matches = []
        for book in self.books:
            if book.author == author:
                matches.append(book)

        if len(matches) == 0:
            return None

        return matches
