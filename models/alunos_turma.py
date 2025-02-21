from utils import db

class Aluno(db.Model):
	__tablename__= "alunos"
	id = db.Column(db.Integer, primary_key = True)
	aluno_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
	turma_id =  db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
	
	aluno = db.relationship('Usuario', back_populates='alunos')
	turma = db.relationship('Turma', back_populates='alunos')
	
	def __init__(self, aluno_id, turma_id):
		self.aluno_id = aluno_id
		self.turma_id = turma_id

	def __repr__(self):
   		return "<Aluno: {} - {}>".format(self.aluno_id, self.turma_id)