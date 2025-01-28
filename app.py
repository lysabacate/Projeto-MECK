from flask import Flask, render_template, request, flash, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db, lm
import os
from controllers.usuario import bp_usuarios
from flask_login import login_user, logout_user, login_required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abuble'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix = '/usuarios')
db.init_app(app)
lm.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def paginainicial():
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
    return render_template('pagina-dashboard.html')

@app.route('/atividades1')
@login_required
def atividades1():
    return render_template('pagina-dashboard-atividades-1.html')

@app.route('/atividades2')
@login_required
def atividades2():
    return render_template('pagina-dashboard-atividades-2.html')

@app.route('/materiais1')
@login_required
def materiais1():
    return render_template('pagina-dashboard-materiais-1.html')

@app.route('/materiais2')
@login_required
def materiais2():
    return render_template('pagina-dashboard-materiais-2.html')

@app.route('/materiais')
@login_required
def materiais():
    return render_template('pagina-materiais.html')

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

if __name__ == '__main__':
        
    app.run(debug=True)
