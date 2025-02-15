from utils import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
	__tablename__= "usuario"
	id = db.Column(db.Integer, primary_key = True)
	matricula = db.Column(db.Integer)
	nome = db.Column(db.String(100))
	senha = db.Column(db.String(100))
	admin = db.Column(db.Boolean)
	turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=True)

	turma = db.relationship('Turma', back_populates='alunos')

	def __init__(self, matricula, nome, senha, admin, turma_id = None):
		self.matricula = matricula
		self.nome = nome
		self.senha = senha
		self.admin = admin
		self.turma_id = turma_id

	def __repr__(self):
   		return "<Usuario: {} - {}>".format(self.nome, self.admin)