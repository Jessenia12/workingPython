from flask import Blueprint, request, jsonify
from models import db, Student

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students]), 200

@bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    s = Student.query.get_or_404(id)
    return jsonify(s.to_dict()), 200

@bp.route("/students", methods=["POST"])
def create_student():
    data = request.json
    s = Student(nombre=data["nombre"], carrera=data["carrera"], nivel=data["nivel"])
    db.session.add(s)
    db.session.commit()
    return jsonify(s.to_dict()), 201

@bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    s = Student.query.get_or_404(id)
    data = request.json
    s.nombre = data.get("nombre", s.nombre)
    s.carrera = data.get("carrera", s.carrera)
    s.nivel = data.get("nivel", s.nivel)
    db.session.commit()
    return jsonify(s.to_dict()), 200

@bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    s = Student.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200
