# Usar a imagem oficial do Maven com OpenJDK 17
FROM maven:3.8.6-openjdk-17-slim AS build

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . .

# Construir o projeto
RUN mvn clean package

# Usar a imagem do OpenJDK 17 para rodar o aplicativo
FROM openjdk:17-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o JAR gerado para o contêiner
COPY --from=build /app/target/conversor-moeda-0.0.1-SNAPSHOT.jar conversor-moeda.jar

# Expor a porta em que a aplicação vai rodar
EXPOSE 25000

# Rodar o JAR
ENTRYPOINT ["java", "-jar", "conversor-moeda.jar"]
