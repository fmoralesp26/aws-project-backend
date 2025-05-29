from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# Usar variável de ambiente para conexão com banco MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://main:lab-password@lab-db.cznhouudifzh.us-east-1.rds.amazonaws.com:3306/lab-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Moeda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    valor = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {'nome': self.nome, 'valor': self.valor}

@app.route('/moedas', methods=['POST'])
def criar_moeda():
    dados = request.get_json()
    nome = dados.get('nome')
    valor = dados.get('valor')

    if not nome or valor is None:
        return jsonify({'erro': 'nome e valor são obrigatórios'}), 400

    if Moeda.query.filter_by(nome=nome).first():
        return jsonify({'erro': 'Moeda já existe'}), 400

    moeda = Moeda(nome=nome, valor=valor)
    db.session.add(moeda)
    db.session.commit()

    return jsonify({'mensagem': 'Moeda criada', 'moeda': moeda.to_dict()}), 201

@app.route('/moedas', methods=['GET'])
def listar_moedas():
    moedas = Moeda.query.all()
    resultado = [m.to_dict() for m in moedas]
    return jsonify(resultado), 200

@app.route('/moedas/<string:nome>', methods=['GET'])
def buscar_moeda(nome):
    moeda = Moeda.query.filter_by(nome=nome).first()
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404
    return jsonify(moeda.to_dict()), 200

@app.route('/moedas/<string:nome>', methods=['PUT'])
def atualizar_moeda(nome):
    moeda = Moeda.query.filter_by(nome=nome).first()
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404

    dados = request.get_json()
    valor = dados.get('valor')
    if valor is None:
        return jsonify({'erro': 'valor é obrigatório para atualização'}), 400

    moeda.valor = valor
    db.session.commit()
    return jsonify({'mensagem': 'Moeda atualizada', 'moeda': moeda.to_dict()}), 200

@app.route('/moedas/<string:nome>', methods=['DELETE'])
def deletar_moeda(nome):
    moeda = Moeda.query.filter_by(nome=nome).first()
    if moeda is None:
        return jsonify({'erro': 'Moeda não encontrada'}), 404

    db.session.delete(moeda)
    db.session.commit()
    return jsonify({'mensagem': 'Moeda deletada'}), 200

if __name__ == '__main__':
    # Rodar no host 0.0.0.0 para aceitar conexões externas no container/Docker/EC2
    app.run(host='0.0.0.0', port=5000, debug=True)
