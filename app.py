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
    return jsonify(data)
