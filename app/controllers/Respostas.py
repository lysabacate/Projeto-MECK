from flask import render_template, request, redirect, flash
from models.Respostas import Respostas
from utils import db
from flask import Blueprint

bp_respostas = Blueprint("respostas", __name__, template_folder='templates')

@bp_respostas.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		resposta = request.form.get('respostas')
		id_atividade = request.form.get('id_atividade')
		respostas = Respostas(resposta, id_atividade)
		db.session.add(respostas)
		db.session.commit()
		return 'Dados cadastrados com sucesso!'