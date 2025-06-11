# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 2
result1 = 'результат операции: 42'
result_index = result1.index(':')
new_result = int(result1[result_index + 1:])
print(new_result + 10)

result2 = 'результат операции: 514'
result_index = result2.index(':')
new_result = int(result2[result_index + 1:])
print(new_result + 10)

result3 = 'результат работы программы: 9'
result_index = result3.index(':')
new_result = int(result3[result_index + 1:])
print(new_result + 10)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print(f'Students {students} study these subjects: {subjects}')
