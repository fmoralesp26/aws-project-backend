# Usar a imagem oficial do Maven com OpenJDK 17
FROM maven:3.8-jdk-17-slim AS build

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do projeto para o diretório de trabalho
COPY . /app

# Compilar o projeto e empacotar o arquivo JAR
RUN mvn clean package -DskipTests

# Usar a imagem oficial do OpenJDK para a execução
FROM openjdk:17-jdk-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo JAR da fase anterior para o contêiner
COPY --from=build /app/target/conversor-moeda-0.0.1-SNAPSHOT.jar /app/conversor-moeda.jar

# Expor a porta 80
EXPOSE 80

# Executar o arquivo JAR
ENTRYPOINT ["java", "-jar", "/app/conversor-moeda.jar"]
