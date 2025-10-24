import React, { useEffect, useState } from "react";
import axios from "axios";
import StudentForm from "../components/StudentForm";
import StudentList from "../components/StudentList";

const API = process.env.REACT_APP_API_URL || "http://127.0.0.1:5000/api";

export default function Students() {
  const [students, setStudents] = useState([]);
  const [editing, setEditing] = useState(null);

  const fetchStudents = async () => {
    try {
      console.log("Llamando al backend...");
      const res = await axios.get(`${API}/students`);
      console.log("Datos recibidos:", res.data);
      setStudents(res.data);
    } catch (err) {
      console.error("Error al obtener estudiantes:", err);
    }
  };

  useEffect(() => {
    console.log("Componente Students montado");
    fetchStudents();
  }, []);

  const onCreate = async (data) => {
    try {
      await axios.post(`${API}/students`, data);
      fetchStudents();
    } catch (err) {
      console.error("Error al crear estudiante:", err);
    }
  };

  const onUpdate = async (id, data) => {
    try {
      await axios.put(`${API}/students/${id}`, data);
      setEditing(null);
      fetchStudents();
    } catch (err) {
      console.error("Error al actualizar estudiante:", err);
    }
  };

  const onDelete = async (id) => {
    try {
      await axios.delete(`${API}/students/${id}`);
      fetchStudents();
    } catch (err) {
      console.error("Error al eliminar estudiante:", err);
    }
  };

  return (
    <div className="students-page">
      <div className="container">
        <h2>📚 Sistema de Estudiantes</h2>

        {/* Formulario */}
        <div className="form-section">
          <StudentForm
            onCreate={onCreate}
            onUpdate={onUpdate}
            editing={editing}
          />
        </div>

        {/* Lista de estudiantes */}
        <div className="list-section">
          <StudentList
            students={students}
            onEdit={setEditing}
            onDelete={onDelete}
          />
        </div>
      </div>
    </div>
  );
}
