from flask import render_template, request, redirect, flash
from models.usuario import Usuario
from utils import db, lm
from flask import Blueprint
from flask_login import login_user, logout_user, login_required
import hashlib

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['POST'])
def create():
	matricula = request.form.get('matricula')
	nome = request.form.get('nome')
	senha = request.form.get('senha')
	senha_hash = hashlib.sha256(senha.encode())
	csenha = request.form.get('csenha')
	admin = request.form.get('admin')
	if senha == csenha:
		usuario = Usuario(matricula, nome, senha_hash.hexdigest(), eval(admin))
		db.session.add(usuario)
		db.session.commit()
		flash ('Dados cadastrados com sucesso')
		return redirect('/entrar')
	else:
		flash ('Erro. Senhas não correspondentes')
		return redirect('/registrar')
	
@bp_usuarios.route('/recovery')
def recovery():
	usuarios = Usuario.query.all()
	return render_template('usuarios_recovery.html', usuarios = usuarios)

@bp_usuarios.route("/teste_delete")
def teste_delete():		
	u = Usuario.query.get(1)
	db.session.delete(u)
	db.session.commit()
	return 'Dados excluídos com sucesso'

@bp_usuarios.route("/teste_update")
def teste_update():
	u = Usuario.query.get(2)
	u.nome = "Alba L."
	db.session.add(u)
	db.session.commit()
	return 'Dados atualizados com sucesso'

@lm.user_loader
def load_user(id):
	usuario = Usuario.query.filter_by(id = id).first()
	return usuario

@bp_usuarios.route('/autenticar', methods=['POST'])
def autenticar():
	matricula = request.form.get('matricula')
	senha = request.form.get('senha')
	usuario = Usuario.query.filter_by(matricula = matricula).first()
	if usuario and (hashlib.sha256(senha.encode()).hexdigest() == usuario.senha):
		login_user(usuario)
		return redirect('/dashboard')
	else:
		flash('Dados incorretos')
		return redirect('/entrar')

@bp_usuarios.route('/logoff')
def logoff():
	logout_user()
	return redirect('/')