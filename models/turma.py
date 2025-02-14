from utils import db

class Turma(db.Model):
	__tablename__= "turma"
	id = db.Column(db.Integer, primary_key = True)
	codigo = db.Column(db.Integer)
	nome = db.Column(db.String(100))
	nivel = db.Column(db.Integer)
	descricao = db.Column(db.String(300))

	alunos = db.relationship('Usuario', back_populates='turma', lazy=True)

	def __init__(self, codigo, nome, nivel, descricao):
		self.codigo = codigo
		self.nome = nome
		self.nivel = nivel
		self.descricao = descricao

	def __repr__(self):
   		return "<Turma: {} - {}>".format(self.nome, self.nivel)