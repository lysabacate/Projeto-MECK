from flask import render_template, request, redirect, flash
from models.usuario import Usuario
from utils import db, lm
from flask import Blueprint
from flask_login import login_user


bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['POST'])
def create():
	matricula = request.form.get('matricula')
	nome = request.form.get('nome')
	email = request.form.get('email')
	senha = request.form.get('senha')
	csenha = request.form.get('csenha')
	perfil = request.form.get('perfil')
	usuario = Usuario(matricula, nome, email, senha, perfil)
	db.session.add(usuario)
	db.session.commit()
	return 'Dados cadastrados com sucesso!'
	
@bp_usuarios.route('/recovery')
def recovery():
	usuarios = Usuario.query.all()
	return render_template('usuarios_recovery.html', usuarios = usuarios)

@lm.user_loader
def load_user(id):
	usuario = Usuario.query.filter_by(id = id).first()
	return usuario

@bp_usuarios.route('/autenticar', methods=['POST'])
def autenticar():
	matricula = request.form.get('matricula')
	senha = request.form.get('senha')
	usuario = Usuario.query.filter_by(matricula = matricula).first()
	if usuario and (senha == usuario.senha):
		login_user(usuario)
		return redirect('/dashboard')
	else:
		flash('Dados incorretos')
		return redirect('/entrar')