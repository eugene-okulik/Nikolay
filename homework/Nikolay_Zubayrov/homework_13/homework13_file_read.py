import datetime
import os

# Путь к папке с файлом
path = 'C:\\Users\\Николай\\Nikolay\\homework\\eugene_okulik\\hw_13'

# Полный путь к файлу
file_path = os.path.join(path, 'data.txt')
new_file_path = os.path.join(path, 'data.txt2')


# Открываем файл по полному пути
def read_file():
    with open(file_path, 'r', encoding='utf-8') as data_file:
        # Читаем содержимое файла
        for file in data_file.readlines():
            yield file


for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        if data_line.startswith('1'):
            print(data_line.replace('2023-11-27 20:34:13.212967', '2023-12-04 20:34:13.212967'))
        elif data_line.startswith('2'):
            data_line = '2023-07-15 18:25:10.121473'
            date = datetime.datetime.strptime(data_line, '%Y-%m-%d %H:%M:%S.%f')
            day = date.strftime('%A')
            print(f"День недели: {day}")
        elif data_line.startswith('3'):
            now = datetime.datetime.now()
            new_date = datetime.datetime.now().replace(year=2023, month=6, day=12, hour=15, minute=23, second=45,
                                                       microsecond=312167)
            print(f'{now - new_date} назад была эта дата')

# new_data1 = data.split()
# print(new_data1)
# new_data1[1] = '2023-12-04'
# print(new_data1[0:3])
# new_data2[19] = 'четверг'
#
#


# Выводим содержимое файла
# print(new_data)
