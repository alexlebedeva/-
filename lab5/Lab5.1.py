class book(object):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def bookinfo(self):
        return f'{self.title} {self.author} {self.year}'

book1 = book("1984", "Оруэлл", 1949)
book2 = book("Мастер и Маргарита", "Булгаков", 1966)

print(book1.bookinfo())