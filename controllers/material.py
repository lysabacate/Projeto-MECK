from flask import render_template, request, redirect, flash, session
from models.turma import Turma
from models.usuario import Usuario
from models.material import Material
from utils import db, lm
from flask import Blueprint
from flask_login import login_user, logout_user, login_required, current_user
import hashlib

bp_materiais = Blueprint("materiais", __name__, template_folder='templates')

@bp_materiais.route('/create/<tipo>', methods=['POST'])
def create(tipo):
	titulo = request.form.get('titulo_material')
	descricao = request.form.get('descricao_material')
	material = Material(tipo, titulo, descricao)
	db.session.add(material)
	db.session.commit()
	flash (f'Material {tipo} adicionado com sucesso')
	return redirect(f'/materiais/{tipo}')

@bp_materiais.route('/<tipo>')
def recovery(tipo):
    materiais = Material.query.filter_by(tipo=tipo).all()
    print(f'Materiais carregados para {tipo}:', materiais)

    if tipo == "apostila":
        template = "pagina-materiais-apostilas.html"
    elif tipo == "video":
        template = "pagina-materiais-videos.html"
    elif tipo == "adicional":
        template = "pagina-material-adicional.html"
    else:
        flash("Tipo de material inválido!", "error")
        return redirect('/dashboard')

    return render_template(template, tipo=tipo, materiais=materiais)