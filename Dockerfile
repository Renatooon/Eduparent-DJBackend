FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY gestion_escolar/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copiar todo el proyecto (incluye manage.py, gestion_escolar/, etc.)
COPY . .

# Exponer el puerto que usará Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo
CMD ["python", "gestion_escolar/manage.py", "runserver", "0.0.0.0:8000"]