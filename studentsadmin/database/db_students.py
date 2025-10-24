from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# 🔹 Rutas absolutas de templates y static
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(
    __name__,
    template_folder=os.path.join(project_root, 'templates'),
    static_folder=os.path.join(project_root, 'static')
)

# 🔹 Configuración MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:TuPasswordSeguro123@localhost/studentsadmin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 🔹 Modelo de estudiante
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    curso = db.Column(db.String(50))
    carrera = db.Column(db.String(50))
    facultad = db.Column(db.String(50))

# 🔹 Crear tablas si no existen
with app.app_context():
    db.create_all()

# 🔹 Página principal
@app.route('/', methods=['GET'])
def index():
    estudiantes = Student.query.all()
    estudiantes_lista = [
        [e.id, e.name, e.age, e.curso or "", e.carrera or "", e.facultad or ""] for e in estudiantes
    ]
    return render_template('index.html', estudiantes=estudiantes_lista, mostrar_tabla=True)

# 🔹 Agregar estudiante
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        name = request.form.get('nombre', '')
        age = request.form.get('edad', 0)
        curso = request.form.get('curso', '')
        carrera = request.form.get('carrera', '')
        facultad = request.form.get('facultad', '')

        try:
            age = int(age)
        except ValueError:
            age = 0

        nuevo = Student(name=name, age=age, curso=curso, carrera=carrera, facultad=facultad)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('agregar.html')

# 🔹 Editar estudiante
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    estudiante = Student.query.get(id)
    if not estudiante:
        return redirect(url_for('index'))

    if request.method == 'POST':
        estudiante.name = request.form.get('nombre', estudiante.name)
        try:
            estudiante.age = int(request.form.get('edad', estudiante.age))
        except ValueError:
            pass
        estudiante.curso = request.form.get('curso', estudiante.curso)
        estudiante.carrera = request.form.get('carrera', estudiante.carrera)
        estudiante.facultad = request.form.get('facultad', estudiante.facultad)
        db.session.commit()
        return redirect(url_for('index'))

    estudiante_lista = [estudiante.id, estudiante.name, estudiante.age, estudiante.curso, estudiante.carrera, estudiante.facultad]
    return render_template('editar.html', estudiante=estudiante_lista)

# 🔹 Eliminar estudiante
@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar(id):
    estudiante = Student.query.get(id)
    if estudiante:
        db.session.delete(estudiante)
        db.session.commit()
    return redirect(url_for('index'))

# 🔹 Salir a bienvenida
@app.route('/salir', methods=['POST'])
def salir():
    return render_template('index.html', mostrar_tabla=False, estudiantes=[])

# 🔹 Ejecutar app
if __name__ == "__main__":
    app.run(debug=True)
