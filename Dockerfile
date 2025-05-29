FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instalar dependências necessárias
<<<<<<< HEAD
RUN pip install --no-cache-dir flask flask-cors mysql-connector-python
=======
RUN pip install --no-cache-dir flask flask-cors flask-sqlalchemy pymysql
>>>>>>> 7e64cee8be95282fd73d7073b5f2638e5c19d018

EXPOSE 5000

CMD ["python", "app.py"]