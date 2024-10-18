alunos = [
    {
        "id": 1,
        "nome": "João Silva",
        "idade": 15,
        "turma": "9A",
        "data_nascimento": "2008-05-14",
        "nota_primeiro_semestre": 8.5,
        "nota_segundo_semestre": 7.5,
        "media_final": (8.5 + 7.5) / 2,
    }
]
def criar_aluno(data):
    """Cria um novo aluno com os dados fornecidos."""
    
    # Validação de dados
    required_fields = ['nome', 'idade', 'turma', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Campo '{field}' é obrigatório.")

    aluno = {
        'id': len(alunos) + 1,  # Gera um novo ID
        'nome': data['nome'],
        'idade': data['idade'],
        'turma': data['turma'],
        'data_nascimento': data['data_nascimento'],
        'nota_primeiro_semestre': data['nota_primeiro_semestre'],
        'nota_segundo_semestre': data['nota_segundo_semestre'],
        'media_final': (data['nota_primeiro_semestre'] + data['nota_segundo_semestre']) / 2
    }
    alunos.append(aluno)  # Adiciona o novo aluno à lista
    return aluno
