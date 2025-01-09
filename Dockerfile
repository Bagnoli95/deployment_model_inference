# Usa una imagen base con Python
FROM python:3.10-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app/src

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar TensorFlow y las demás dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8080

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
