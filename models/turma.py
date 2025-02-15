from utils import db

class Turma(db.Model):
	__tablename__= "turma"
	id = db.Column(db.Integer, primary_key = True)
	codigo = db.Column(db.String(100))
	nome = db.Column(db.String(100))
	nivel = db.Column(db.Integer)

	alunos = db.relationship('Usuario', back_populates='turma', lazy=True)

	def __init__(self, codigo, nome, nivel,):
		self.codigo = codigo
		self.nome = nome
		self.nivel = nivel

	def __repr__(self):
   		return "<Turma: {} - {}>".format(self.nome, self.nivel)