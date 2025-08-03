class Book:
    page_material = 'материал: бумага'
    text = True


class Pushkin(Book):
    book_title = 'Название: Лукоморье'
    author = 'Автор: Пушкин'
    number_of_pages = 'страниц: 50'
    ISBN = 101


class Dostoevsky(Book):
    book_title = 'Название: Идиот'
    author = 'Автор: Достоевский'
    number_of_pages = 'страниц: 500'
    ISBN = 101

    def __init__(self, reserved):
        self.reserved = reserved


class Griboyedov(Book):
    book_title = 'Название: Горе от ума'
    author = 'Автор: Грибоедов'
    number_of_pages = 'страниц: 400'
    ISBN = 101


pushkin = Pushkin()
dostoevsky = Dostoevsky('зарезервирована')
griboyedov = Griboyedov()

print(pushkin.book_title)
print(pushkin.author)
print(pushkin.number_of_pages)
print(pushkin.page_material)
print()
print(dostoevsky.book_title)
print(dostoevsky.author)
print(dostoevsky.number_of_pages)
print(dostoevsky.page_material)
print(dostoevsky.reserved)
print()
print(griboyedov.book_title)
print(griboyedov.author)
print(griboyedov.number_of_pages)
print(griboyedov.page_material)
print()


class SchoolTextbooks(Book):
    exercise = True


class Mathematics(SchoolTextbooks):
    name = 'Название: математика'
    lesson = 'Предмет: алгебра'
    group = 'класс: 6'
    author = 'Автор: Зыкин'
    number_of_pages = 'страниц: 50'

    def __init__(self, reserved):
        self.reserved = reserved


class Story(SchoolTextbooks):
    name = 'Название: история'
    lesson = 'Предмет: история мира'
    group = 'класс: 6'
    author = 'автор: Иванов'
    number_of_pages = 'страниц: 507'


class Geography(SchoolTextbooks):
    name = 'Название: география'
    lesson = 'Предмет: география мира'
    group = 'класс: 8'
    author = 'автор: Петров'
    number_of_pages = 'страниц: 550'


mathematics = Mathematics('зарезервирована')
story = Story()
geography = Geography()

print(mathematics.name)
print(mathematics.author)
print(mathematics.number_of_pages)
print(mathematics.lesson)
print(mathematics.group)
print(mathematics.reserved)
print()
print(story.name)
print(story.author)
print(story.number_of_pages)
print(story.lesson)
print(story.group)
print()
print(geography.name)
print(geography.author)
print(geography.number_of_pages)
print(geography.lesson)
print(geography.group)
