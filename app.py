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

@app.route('/materiais')
def materiais():
    return render_template('pagina-materiais.html')

if __name__ == '__main__':
    app.run()
