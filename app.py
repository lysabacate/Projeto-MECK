from flask import Flask, render_template, request, flash, redirect, Blueprint, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db, lm
import os
from controllers.usuario import bp_usuarios
from controllers.turma import bp_turmas
from flask_login import login_user, logout_user, login_required, current_user
from models.turma import Turma

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SECRET_KEY'] = 'abuble'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix = '/usuarios')
app.register_blueprint(bp_turmas, url_prefix = '/turmas')
db.init_app(app)
lm.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def paginainicial():
    if current_user.is_authenticated and current_user.admin:
        return render_template('pagina-dashboard-prof.html')
    
    elif current_user.is_authenticated and not current_user.admin:
        return render_template('pagina-dashboard-aluno.html')
    
    else:
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


@app.route('/materiais_videos')
@login_required
def materiais_videos():
    videos = [
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material2'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material3'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material4'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material5'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material6'}
    ]
    return render_template('pagina-materiais-videos.html', videos = videos)

@app.route('/materiais_apostilas')
@login_required
def materiais_apostilas():
    apostilas = [
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material2'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material3'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material4'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material5'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material6'}
    ]
    return render_template('pagina-materiais-apostilas.html', apostilas = apostilas)

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

@app.route('/material_adicional')
@login_required
def materiais_adicional():
    adicional = [
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material2'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material3'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material4'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material5'},
        {'imagem': 'static/img/imagem-listening.svg','nome':'Nome_Material6'}
    ]
    return render_template('pagina-material-adicional.html', adicional = adicional)

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
    turma_ids = session.get('turmas_ids', [])
    turmas = Turma.query.filter(Turma.id.in_(turma_ids)).all()
    return render_template('pagina-listar-turmas.html', turmas = turmas)

if __name__ == '__main__':
        
    app.run(debug=True)
