FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instalar dependências necessárias
RUN pip install --no-cache-dir flask flask-cors mysql-connector-python

EXPOSE 5000

CMD ["python", "app.py"]