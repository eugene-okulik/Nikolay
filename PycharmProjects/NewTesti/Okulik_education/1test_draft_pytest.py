# Напиши тест для простой функции, которая принимает два числа и возвращает их сумму.
# Проверь, что результат корректный для нескольких примеров.

import pytest



def add(a, b):
    return a + b


@pytest.mark.parametrize('a, b, result', [(2, 2, 4), (3, 3, 6), (-3, 1, -2)])
def test_add(a, b, result):
    assert add(a, b) == result


# Создай тест для функции, которая проверяет, является ли строка палиндромом
# (читается одинаково слева направо и справа налево).
# Протестируй на нескольких строках.

def my_palindrom(word):
    return word == word[::-1]


@pytest.mark.parametrize('string, result', [('hello', False), ('abba', True)])
def test_my_palindrom(string, result):
    actual_result = my_palindrom(string)
    assert actual_result == result
