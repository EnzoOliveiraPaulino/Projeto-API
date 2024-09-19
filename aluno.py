from flask import Flask, jsonify, request

meuApp = Flask(__name__)

alunos = [
    {"id":1, "nome":"jose", "idade": "18", "turma":"a", "datanasc":"20/12/2005", "nota1":6, "nota2":7, "media":10},
]