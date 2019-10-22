from flask import Flask, request, jsonify
from usuario import Usuario

app = Flask(__name__)


@app.route("/")
def index():
    return ("Oi")


@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    data = request.json
    user = Usuario()
    user.cadastrar_usuario(data)
    return "Cadastrei mesmo"


@app.route("/deletar/<id>", methods=['DELETE'])
def delete(id):
    user = Usuario()
    user.deletar_usuario(id)
    return 'Deletei mesmo'


@app.route("/atualizar/<id>", methods=['PUT'])
def atualizar(id):
    data = request.json
    user = Usuario()
    user.atualizar_usuario(id,  data)
    return 'Atualizei mesmo'


@app.route("/mostrar/<id>")
@app.route("/mostrar/")
def mostrar(id=None):
    user = Usuario()
    data = user.mostrar_usuario(id)
    return jsonify(data)
