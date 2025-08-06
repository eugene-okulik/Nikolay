class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, reserved):
        self.reserved = reserved


class Pushkin(Book):
    book_title = 'Лукоморье'
    author = 'Пушкин'
    number_of_pages = 50
    ISBN = 101


class Dostoevsky(Book):
    book_title = 'Идиот'
    author = 'Достоевский'
    number_of_pages = 500
    ISBN = 102


class Griboyedov(Book):
    book_title = 'Горе от ума'
    author = 'Грибоедов'
    number_of_pages = 400
    ISBN = 103


pushkin = Pushkin('не зарезервирована')
dostoevsky = Dostoevsky('зарезервирована')
griboyedov = Griboyedov('не зарезервирована')

print('Название:', pushkin.book_title)
print('Автор: ', pushkin.author)
print('страниц: ', pushkin.number_of_pages)
print('материал: ', pushkin.page_material)
print()
print('Название: ', dostoevsky.book_title)
print('Автор: ', dostoevsky.author)
print('страниц: ', dostoevsky.number_of_pages)
print('материал: ', dostoevsky.page_material)
print(dostoevsky.reserved)
print()
print('Название: ', griboyedov.book_title)
print('Автор: ', griboyedov.author)
print('страниц: ', griboyedov.number_of_pages)
print('материал: ', griboyedov.page_material)
print()


class SchoolTextbooks(Book):
    exercise = True


class Mathematics(SchoolTextbooks):
    book_title = 'математика'
    lesson = 'алгебра'
    group = '6б'
    author = 'Зыкин'
    number_of_pages = 50


class Story(SchoolTextbooks):
    book_title = 'история'
    lesson = 'история мира'
    group = '8a'
    author = 'Иванов'
    number_of_pages = 507


class Geography(SchoolTextbooks):
    book_title = 'география'
    lesson = 'география мира'
    group = '8б'
    author = 'Петров'
    number_of_pages = 550


mathematics = Mathematics('зарезервирована')

story = Story('не зарезервирована')
geography = Geography('не зарезервирована')

print('Название: ', mathematics.book_title)
print('Автор: ', mathematics.author)
print('страниц: ', mathematics.number_of_pages)
print('Предмет: ', mathematics.lesson)
print('класс: ', mathematics.group)
print(mathematics.reserved)
print()
print('Название: ', story.book_title)
print('Автор: ', story.author)
print('страниц: ', story.number_of_pages)
print('Предмет: ', story.lesson)
print('класс: ', story.group)
print()
print('Название: ', geography.book_title)
print('Автор: ', geography.author)
print('страниц: ', geography.number_of_pages)
print('Предмет: ', geography.lesson)
print('класс: ', geography.group)
