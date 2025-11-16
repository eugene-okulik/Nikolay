class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, book_title, author, number_of_pages, isbn):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = False

    def display_info(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f'Название книги: {self.book_title}, автор: {self.author}, '
                f'количество страниц: {self.number_of_pages}, материал: {self.page_material}, '
                f'{reserved_status}.')


class SchoolTextbooks(Book):
    exercise = True

    def __init__(self, book_title, author, number_of_pages, isbn, lesson, group):
        super().__init__(book_title, author, number_of_pages, isbn)
        self.lesson = lesson
        self.group = group

    def display_info(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f'Название: {self.book_title}, автор: {self.author}, '
                f'количество страниц: {self.number_of_pages}, предмет: {self.lesson}, '
                f'класс: {self.group}, {reserved_status}.')


book1 = Book('Идиот', 'Достоевский', 200, 101)
book1.reserved = True
book2 = Book('Лукоморье', 'Пушкин', 150, 102)
book3 = Book('Мцыри', 'Лермонтов', 180, 103)
book4 = Book('Дубровский', 'Пушкин', 55, 104)
book5 = Book('Война и мир', 'Толстой', 500, 105)


print(book2.display_info())
print(book1.display_info())
print(book3.display_info())
print(book4.display_info())
print(book5.display_info())

textbooks1 = SchoolTextbooks('Алгебра', 'Иванов', 200, 800,
                             'Математика', '6a')
textbooks1.reserved = True
textbooks2 = SchoolTextbooks('История', 'Петров', 250, 801,
                             'История Мира', '8б')
textbooks3 = SchoolTextbooks('География', 'Смирнов', 150, 805,
                             'География  Мира', '9б')
print(textbooks2.display_info())
print(textbooks1.display_info())
print(textbooks3.display_info())
