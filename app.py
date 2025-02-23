from flask import Flask, render_template, request, flash, redirect, Blueprint, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db, lm
import os
from controllers.usuario import bp_usuarios
from controllers.turma import bp_turmas
from controllers.material import bp_materiais
from controllers.alunos_turma import bp_alunos
from flask_login import login_user, logout_user, login_required, current_user
from models.turma import Turma
from models.material import Material
from models.alunos_turma import Aluno

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SECRET_KEY'] = 'abuble'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix = '/usuarios')
app.register_blueprint(bp_turmas, url_prefix = '/turmas')
app.register_blueprint(bp_materiais, url_prefix = '/materiais')
app.register_blueprint(bp_alunos, url_prefix = '/alunos')
db.init_app(app)
lm.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def paginainicial():
    existe_turma = db.session.query(Turma.id).first() is not None
    alunos = {aluno.aluno_id: aluno.turma_id for aluno in Aluno.query.with_entities(Aluno.aluno_id, Aluno.turma_id).all()}

    if current_user.is_authenticated:
        if current_user.admin and existe_turma:
            return redirect('/listar_turmas')

        if current_user.id in alunos:
            turma_id = alunos[current_user.id]  
            if turma_id:
                return redirect(f'/turma_aluno/{turma_id}')

        return redirect('/dashboard')

    return render_template('pagina-inicial.html')

@app.route('/registrar')
def registrar():
    return render_template('pagina-registrar-conta.html')

@app.route('/redefinir_senha')
def redefinir_senha():
    return render_template('pagina-redefinir-senha.html')

@app.route('/entrar')
def entrar():
    return render_template('pagina-login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated and current_user.admin:
        return render_template('pagina-dashboard-prof.html')
    
    elif current_user.is_authenticated and not current_user.admin:
        return render_template('pagina-dashboard-aluno.html')

@app.route('/atividades')
@login_required
def atividades():
    return render_template('pagina-dashboard-atividades.html')

@app.route('/materiais')
@login_required
def materiais():
    return render_template('pagina-dashboard-materiais.html')

@app.route('/links')
@login_required
def links():
    return render_template('pagina-links.html')

@app.route('/listaatvs')
@login_required
def listaatvs():
    habilidades = [
        {'nome':'Nome_Atv', 'descricao':'Atividade complexa e bem feita'},
        {'nome':'Nome_Atv2', 'descricao':'Atividade complexa e bem feita legal'},
        {'nome':'Nome_Atv3', 'descricao':'Atividade complexa e bem feita legal'},
        {'nome':'Nome_Atv4', 'descricao':'Atividade complexa e bem feita legal'},
        {'nome':'Nome_Atv5', 'descricao':'Atividade complexa e bem feita legal'},
        {'nome':'Nome_Atv6', 'descricao':'Atividade complexa e bem feita legal'}
    ]
    return render_template('pagina-lista-atividades.html', habilidades = habilidades)


@app.route('/turma_aluno/<int:id>')
@login_required
def turma_aluno(id):
    turma = Turma.query.get(id)
    return render_template('pagina-turma-aluno.html', turma=turma)


@app.route('/criar_turma')
@login_required
def criar_turma():
    return render_template('pagina-criar-turma.html')

@app.route('/listar_turmas')
@login_required
def listar_turma():
    turmas = Turma.query.all()
    return render_template('pagina-listar-turmas.html', turmas = turmas)

@app.route('/add_material/<tipo>')
@login_required
def add_material(tipo):
    return render_template('pagina-add-material.html', tipo = tipo)

@app.route('/listar_materiais/<tipo>')
def listar_materiais(tipo):
    materiais = Material.query.filter_by(tipo=tipo).all()
    
    if not materiais:
        flash(f'Nenhum material encontrado para {tipo}', )

    return render_template('listar_materiais.html', tipo=tipo, materiais=materiais)


if __name__ == '__main__':
    app.run(debug=True)
