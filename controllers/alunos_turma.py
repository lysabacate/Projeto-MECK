from flask import request, redirect, flash, session
from models.alunos_turma import Aluno
from models.turma import Turma
from models.usuario import Usuario
from utils import db
from flask import Blueprint
from flask_login import current_user

bp_alunos = Blueprint("alunos", __name__, template_folder='templates')

@bp_alunos.route('/create', methods=['POST'])
def create():
    codigo_turma = request.form.get('codigo')
    turma = Turma.query.filter_by(codigo=codigo_turma).first()

    if not turma:
        flash('Código de turma inexistente. Tente novamente', 'error')
        return redirect('/dashboard')

    aluno_id = current_user.id

    aluno = Aluno.query.filter_by(id=aluno_id).first()

    if aluno:
        if aluno.turma_id:
            flash("Você já está em uma turma, saia antes de ingressar em outra", 'error')
            return redirect('/dashboard')
        
        else:
            aluno.turma_id = turma.id
            
    else:
        aluno = Aluno(aluno_id, turma_id=turma.id)
        db.session.add(aluno)

    db.session.commit()
    flash(f'Você entrou na turma {turma.nome}', 'success')
    return redirect(f'/turma_aluno/{turma.id}')