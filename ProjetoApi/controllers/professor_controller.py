from flask import jsonify, request
from models.professor import professores

def get_professores():
    return jsonify({'professores': professores})

def create_professor():
    data = request.json
    professor = {
        'id': len(professores) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacao': data['observacao']
    }
    professores.append(professor)
    return jsonify(professor), 201

def get_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            return jsonify(professor)
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404
