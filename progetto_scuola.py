class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def toString(self):
        return "Anno: " + self.year + ", Autore: " + self.author

book_instance = Book("La divina commedia", "1320", "Dante Alighieri")
print(book_instance.toString())
print(book_instance.get_title())
