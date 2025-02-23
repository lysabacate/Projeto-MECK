from flask import request, redirect, flash, session
from models.turma import Turma
from models.usuario import Usuario
from utils import db
from flask import Blueprint
from flask_login import current_user


bp_turmas = Blueprint("turmas", __name__, template_folder='templates')

@bp_turmas.route('/create', methods=['POST'])
def create():
	codigo = request.form.get('codigo_turma')
	nome = request.form.get('nome_turma')
	nivel = request.form.get('nivel_turma')
	professor_id = current_user.id
	print(f"Professor ID: {professor_id}")
	turma = Turma(codigo, nome, nivel, professor_id = professor_id)
	db.session.add(turma)
	db.session.commit()
	flash ('Turma criada com sucesso')
	return redirect('/turmas/recovery')


@bp_turmas.route('/recovery')
def recovery():
	return redirect('/listar_turmas')

@bp_turmas.route('/delete/<int:id>', methods=['POST'])
def delete(id):
	turma = Turma.query.get(id)
	if turma is None:
		flash('Turma não encontrada', 'error')
		return redirect('/listar_turmas')

	db.session.delete(turma)
	db.session.commit()

	flash('Turma excluída com sucesso', 'success')
	return redirect('/listar_turmas')


@bp_turmas.route('/update/<int:id>', methods=['POST'])
def update(id):
    turma = Turma.query.get(id)

    if turma:
        turma.codigo = request.form.get('codigo_turma')
        turma.nome = request.form.get('nome_turma')
        turma.nivel = request.form.get('nivel_turma')

        db.session.commit()

        flash('Turma atualizada com sucesso', 'success')
    else:
        flash('Turma não encontrada', 'error')

    return redirect('/listar_turmas')

    
'''@bp_turmas.route('/ingressar-turma', methods=['POST'])
def ingressar_turma():
	codigo_turma = request.form.get('codigo')
	turma = Turma.query.filter_by(codigo=codigo_turma).first()

	if not turma:
		flash('Código de turma inexistente. Tente novemente', 'error')
		return redirect('/dashboard')
	
	aluno = Usuario.query.get(current_user.id)
	if aluno.turma_id:
		flash("Você já está em uma turma, saia antes de ingressar em outra")
		return redirect('/dashboard')

	aluno.turma_id = turma.id
	db.session.commit()
	flash(f'Você entrou na turma {turma.nome}')
	return redirect(f'/turma_aluno/{turma.id}')'''