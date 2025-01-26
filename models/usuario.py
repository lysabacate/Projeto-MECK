from utils import db
from flask_login import UserMixin


#Tabela usada no exemplo da prof:
class Usuario(db.Model, UserMixin):
	__tablename__= "usuario"
	id = db.Column(db.Integer, primary_key = True)
	matricula = db.Column(db.Integer)
	nome = db.Column(db.String(100))
	email = db.Column(db.String(100))
	senha = db.Column(db.String(100))
	perfil = db.Column(db.Integer)

	def __init__(self, matricula, nome, email, senha, perfil):
		self.matricula = matricula
		self.nome = nome
		self.email = email
		self.senha = senha
		self.perfil = perfil
    
	def __repr__(self):
   		return "<Usuario {} - {}>".format(self.nome, self.perfil)