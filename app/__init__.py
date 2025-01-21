"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
    db.init_app(app)

    class Usuario(db.Model):
        __tablename__= "usuario"
        matricula = db.Column(db.Integer, primary_key = True)
        nome = db.Column(db.String(100))
        email = db.Column(db.String(100))
        senha = db.Column(db.String(100))

        def __init__(self, nome, email, senha):
                self.nome = nome
                self.email = email
                self.senha = senha
            
        def __repr__(self):
            return "<Usuario {}>".format(self.nome)

    from app import routes, models

    if __name__ == '__main__':
        with app.app_context():
            from app.models import models
            app.register_blueprint(models)
        app.run(debug=True)"""