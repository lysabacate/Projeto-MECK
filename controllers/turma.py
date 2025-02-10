from flask import render_template, request, redirect, flash, session
from models.turma import Turma
from utils import db, lm
from flask import Blueprint
from flask_login import login_user, logout_user, login_required
import hashlib

bp_turmas = Blueprint("turmas", __name__, template_folder='templates')

@bp_turmas.route('/create', methods=['POST'])
def create():
	codigo = request.form.get('codigo_turma')
	nome = request.form.get('nome_turma')
	nivel = request.form.get('nivel_turma')
	descricao= request.form.get('descricao')
	turma = Turma(codigo, nome, nivel, descricao)
	db.session.add(turma)
	db.session.commit()
	flash ('Turma criada com sucesso')
	return redirect('/turmas/recovery')


@bp_turmas.route('/recovery')
def recovery():
	turmas = Turma.query.all()
	session['turmas_ids'] = [turma.id for turma in turmas]
	return redirect('/listar_turmas')