from utils import db

class Turma(db.Model):
	__tablename__= "turma"
	id = db.Column(db.Integer, primary_key = True)
	codigo = db.Column(db.String(100))
	nome = db.Column(db.String(100))
	nivel = db.Column(db.Integer)
	professor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

	professor = db.relationship('Usuario', back_populates='turma')
	alunos = db.relationship('Aluno', back_populates='turma', cascade="all, delete-orphan")

	def __init__(self, codigo, nome, nivel, professor_id):
		self.codigo = codigo
		self.nome = nome
		self.nivel = nivel
		self.professor_id = professor_id

	def __repr__(self):
   		return "<Turma: {} - {}>".format(self.nome, self.nivel)