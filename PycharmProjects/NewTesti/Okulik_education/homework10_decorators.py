# задание 1
def finish_me(func):
    def wrapper(text):
        func(text)
        print('finished')

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')


# задание 2
def repeat_me(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)

# задание 3

number1 = int(input('enter the first number: '))
number2 = int(input('enter second number: '))


def calculator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            print('что-то не так')

        return func(first, second, operation)

    return wrapper


@calculator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        print('что-то пошло не так')


print(calc(number1, number2))

# задание 4

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {
    price.split()[0]: int(price.split()[1][:-1])
    for price in PRICE_LIST.splitlines()
}

print(price_dict)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


# price_dict = {}  # пустой словарь
#
# for line in PRICE_LIST.splitlines():
#     parts = line.split()
#     name = parts[0]                 # название товара
#     price = int(parts[1][:-1])     # цена без последнего символа 'р', преобразованная в int
#     price_dict[name] = price       # добавляем в словарь
#
# print(price_dict)

price_dict = {}
for element in PRICE_LIST.splitlines():
    # print(element)
    parts = element.split()
    # print(parts)
    name = parts[0]
    # print(name)
    price = int(parts[1][:-1])
    # print(price)
    price_dict[name] = price
print(price_dict)