# Conversor de Moedas - Backend

Este projeto é uma API REST em Flask para cadastro, consulta, atualização e remoção de moedas, conectando-se a um banco de dados MySQL hospedado na AWS RDS.

## Funcionalidades

- **POST /moedas**: Cadastra uma nova moeda.
- **GET /moedas**: Lista todas as moedas cadastradas.
- **GET /moedas/<nome>**: Busca uma moeda pelo nome.
- **PUT /moedas/<nome>**: Atualiza o valor de uma moeda.
- **DELETE /moedas/<nome>**: Remove uma moeda.

## Estrutura

- `app.py`: Código principal da API Flask.
- `db.py`: Script de conexão com o banco de dados MySQL.
- `Dockerfile`: Permite rodar a aplicação em container Docker.

## Como rodar localmente

1. **Clone o repositório**
   ```bash
   git clone <url-do-repo>
   cd aws-project-backend
   ```

2. **Configure o banco de dados**
   - Certifique-se de ter um banco MySQL acessível e atualize as credenciais em `db.py` e/ou `app.py` se necessário.

3. **Instale as dependências**
   ```bash
   pip install flask flask-cors mysql-connector-python
   ```

4. **Execute a aplicação**
   ```bash
   python3 app.py
   ```

## Como rodar com Docker

1. **Build da imagem**
   ```bash
   docker build -t conversor-backend .
   ```

2. **Execute o container**
   ```bash
   docker run -p 5000:5000 conversor-backend
   ```

## Exemplos de uso

### POST /moedas

```bash
curl -X POST http://localhost:5000/moedas \
  -H "Content-Type: application/json" \
  -d '{"nome": "USD", "valor": 5.20}'
```

### GET /moedas

```bash
curl http://localhost:5000/moedas
```

## Observações

- Certifique-se de que o banco de dados está acessível a partir do ambiente onde a API está rodando.
- Para ambientes AWS, verifique as configurações de VPC, subnets e grupos de segurança.

---

Desenvolvido por Camila Sousa, Fernando Morales, Lucas Deosoci, Paola Polito.
