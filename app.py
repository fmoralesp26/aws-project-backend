from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# 🔗 Conexão com o banco RDS
conn = mysql.connector.connect(
    host="lab-db.cznhouudifzh.us-east-1.rds.amazonaws.com",        # exemplo: "meu-banco.c8dfx123abc.us-east-1.rds.amazonaws.com"
    user="main",             # exemplo: "admin"
    password="lab-password",
    database="banco_moedas"            # exemplo: "banco_moedas"
)

cursor = conn.cursor(dictionary=True)

@app.route('/moedas', methods=['POST'])
def criar_moeda():
    dados = request.get_json()
    nome = dados.get('nome')
    valor = dados.get('valor')

    if not nome or valor is None:
        return jsonify({'erro': 'nome e valor são obrigatórios'}), 400

    cursor.execute("SELECT * FROM moedas WHERE nome = %s", (nome,))
    if cursor.fetchone():
        return jsonify({'erro': 'Moeda já existe'}), 400

    cursor.execute("INSERT INTO moedas (nome, valor) VALUES (%s, %s)", (nome, valor))
    conn.commit()

    return jsonify({'mensagem': 'Moeda criada', 'moeda': {'nome': nome, 'valor': valor}}), 201

@app.route('/moedas', methods=['GET'])
def listar_moedas():
    cursor.execute("SELECT nome, valor FROM moedas")
    moedas = cursor.fetchall()
    return jsonify(moedas), 200

@app.route('/moedas/<string:nome>', methods=['GET'])
def buscar_moeda(nome):
    cursor.execute("SELECT nome, valor FROM moedas WHERE nome = %s", (nome,))
    moeda = cursor.fetchone()
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404
    return jsonify(moeda), 200

@app.route('/moedas/<string:nome>', methods=['PUT'])
def atualizar_moeda(nome):
    dados = request.get_json()
    novo_valor = dados.get('valor')

    if novo_valor is None:
        return jsonify({'erro': 'valor é obrigatório para atualização'}), 400

    cursor.execute("SELECT * FROM moedas WHERE nome = %s", (nome,))
    if cursor.fetchone() is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404

    cursor.execute("UPDATE moedas SET valor = %s WHERE nome = %s", (novo_valor, nome))
    conn.commit()
    return jsonify({'mensagem': 'Moeda atualizada', 'moeda': {'nome': nome, 'valor': novo_valor}}), 200

@app.route('/moedas/<string:nome>', methods=['DELETE'])
def deletar_moeda(nome):
    cursor.execute("SELECT * FROM moedas WHERE nome = %s", (nome,))
    if cursor.fetchone() is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404

    cursor.execute("DELETE FROM moedas WHERE nome = %s", (nome,))
    conn.commit()
    return jsonify({'mensagem': 'Moeda deletada'}), 200

if __name__ == '__main__':
    app.run(debug=True)
