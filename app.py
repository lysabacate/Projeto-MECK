from flask import Flask, render_template, request, flash, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)

class Usuario(db.Model):
    __tablename__= "usuario"
    matricula = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

@app.route('/')
def index():
    return "Olá, Mundo"

if __name__ == '__main__':
    with app.app_context():
        db.create_all
        
    app.run(debug=True)
