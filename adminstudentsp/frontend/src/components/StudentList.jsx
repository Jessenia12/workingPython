import React from "react";
import { motion } from "framer-motion";

export default function StudentList({ students, onEdit, onDelete }) {
  console.log("Render StudentList", students);

  return (
    <div style={{ marginTop: 20 }}>
      {students.length === 0 ? (
        <p style={{ textAlign: "center", color: "#00ff88" }}>No hay estudiantes</p>
      ) : (
        <motion.div
          layout
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
            gap: 15,
          }}
        >
          {students.map((s) => (
            <motion.div
              key={s.id}
              layout
              whileHover={{ scale: 1.03 }}
              style={{
                background: "rgba(0,0,0,0.6)",
                padding: 20,
                borderRadius: 15,
                boxShadow: "0 0 25px #00ffaa, 0 0 50px #00ff88 inset",
                display: "flex",
                flexDirection: "column",
                gap: 10,
              }}
            >
              <div style={{ color: "#00ff88", fontWeight: "bold", fontSize: "1.1em" }}>
                {s.nombre}
              </div>
              <div style={{ color: "#ccc", fontSize: "0.95em" }}>
                {s.carrera} — {s.nivel}
              </div>
              <div style={{ display: "flex", gap: 10, justifyContent: "flex-end" }}>
                <button
                  onClick={() => onEdit(s)}
                  style={{
                    flex: 1,
                    padding: "8px 12px",
                    borderRadius: 10,
                    border: "none",
                    background: "#00ff88",
                    color: "#000",
                    fontWeight: "bold",
                    cursor: "pointer",
                    boxShadow: "0 0 15px #00ffaa, 0 0 30px #00ff88 inset",
                    transition: "0.3s",
                  }}
                  onMouseEnter={(e) => (e.target.style.boxShadow = "0 0 25px #00ffaa, 0 0 50px #00ff88 inset")}
                  onMouseLeave={(e) => (e.target.style.boxShadow = "0 0 15px #00ffaa, 0 0 30px #00ff88 inset")}
                >
                  Editar
                </button>
                <button
                  onClick={() => onDelete(s.id)}
                  style={{
                    flex: 1,
                    padding: "8px 12px",
                    borderRadius: 10,
                    border: "none",
                    background: "#ff4d4d",
                    color: "#fff",
                    fontWeight: "bold",
                    cursor: "pointer",
                    boxShadow: "0 0 20px #ff4d4d, 0 0 40px #ff1a1a inset",
                    transition: "0.3s",
                  }}
                  onMouseEnter={(e) => (e.target.style.boxShadow = "0 0 40px #ff4d4d, 0 0 80px #ff1a1a inset")}
                  onMouseLeave={(e) => (e.target.style.boxShadow = "0 0 20px #ff4d4d, 0 0 40px #ff1a1a inset")}
                >
                  Eliminar
                </button>
              </div>
            </motion.div>
          ))}
        </motion.div>
      )}
    </div>
  );
}
