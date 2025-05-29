import mysql.connector

try:
    conn = mysql.connector.connect(
        host="lab-db.cznhouudifzh.us-east-1.rds.amazonaws.com",
        user="main",
        password="lab-password",
        database="banco_moedas"
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print("Erro ao conectar ao MySQL:")
    print(f"Tipo: {type(err)}")
    print(f"Mensagem: {err}")