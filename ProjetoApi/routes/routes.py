from flask import Blueprint
from controllers.professor_controller import get_professores, create_professor, get_professor
from controllers.turma_controller import get_turmas, create_turma, get_turma
from controllers.aluno_controller import get_alunos, create_aluno, update_aluno, delete_aluno

bp = Blueprint('routes', __name__)

# Professores routes
bp.route('/professores', methods=['GET'])(get_professores)
bp.route('/professores', methods=['POST'])(create_professor)
bp.route('/professores/<int:professor_id>', methods=['GET'])(get_professor)

# Turmas routes
bp.route('/turmas', methods=['GET'])(get_turmas)
bp.route('/turmas', methods=['POST'])(create_turma)
bp.route('/turmas/<int:turma_id>', methods=['GET'])(get_turma)

# Alunos routes
bp.route('/alunos', methods=['GET'])(get_alunos)
bp.route('/alunos', methods=['POST'])(create_aluno)
bp.route('/alunos/<int:aluno_id>', methods=['PUT'])(update_aluno)
bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])(delete_aluno)
