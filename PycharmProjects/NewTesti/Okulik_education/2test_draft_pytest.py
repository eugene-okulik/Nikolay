# Создайте функцию is_even(n), которая возвращает True если число четное, и False если нечетное. Напишите тесты для:
#
# Положительных четных чисел
#
# Положительных нечетных чисел
#
# Отрицательных чисел
#
# Нуля

import pytest


def is_even(n):
    return n % 2 == 0


@pytest.mark.parametrize('number, result', [(2, True), (3, False), (-3, False), (0, True)])
def test_even_numbers(number, result):
    assert is_even(number) == result


# Создайте функцию divide(a, b), которая возвращает результат деления. Напишите тесты:
#
# Проверка корректного деления
#
# Проверка что при делении на 0 вызывается ZeroDivisionError

def divide(a, b):
    return a / b


@pytest.mark.parametrize('a, b, result', [(2, 2, 1), (3, 2, 1.5), (6, 2, 3), (4, -1, -4)])
def test_division(a, b, result):
    assert divide(a, b) == result


@pytest.mark.parametrize('a', [1])
def test_division_zero(a):
    with pytest.raises(ZeroDivisionError):
        divide(a, 0)


# Создайте фикстуру, которая:
#
# Перед тестом создает временный список [1, 2, 3, 4, 5]
#
# После теста очищает список
#
# Напишите тесты для проверки операций с этим списком

@pytest.fixture()
def add_list():
    print("Создаем временный список [1, 2, 3, 4, 5]")
    my_list = [1, 2, 3, 4, 5]
    yield my_list
    print("Очищаем список")
    my_list.clear()


def test_list(add_list):
    "Тест проверяет длину списка"
    print(f'Список в тесте: {add_list}')
    assert len(add_list) == 5
    assert add_list == [1, 2, 3, 4, 5]


def test_operation(add_list):
    """Тест различных операций со списком"""
    # Добавляем элемент
    add_list.append(6)
    assert add_list == [1, 2, 3, 4, 5, 6]
    # Удаляем элемент
    add_list.remove(3)
    assert add_list == [1, 2, 4, 5, 6]
    # Проверяем сумму
    assert sum(add_list) == 18


def test_list_after_modification(add_list):
    """Тест показывает, что список восстанавливается для каждого теста"""
    # Модифицируем список
    add_list.extend([10, 20])
    assert len(add_list) == 7
