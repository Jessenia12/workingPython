from flask import Flask, render_template, request, redirect, url_for, session, flash
from database.db_students import get_connection, init_db

app = Flask(__name__)
app.secret_key = "clave_super_secreta"  # necesario para session y flash

# Inicializar la base de datos
init_db()

@app.route('/')
def index():
    mostrar_tabla = session.get('mostrar_tabla', False)
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    estudiantes = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', estudiantes=estudiantes, mostrar_tabla=mostrar_tabla)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        curso = request.form['curso']
        carrera = request.form['carrera']
        facultad = request.form['facultad']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (nombre, edad, curso, carrera, facultad) VALUES (?, ?, ?, ?, ?)",
            (nombre, edad, curso, carrera, facultad)
        )
        conn.commit()
        conn.close()

        # Activar tabla y mostrar mensaje
        session['mostrar_tabla'] = True
        flash(f'Estudiante "{nombre}" registrado con éxito ✅')
        return redirect(url_for('agregar'))

    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        curso = request.form['curso']
        carrera = request.form['carrera']
        facultad = request.form['facultad']
        cursor.execute("""
            UPDATE students
            SET nombre=?, edad=?, curso=?, carrera=?, facultad=?
            WHERE id=?
        """, (nombre, edad, curso, carrera, facultad, id))
        conn.commit()
        conn.close()

        flash(f'Estudiante "{nombre}" actualizado con éxito ✏️')
        return redirect(url_for('editar', id=id))

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    estudiante = cursor.fetchone()
    conn.close()
    return render_template('editar.html', estudiante=estudiante)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    flash("Estudiante eliminado correctamente 🗑️")
    return redirect(url_for('index'))

@app.route('/salir', methods=['POST'])
def salir():
    session.pop('mostrar_tabla', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
