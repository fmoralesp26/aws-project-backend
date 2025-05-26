from flask import Flask, request, jsonify

app = Flask(__name__)

class Moeda:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

# Banco de dados em memória (lista)
moedas = []

# CREATE
@app.route('/moedas', methods=['POST'])
def criar_moeda():
    dados = request.json
    nome = dados.get('nome')
    valor = dados.get('valor')

    if not nome or valor is None:
        return jsonify({'erro': 'nome e valor são obrigatórios'}), 400

    if any(m.nome == nome for m in moedas):
        return jsonify({'erro': 'Moeda já existe'}), 400

    moeda = Moeda(nome, valor)
    moedas.append(moeda)
    return jsonify({'mensagem': 'Moeda criada', 'moeda': {'nome': nome, 'valor': valor}}), 201

# READ ALL
@app.route('/moedas', methods=['GET'])
def listar_moedas():
    resultado = [{'nome': m.nome, 'valor': m.valor} for m in moedas]
    return jsonify(resultado), 200

# READ ONE
@app.route('/moedas/<string:nome>', methods=['GET'])
def buscar_moeda(nome):
    moeda = next((m for m in moedas if m.nome == nome), None)
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404
    return jsonify({'nome': moeda.nome, 'valor': moeda.valor}), 200

# UPDATE
@app.route('/moedas/<string:nome>', methods=['PUT'])
def atualizar_moeda(nome):
    moeda = next((m for m in moedas if m.nome == nome), None)
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404

    dados = request.json
    valor = dados.get('valor')
    if valor is None:
        return jsonify({'erro': 'valor é obrigatório para atualização'}), 400

    moeda.valor = valor
    return jsonify({'mensagem': 'Moeda atualizada', 'moeda': {'nome': moeda.nome, 'valor': moeda.valor}}), 200

# DELETE
@app.route('/moedas/<string:nome>', methods=['DELETE'])
def deletar_moeda(nome):
    global moedas
    moeda = next((m for m in moedas if m.nome == nome), None)
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404

    moedas = [m for m in moedas if m.nome != nome]
    return jsonify({'mensagem': 'Moeda deletada'}), 200

if __name__ == '__main__':
    app.run(debug=True)
