"""from flask import render_template, request, redirect, flash
from models.usuario import Usuario
from utils import db, lm
from flask import Blueprint
from flask_login import login_user, logout_user, login_required
import hashlib

bp_usuarios = Blueprint("turmas", __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['POST'])
def create():
    codigo = request.form.get('codigo_turma')
	nome = request.form.get('nome_turma')
	nivel = request.form.get('nivel_turma')
	descricao= request.form.get('descricao')
	turma = Usuario(imagem_url, codigo, nome, nivel, descricao)
	db.session.add(turma)
	db.session.commit()
	#flash ('Turma criada com sucesso')
    #return render_template('')
    return 'Turma criada com sucesso'"""



