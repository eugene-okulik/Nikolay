result1 = 'результат операции: 42'
result2 = 'результат операции: 54'
result3 = 'результат работы программы: 209'
result4 = 'результат: 2'


def add(result):
    new_result = result.split()
    print(int(new_result[-1]) + 10)


add(result1)
add(result2)
add(result3)
add(result4)
