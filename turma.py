from flask import Flask, jsonify, request

app = Flask(__name__)

turmas = [
    {
        "id":1, 
        "descricao":"obs", 
        "professor":"caio", 
        "ativo":"sim"
    }
]



@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify({'turmas': turmas})


@app.route('/turmas/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            return jsonify(turma)
    return jsonify({'mensagem': 'Turma não encontrado'}), 404


@app.route('/turmas', methods=['POST'])
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


@app.route('/turmas/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            data = request.json
            turma['descricao'] = data.get('descricao', turma['descricao'])
            turma['professor'] = data.get('professor', turma['professor'])
            turma['ativo'] = data.get('ativo', turma['ativo'])
    return jsonify({'mensagem': 'Turma não encontrado'}), 404


@app.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma removido'})
    return jsonify({'mensagem': 'Turma não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
