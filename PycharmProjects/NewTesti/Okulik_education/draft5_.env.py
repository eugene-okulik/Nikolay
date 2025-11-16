import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv()

# Подключение к базе
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)


def get_matching_data(name, second_name, group_title, book_title, subject_title, lesson_title, mark_value):
    """
    Функция для выполнения параметризованного запроса.
    Возвращает список словарей с совпадениями или пустой список.
    """
    query = '''
    SELECT
    students.name, students.second_name, groups.title AS group_title, books.title AS book_title, subjects.title AS subject_title, lessons.title AS lesson_title, marks.value
    FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    JOIN books ON books.taken_by_student_id = students.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON lessons.id = marks.lesson_id
    JOIN subjects ON subjects.id = lessons.subject_id
    WHERE students.name = %s
    AND students.second_name = %s
    AND groups.title = %s
    AND books.title = %s
    AND subjects.title = %s
    AND lessons.title = %s
    AND marks.value = %s
    '''

    cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
    return cursor.fetchall()


# Путь к файлу
path = 'C:\\Users\Николай\\Nikolay\\homework\\eugene_okulik\\Lesson_16\\hw_data'
file_path = os.path.join(path, 'data.csv')

missing_data = []

with open(file_path, newline='', encoding='utf-8') as csv_file:
    file_data = csv.reader(csv_file)
    header = next(file_data)  # Пропускаем заголовок

    for row in file_data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

        # Вызываем функцию для проверки
        matches = get_matching_data(name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)

        if not matches:  # Если совпадений нет, добавляем в отсутствующие
            missing_data.append(row)

print("Данные из CSV, отсутствующие в базе:")
if missing_data:
    for item in missing_data:
        print(
            f"Имя: {item[0]}, Фамилия: {item[1]}, Группа: {item[2]}, Книга: {item[3]}, Предмет: {item[4]}, Урок: {item[5]}, Оценка: {item[6]}")
else:
    print("Все данные из CSV найдены в базе.")

# Закрываем соединение
cursor.close()
db.close()
