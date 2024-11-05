from flask import Flask, render_template, request, flash, redirect
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abuble'

@app.route('/')
def paginainicial():
    return render_template('pagina-inicial.html')



@app.route('/registre-se')
def registrar():
    return render_template('pagina-registrar-conta.html')

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
    app.run()
