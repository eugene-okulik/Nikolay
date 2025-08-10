class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, book_title, author, number_of_pages, isbn):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn


class SchoolTextbooks(Book):
    exercise = True

    def __init__(self, book_title, author, number_of_pages, isbn, lesson, group):
        super().__init__(book_title, author, number_of_pages, isbn)
        self.lesson = lesson
        self.group = group


book1 = Book('Идиот', 'Достоевский', 200, 101)
book1.reserved = True
book2 = Book('Лукоморье', 'Пушкин', 150, 102)
book3 = Book('Мцыри', 'Лермонтов', 180, 103)
book4 = Book('Дубровский', 'Пушкин', 55, 104)
book5 = Book('Война и мир', 'Толстой', 500, 105)

print(f'Название книги: {book2.book_title}, автор: {book2.author}, количество страниц: {book3.number_of_pages},  '
      f'материал: {book4.page_material}')
print(f'Название книги: {book1.book_title}, автор: {book1.author}, количество страниц: {book1.number_of_pages},  '
      f'материал: {book1.page_material}, зарезервирована: {book1.reserved}')

textbooks1 = SchoolTextbooks('Алгебра', 'Иванов', 200, 800,
                             'Математика', '6a')
textbooks1.reserved = True
textbooks2 = SchoolTextbooks('История', 'Петров', 250, 801,
                             'История Мира', '8б')
textbooks3 = SchoolTextbooks('География', 'Смирнов', 150, 805,
                             'География  Мира', '9б')

print(
    f'Название: {textbooks1.book_title}, автор: {textbooks1.author}, количество страниц: {textbooks1.number_of_pages},'
    f'предмет: {textbooks1.lesson}, класс: {textbooks1.group}, зарезервирована: {textbooks1.reserved}')
print(
    f'Название: {textbooks2.book_title}, автор: {textbooks2.author}, количество страниц: {textbooks2.number_of_pages},'
    f'предмет: {textbooks2.lesson}, класс: {textbooks2.group}')
