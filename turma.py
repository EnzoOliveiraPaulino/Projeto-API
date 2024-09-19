from flask import Flask, jsonify, request

meuApp = Flask(__name__)

turmas = [
    {"id":1, "descricao":"obs", "professor":"caio", "ativo":"sim"},
]