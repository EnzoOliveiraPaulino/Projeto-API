from flask import jsonify, request
from models.turma import turmas

def get_turmas():
    return jsonify({'turmas': turmas})

def create_turma():
    data = request.json
    turma = {
        'id': len(turmas) + 1,
        'descricao': data['descricao'],
        'professor': data['professor'],
        'ativo': data['ativo']
    }
    turmas.append(turma)
    return jsonify(turma), 201

def get_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            return jsonify(turma)
    return jsonify({'mensagem': 'Turma não encontrada'}), 404
