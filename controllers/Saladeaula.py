from flask import render_template, request, redirect, flash
from models.Saladeaula import Saladeaula
from utils import db
from flask import Blueprint

bp_saladeaula = Blueprint("saladeaula", __name__, template_folder='templates')

@bp_saladeaula.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		numeracao_nv = request.form.get('numeracao_nv')
		turma = request.form.get('turma')
		nome = request.form.get('nome')
		saladeaula = Saladeaula(numeracao_nv, turma, nome)
		db.session.add(saladeaula)
		db.session.commit()
		return 'Dados cadastrados com sucesso!'