import sqlite3

conn = sqlite3.connect('studentsuleam.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER)
''')

print('La base de datos "studentsuleam.db" y la tabla "students" fueron creadas exitosamente o ya existían.')

conn.commit()

# 🟢 Borrar todos los registros anteriores
cursor.execute('DELETE FROM students')

studentsList = [('Jessenia', 26), ('Javier', 31), ('Madleine', 8)]

for name, age in studentsList:
    print(name)
    print(age)
    cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

print('Exist')

cursor.execute('SELECT * FROM students')

for row in cursor.fetchall():
    print(f'id: {row[0]}, Name: {row[1]}, Age: {row[2]}')

conn.commit()
conn.close()
