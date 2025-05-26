# Usar imagem oficial do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar requirements (se tivesse, mas aqui não tem) e código
COPY . .

# Instalar Flask
RUN pip install --no-cache-dir flask

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
