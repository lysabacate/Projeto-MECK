"""from flask import render_template, request, redirect, flash
from models.Aluno import Aluno
from utils import db
from flask import Blueprint

bp_alunos = Blueprint("alunos", __name__, template_folder='templates')

@bp_alunos.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		nome = request.form.get('nome')
		email = request.form.get('email')
		senha = request.form.get('senha')
		csenha = request.form.get('csenha')
		aluno = Aluno(nome, email, senha, csenha)
		db.session.add(aluno)
		db.session.commit()
		return 'Dados cadastrados com sucesso!'"""