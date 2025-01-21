"""from flask import render_template, request, redirect, flash
from models.Atividade import Atividade
from utils import db
from flask import Blueprint

bp_atividades = Blueprint("atividades", __name__, template_folder='templates')

@bp_atividades.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		nome = request.form.get('nome')
		habilidade_eng = request.form.get('habilidade_eng')
		codigo_prof = request.form.get('codigo_prof')
		numeracao_nv = request.form.get('numeracao_nv')
		questoes = request.form.get('questoes')
		atividade = Atividade(nome, habilidade_eng, codigo_prof, numeracao_nv, questoes)
		db.session.add(atividade)
		db.session.commit()
		return 'Atividade postada com sucesso!'"""