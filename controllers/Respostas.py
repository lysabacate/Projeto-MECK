from flask import render_template, request, redirect, flash
from models.Respostas import Respostas
from utils import db
from flask import Blueprint

bp_resposta = Blueprint("respostas", __name__, template_folder='templates')

@bp_resposta.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		resposta = request.form.get('resposta')
		id_atividade = request.form.get('id_atividade')
		resposta = Respostas(resposta, id_atividade)
		db.session.add(resposta)
		db.session.commit()
		return 'Nível definido com sucesso!'