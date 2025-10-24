import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3001,
    // Esto permite que React Router maneje rutas internas sin 404
    historyApiFallback: true
  }
});
