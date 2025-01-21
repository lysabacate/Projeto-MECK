from flask import render_template, request, redirect, flash
from models.Material import Material
from utils import db
from flask import Blueprint

bp_materiais = Blueprint("materiais", __name__, template_folder='templates')

@bp_materiais.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		nome = request.form.get('nome')
		habilidade_eng = request.form.get('habilidade_eng')
		codigo_prof = request.form.get('codigo_prof')
		numeracao_nv = request.form.get('numeracao_nv')
		tipo = request.form.get('tipo')
		material = Material(nome, habilidade_eng, codigo_prof, numeracao_nv, tipo)
		db.session.add(material)
		db.session.commit()
		return 'Material postado com sucesso!'