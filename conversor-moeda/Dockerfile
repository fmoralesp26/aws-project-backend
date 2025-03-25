# Usar a imagem oficial do OpenJDK para a construção
FROM maven:3.8.6-openjdk-17-slim AS build

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo pom.xml e fazer o cache das dependências do Maven
COPY pom.xml .

# Baixar as dependências do projeto
RUN mvn dependency:go-offline

# Copiar o código-fonte para dentro do contêiner
COPY src /app/src

# Construir o arquivo JAR do Spring Boot
RUN mvn clean package -DskipTests

# Usar uma imagem mais leve do OpenJDK para rodar o contêiner
FROM openjdk:17-jdk-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo JAR gerado do estágio de build para o contêiner
COPY --from=build /app/target/conversor-moeda-0.0.1-SNAPSHOT.jar /app/conversor-moeda.jar

# Expôr a porta que o Spring Boot usará
EXPOSE 8080

# Comando para rodar o Spring Boot no contêiner
ENTRYPOINT ["java", "-jar", "conversor-moeda.jar"]

