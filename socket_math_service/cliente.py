# cliente.py
import socket
import gradio as gr

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

def conectar_y_enviar(num1, num2, operacion):
    """Envía una solicitud al servidor y recibe la respuesta"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            mensaje = f"{num1},{num2},{operacion}"
            s.sendall(mensaje.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            return data.strip()
    except ConnectionRefusedError:
        return "❌ Error: No se pudo conectar al servidor. Asegúrate de que esté en ejecución."
    except Exception as e:
        return f"⚠️ Error inesperado: {str(e)}"

# 🎨 Interfaz moderna
titulo = "🧮 Servicio de Operaciones Matemáticas"
descripcion = """
Bienvenido al **Servicio de Cálculo**.  
Introduce dos números y selecciona la operación que deseas realizar.  
Este sistema usa **sockets TCP** para comunicarse con el servidor.
"""

iface = gr.Interface(
    fn=conectar_y_enviar,
    inputs=[
        gr.Number(label="Número 1", precision=3),
        gr.Number(label="Número 2", precision=3),
        gr.Radio(
            ["add ➕ (Suma)", "sub ➖ (Resta)", "mul ✖️ (Multiplicación)", "div ➗ (División)"],
            label="Selecciona la operación",
        )
    ],
    outputs=gr.Textbox(label="Resultado"),
    title=titulo,
    description=descripcion,
    theme=gr.themes.Soft(primary_hue="green", secondary_hue="blue"),
    examples=[
        [5, 2, "add ➕ (Suma)"],
        [8, 3, "sub ➖ (Resta)"],
        [6, 7, "mul ✖️ (Multiplicación)"],
        [10, 2, "div ➗ (División)"]
    ]
)

# 🌍 Activar enlace público
iface.launch(share=True)
