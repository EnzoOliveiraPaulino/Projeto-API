from flask import Flask, jsonify, request

meuApp = Flask(__name__)

professores = [  
    {"id":1, "nome":"caio", "idade": "40", "materia":"historia", "observacao":"obs"},
    ]
Turma = [
    {"id":1, "descricao":"obs", "professor":"caio", "ativo":"sim"},
]
aluno = [
    {"id":1, "nome":"jose", "idade": "18", "turma":"a", "datanasc":"20/12/2005", "nota1":6, "nota2":7, "media":}
]
@meuApp.route('/professors', methods=['GET'])
def get_users():
    return jsonify({'professores': professores})

@meuApp.route('/professors', methods=['POST'])
def create_user():
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

@meuApp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for usuario in usuarios:
        print(usuario)
        if usuario['id'] == user_id:
            return usuario
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404

@meuApp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            data = request.json
            usuario['nome'] = data.get('nome', usuario['nome'])
            usuario['email'] = data.get('email', usuario['email'])
            return jsonify(usuario)
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404

@meuApp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário removido'})
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    meuApp.run(debug=True)