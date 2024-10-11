from flask import jsonify, request
from models.aluno import alunos

def get_alunos():
    return jsonify({'alunos': alunos})

def create_aluno():
    data = request.json
    aluno = {
        'id': len(alunos) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'turma': data['turma'],
        'data_nascimento': data['data_nascimento'],
        'nota_primeiro_semestre': data['nota_primeiro_semestre'],
        'nota_segundo_semestre': data['nota_segundo_semestre'],
        'media_final': (data['nota_primeiro_semestre'] + data['nota_segundo_semestre']) / 2
    }
    alunos.append(aluno)
    return jsonify(aluno), 201