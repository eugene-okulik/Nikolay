# задание 1
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
import datetime

my_date = "Jan 15, 2023 - 12:05:33"
new_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
print(new_date)
human_date = new_date.strftime('%B')
print(human_date)
human_date2 = new_date.strftime('%d.%m.%Y, %H:%M')
print(human_date2)

# задание 2
# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31,
#                 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]


def hot(day):
    if day > 28:
        return True
    else:
        return False


hot_days = filter(hot, temperatures)
print(list(hot_days))
very_hot_days = [32, 34, 30, 32, 34, 30, 29, 29, 29, 31, 33, 31, 30, 32, 30]
print(max(very_hot_days))
print(min(very_hot_days))
print(sum(very_hot_days) // 2)
