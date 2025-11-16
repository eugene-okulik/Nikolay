import mysql.connector as mysql
import dotenv
import os
import csv
# Подключение к базе данных

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
path = 'C:\\Users\\Николай\\Nikolay\\homework\\eugene_okulik\\Lesson_16\\hw_data'
file_path = os.path.join(path, 'data.csv')

# Открываем CSV-файл
with open(file_path, 'r', encoding='utf-8') as file:
    file_data = csv.reader(file)
    next(file_data)  # Пропускаем заголовок (первую строку)

    # Список для отсутствующих данных
    missing_data = []

    # Цикл по строкам CSV
    for row in file_data:
        # Распаковываем строку в переменные (предполагаем 7 колонок)
        name, second_name, group_title, book_title, subject_title, lesson_title, value = row

        # Создаём курсор для запроса
        cursor = db.cursor()

        # Параметризованный запрос: ищем запись, где все поля совпадают
        query = """
        SELECT COUNT(*) 
        FROM students 
        JOIN groups ON students.group_id = groups.id 
        JOIN books ON students.book_id = books.id 
        JOIN subjects ON books.subject_id = subjects.id 
        JOIN lessons ON subjects.id = lessons.subject_id 
        WHERE students.name = %s 
          AND students.second_name = %s 
          AND groups.title = %s 
          AND books.title = %s 
          AND subjects.title = %s 
          AND lessons.title = %s 
          AND students.value = %s
        """

        # Выполняем запрос с параметрами (безопасно от SQL-инъекций)
        cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, value))

        # Получаем результат: fetchone()[0] вернёт число совпадений (0 или больше)
        result = cursor.fetchone()[0]

        # Проверяем: если result == 0, значит, записи нет — добавляем в список
        if result == 0:
            missing_data.append(row)

        # Закрываем курсор (важно после каждого запроса)
        cursor.close()

# Закрываем соединение после всех операций
db.close()

# Выводим результат
print("Данные из CSV, отсутствующие в базе:")
if missing_data:
    for item in missing_data:
        print(
            f"Имя: {item[0]}, Фамилия: {item[1]}, Группа: {item[2]}, Книга: {item[3]}, Предмет: {item[4]},"
            f" Урок: {item[5]}, Оценка: {item[6]}"
        )
else:
    print("Все данные из CSV найдены в базе.")
