import React from "react";
import { motion } from "framer-motion";

export default function Welcome() {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: "80vh",
        flexDirection: "column",
        backgroundColor: "#f0f8ff", // fondo suave azul claro
        textAlign: "center",
        padding: "20px",
        borderRadius: "10px",
        boxShadow: "0 4px 10px rgba(0,0,0,0.1)"
      }}
    >
      <motion.h1
        initial={{ y: -50, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.7 }}
        style={{
          fontSize: "2rem",
          color: "#4caf50", // verde moderno
          marginBottom: "15px",
          textShadow: "1px 1px 2px rgba(0,0,0,0.2)"
        }}
      >
        Bienvenido al sistema de registro de estudiantes
      </motion.h1>
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        style={{
          fontSize: "1.2rem",
          color: "#333",
          maxWidth: "600px"
        }}
      >
        Haz click en "Sistema Estudiantes" para empezar.
      </motion.p>
    </div>
  );
}
