from flask import render_template, request, redirect, flash
from models.Nivel import Nivel
from utils import db
from flask import Blueprint

bp_niveis = Blueprint("niveis", __name__, template_folder='templates')

@bp_niveis.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('pagina-login.html')

	if request.method=='POST':
		numeracao = request.form.get('numeracao')
		conteudo = request.form.get('conteudo')
		nivel = Nivel(numeracao, conteudo)
		db.session.add(nivel)
		db.session.commit()
		return 'Nível definido com sucesso!'