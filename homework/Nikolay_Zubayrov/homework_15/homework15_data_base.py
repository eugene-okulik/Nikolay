import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Nikolay',  'Zubayrov',  NULL)")

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = ('Лукоморье', 21292)
cursor.execute(query, values)

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = ('Теория', 21292)
cursor.execute(query, values)

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('1218', '14.09.2025', '17.09.2025')")
cursor.execute("INSERT INTO subjects (title) VALUES ('математика')")
cursor.execute("INSERT INTO subjects (title) VALUES ('физика')")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('контрольная', 12248)")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('экзамен математика', 12248)")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('контрольная физика', 12249)")
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('экзамен физика', 12249)")

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (5, 12698, 21292)
cursor.execute(query, values)

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (4, 12699, 21292)
cursor.execute(query, values)

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (2, 12700, 21292)
cursor.execute(query, values)

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (4, 12701, 21292)
cursor.execute(query, values)

query = '''
SELECT * FROM students JOIN marks ON students.id = marks.student_id 
WHERE name = 'Nikolay' AND second_name = 'Zubayrov'
'''
cursor.execute(query)
cursor.fetchall()

query = ("SELECT * FROM students JOIN books ON students.id = books.taken_by_student_id WHERE  name = 'Nikolay' AND "
         "second_name = 'Zubayrov'")
cursor.execute(query)
cursor.fetchall()

query = '''
SELECT students.name, students.second_name, groups.title, books.title, lessons.title, subjects.title, marks.value
FROM students  JOIN `groups` ON students.group_id = `groups`.id
JOIN books  ON books.taken_by_student_id = students.id
JOIN marks  ON marks.student_id = students.id JOIN lessons  ON lessons.id = marks.lesson_id JOIN subjects
ON subjects.id = lessons.subject_id WHERE students.id = 21292

'''
cursor.execute(query)
cursor.fetchall()

db.commit()

db.close()
