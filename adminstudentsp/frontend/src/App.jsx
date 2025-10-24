import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Welcome from "./pages/Welcome";
import Students from "./pages/Students";

export default function App() {
  return (
    <div style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
      {/* Navegación */}
      <nav className="nav-bar">
        <Link className="nav-link" to="/">Bienvenida</Link>
        <Link className="nav-link" to="/students">Sistema Estudiantes</Link>
      </nav>

      {/* Rutas */}
      <div style={{ flex: 1 }}>
        <Routes>
          <Route path="/" element={<Welcome />} />
          <Route path="/students" element={<Students />} />
        </Routes>
      </div>

      {/* Footer */}
<div
  style={{
    display: "flex",
    justifyContent: "space-between",
    padding: "10px 20px",
    borderTop: "1px solid #ccc",
    fontSize: "14px",
    color: "#ffeb3b", // amarillo brillante
    fontWeight: "bold",
    textShadow: "1px 1px 2px #000" // ligera sombra para resaltar la letra
  }}
>
  <span>© 2025</span>
  <span>Elaborado por: Jessenia Zambrano</span>
</div>

    </div>
  );
}
