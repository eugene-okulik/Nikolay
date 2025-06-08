# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


# Задание 2
result1 = 'результат операции: 42'
my_list = result1.split()
print(int(my_list[2]) + 10)

result2 = 'результат операции: 514'
my_list = result2.split()
print(int(my_list[2]) + 10)

result3 = 'результат работы программы: 9'
my_list = result3.split()
print(int(my_list[3]) + 10)


# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print(f'Students {students} study these subjects: {subjects}')
