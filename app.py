from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/aaa')
def paginainicial():
    return render_template('pagina-inicial.html')

@app.route('/')
def entrar():
    return render_template('pagina-login.html')

@app.route('/registre-se')
def registrar():
    return render_template('pagina-registrar-conta.html')

@app.route('/dashboard')
def dashboard():
    return render_template('pagina-dashboard.html')


if __name__ == '__main__':
    app.run()
