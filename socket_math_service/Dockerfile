# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo server.py (cliente.py está excluido por .dockerignore)
COPY server.py .

# Exponer el puerto (ajusta si tu servidor usa otro)
EXPOSE 5000

# Comando de ejecución
CMD ["python", "server.py"]
