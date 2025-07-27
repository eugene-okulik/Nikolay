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
    def wrapper(first, second):
        if first < 0 or second < 0:
            return first * second
        elif first == second:
            return first + second
        elif first > second:
            return first - second
        elif second > first:
            return first / second
        else:
            print('что-то не так')

        func(first, second)

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
