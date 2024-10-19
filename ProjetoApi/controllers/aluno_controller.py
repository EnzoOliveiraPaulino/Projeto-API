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

def get_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return jsonify(aluno)
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404


def update_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            data = request.json
            aluno['nome'] = data.get('nome', aluno['nome'])
            aluno['idade'] = data.get('idade', aluno['idade'])
            aluno['turma'] = data.get('turma', aluno['turma'])
            aluno['data_nascimento'] = data.get('data_nascimento', aluno['data_nascimento'])
            aluno['nota_primeiro_semestre'] = data.get('nota_primeiro_semestre', aluno['nota_primeiro_semestre'])
            aluno['nota_segundo_semestre'] = data.get('nota_segundo_semestre', aluno['nota_segundo_semestre'])
            aluno['media_final'] = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2
            return jsonify(aluno)
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404
