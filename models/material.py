from utils import db

class Material(db.Model):
	__tablename__= "material"
	id = db.Column(db.Integer, primary_key = True)
	tipo = db.Column(db.String(100))
	titulo = db.Column(db.String(100))
	descricao = db.Column(db.String(100))
	turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

	def __init__(self, tipo,  titulo, descricao, turma_id):
		self.tipo = tipo
		self.titulo = titulo
		self.descricao = descricao
		self.turma_id = turma_id

	def __repr__(self):
   		return "<Material: {} - {}>".format(self.titulo, self.descricao)