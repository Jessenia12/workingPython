import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";

export default function StudentForm({ onCreate, onUpdate, editing, onDelete }) {
  const [form, setForm] = useState({ nombre: "", carrera: "", nivel: "" });

  useEffect(() => {
    if (editing) setForm(editing);
    else setForm({ nombre: "", carrera: "", nivel: "" });
  }, [editing]);

  const submit = (e) => {
    e.preventDefault();
    if (editing) onUpdate(editing.id, form);
    else onCreate(form);
    setForm({ nombre: "", carrera: "", nivel: "" });
  };

  const inputStyle = {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    marginBottom: "10px",
    fontSize: "16px",
    width: "100%",
    boxSizing: "border-box"
  };

  const buttonStyle = {
    padding: "10px",
    borderRadius: "8px",
    border: "none",
    backgroundColor: "#4caf50",
    color: "white",
    cursor: "pointer",
    fontSize: "16px",
    marginBottom: "10px"
  };

  const deleteButtonStyle = {
    ...buttonStyle,
    backgroundColor: "#f44336"
  };

  return (
    <motion.form
      initial={{ scale: 0.95, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.3 }}
      onSubmit={submit}
      style={{ maxWidth: "400px", margin: "auto", display: "flex", flexDirection: "column" }}
    >
      <input
        required
        placeholder="Nombre"
        value={form.nombre}
        onChange={(e) => setForm({ ...form, nombre: e.target.value })}
        style={inputStyle}
      />
      <input
        required
        placeholder="Carrera"
        value={form.carrera}
        onChange={(e) => setForm({ ...form, carrera: e.target.value })}
        style={inputStyle}
      />
      <input
        required
        placeholder="Nivel"
        value={form.nivel}
        onChange={(e) => setForm({ ...form, nivel: e.target.value })}
        style={inputStyle}
      />
      <button type="submit" style={buttonStyle}>
        {editing ? "Actualizar" : "Registrar"}
      </button>

      {editing && onDelete && (
        <button type="button" style={deleteButtonStyle} onClick={() => onDelete(editing.id)}>
          Eliminar
        </button>
      )}
    </motion.form>
  );
}
