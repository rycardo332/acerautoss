# ------------------------------------------------------------
# Dockerfile para una aplicación Django
# ------------------------------------------------------------
# Etapa 1: Imagen Base
FROM python:3.11-slim

# Etapa 2: Variables de Entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Etapa 3: Instalar Dependencias del Sistema
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    libcairo2-dev \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    shared-mime-info \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Etapa 4: Configurar el Directorio de Trabajo
WORKDIR /app

# Etapa 5: Instalar Dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 6: Copiar el Proyecto
COPY . .

# Etapa 7: Puerto que expone el contenedor
EXPOSE 8000

# Etapa 8: Comando por defecto (desarrollo con runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]