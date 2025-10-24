from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    carrera = db.Column(db.String(120), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "carrera": self.carrera, "nivel": self.nivel}
