# server.py
import socket
import threading
from colorama import init, Fore, Style

# Inicializar colorama para colores en consola
init(autoreset=True)

HOST = '0.0.0.0'  # escuchar en todas las interfaces
PORT = 5000

def handle_client(conn, addr):
    print(Fore.GREEN + f"[+] Cliente conectado: {addr}")
    try:
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break
            if data.lower() == "quit":
                break

            # Parsear la solicitud
            parts = data.split(',')
            if len(parts) != 3:
                conn.sendall("❌ ERROR: formato inválido. Usa: num1,num2,op\n".encode('utf-8'))
                continue

            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
                op_raw = parts[2].strip().lower()
            except ValueError:
                conn.sendall("❌ ERROR: números inválidos\n".encode('utf-8'))
                continue

            # Normalizar operación (acepta texto extra o emojis)
            if "add" in op_raw:
                op = "add"
                symbol = "➕"
            elif "sub" in op_raw:
                op = "sub"
                symbol = "➖"
            elif "mul" in op_raw:
                op = "mul"
                symbol = "✖️"
            elif "div" in op_raw:
                op = "div"
                symbol = "➗"
            else:
                conn.sendall("❌ ERROR: operación desconocida (usa add, sub, mul, div)\n".encode('utf-8'))
                continue

            # Realizar operación
            if op == "add":
                result = num1 + num2
            elif op == "sub":
                result = num1 - num2
            elif op == "mul":
                result = num1 * num2
            elif op == "div":
                if num2 == 0:
                    conn.sendall("❌ ERROR: división por cero\n".encode('utf-8'))
                    continue
                result = num1 / num2

            # Enviar resultado al cliente
            conn.sendall(f"✅ Resultado {symbol}: {result}\n".encode('utf-8'))

            # Log en consola con colores
            print(Fore.CYAN + f"[{addr}] {num1} {symbol} {num2} = {result}")

    except Exception as e:
        print(Fore.RED + f"[ERROR] {addr}: {e}")
        try:
            conn.sendall(f"❌ ERROR: {str(e)}\n".encode('utf-8'))
        except:
            pass  # El socket ya podría estar cerrado
    finally:
        conn.close()
        print(Fore.YELLOW + f"[-] Cliente desconectado: {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(Fore.MAGENTA + f"[*] Servidor escuchando en {HOST}:{PORT} 🌟")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.daemon = True
            client_thread.start()

if __name__ == "__main__":
    start_server()
