import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Nikolay', 'Zubayrov', NULL)")
student_id = cursor.lastrowid
print(f"Создан студент с ID: {student_id} (пока без группы)")

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [('Лукоморье', student_id), ('Теория', student_id)]
cursor.executemany(query, values)
print(f"Добавлено 2 книги для студента {student_id}")

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('1218', '14.09.2025', '17.09.2025')")
group_id = cursor.lastrowid
print(f"Создана группа с ID: {group_id}")

query = 'UPDATE students SET group_id = %s WHERE id = %s'
values = (group_id, student_id)
cursor.execute(query, values)
print(f"Студент {student_id} добавлен в группу {group_id}")

cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('математика',))
subject_math_id = cursor.lastrowid
print(f"Добавлен предмет 'математика' с ID: {subject_math_id}")

cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('физика',))
subject_physics_id = cursor.lastrowid
print(f"Добавлен предмет 'физика' с ID: {subject_physics_id}")

lesson_ids = []  # Список для хранения ID уроков
query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values = [
    ('контрольная', subject_math_id),
    ('экзамен математика', subject_math_id),
    ('контрольная физика', subject_physics_id),
    ('экзамен физика', subject_physics_id)
]

for value in values:
    cursor.execute(query, value)
    lesson_ids.append(cursor.lastrowid)

print(f"Добавлено {len(lesson_ids)} урока с ID: {lesson_ids}")

query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values = [
    (5, lesson_ids[0], student_id),
    (4, lesson_ids[1], student_id),
    (2, lesson_ids[2], student_id),
    (4, lesson_ids[3], student_id)
]
cursor.executemany(query, values)
print(f'Добавлено 4 оценки для студента {student_id}')
db.commit()

query = '''
SELECT * FROM students JOIN marks ON students.id = marks.student_id
WHERE name = 'Nikolay' AND second_name = 'Zubayrov' ORDER BY marks.id DESC LIMIT 4
'''
cursor.execute(query)
result1 = cursor.fetchall()
print("Результат первого SELECT (студент и оценки):")
print(result1)

query = ("SELECT * FROM students JOIN books ON students.id = books.taken_by_student_id WHERE  name = 'Nikolay'"
         "AND second_name = 'Zubayrov' ORDER BY books.id DESC LIMIT 2")

cursor.execute(query)
result2 = cursor.fetchall()
print("Результат второго SELECT (студент и книги):")
print(result2)

query = '''
SELECT students.name, students.second_name, groups.title, books.title, lessons.title, subjects.title, marks.value
FROM students
JOIN `groups` ON students.group_id = `groups`.id
JOIN books ON books.taken_by_student_id = students.id
JOIN marks ON marks.student_id = students.id
JOIN lessons ON lessons.id = marks.lesson_id
JOIN subjects ON subjects.id = lessons.subject_id
WHERE students.id = %s
'''
cursor.execute(query, (student_id,))
result3 = cursor.fetchall()
print(f"Результат третьего SELECT (полный JOIN для студента {student_id}):")
print(result3)

db.close()
