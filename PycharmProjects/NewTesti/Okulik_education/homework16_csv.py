import csv
import os

path = 'C:\\Users\Николай\\Nikolay\\homework\\eugene_okulik\\Lesson_16\\hw_data'

file_path = os.path.join(path, 'data.csv')



with open(file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        print(row)




