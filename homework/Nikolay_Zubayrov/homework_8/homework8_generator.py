# задание 1
import random

salary = int(input('Введите число: '))
bonus = random.choice([True, False])
if bonus:
    bonus_new = random.randrange(100, 151)
    total = salary + bonus_new
else:
    total = salary + 0
print(f'{salary},  {bonus} - ${total}')

# задание 2
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fib_generator()


def get_nth(gen, n):
    for _ in range(n - 1):
        next(gen)
    return next(gen)


print("5-е число:", get_nth(fib_generator(), 5))
print("200-е число:", get_nth(fib_generator(), 200))
print("1000-е число:", get_nth(fib_generator(), 1000))
print("100000-е число:", get_nth(fib_generator(), 100000))
