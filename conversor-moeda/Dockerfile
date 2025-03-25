# Use a imagem oficial do OpenJDK
FROM openjdk:17-jdk-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo JAR para o diretório de trabalho
COPY target/conversor-moeda-0.0.1-SNAPSHOT.jar /app/conversor-moeda.jar

# Expor a porta 80
EXPOSE 80

# Comando para rodar o seu backend
ENTRYPOINT ["java", "-jar", "/app/conversor-moeda.jar"]
