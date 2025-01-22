from flask import Flask, render_template, request, flash, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db
import os

app = Flask(__name__)
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

migrate = Migrate(app, db)

@app.route('/')
def paginainicial():
    return render_template('pagina-inicial.html')

@app.route('/registre-se')
def registrar():
    return render_template('pagina-registrar-conta.html')

@app.route('/redefinir_senha')
def redefinir_senha():
    return render_template('pagina-redefinir-senha.html')

@app.route('/entrar')
def entrar():
    return render_template('pagina-login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    matricula = request.form["matricula"]
    senha = request.form["senha"]
    if matricula != '123' or senha != 'senha123':
        flash("Login ou senha incorretos")
        return redirect("/entrar")
    else:
        return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('pagina-dashboard.html')

@app.route('/atividades1')
def atividades1():
    return render_template('pagina-dashboard-atividades-1.html')

@app.route('/atividades2')
def atividades2():
    return render_template('pagina-dashboard-atividades-2.html')

@app.route('/materiais1')
def materiais1():
    return render_template('pagina-dashboard-materiais-1.html')

@app.route('/materiais2')
def materiais2():
    return render_template('pagina-dashboard-materiais-2.html')

@app.route('/materiais')
def materiais():
    return render_template('pagina-materiais.html')

@app.route('/listaatvs')
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
    with app.app_context():
        db.create_all
        
    app.run(debug=True)
