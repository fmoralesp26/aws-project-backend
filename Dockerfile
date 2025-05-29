FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instalar dependências necessárias
RUN pip install --no-cache-dir flask flask-cors flask-sqlalchemy pymysql

EXPOSE 5000

CMD ["python", "app.py"]