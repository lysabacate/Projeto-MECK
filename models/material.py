from utils import db

class Material(db.Model):
	__tablename__= "material"
	id = db.Column(db.Integer, primary_key = True)
	tipo = db.Column(db.String(100))
	titulo = db.Column(db.String(100))
	descricao = db.Column(db.String(100))

	def __init__(self, tipo,  titulo, descricao):
		self.tipo = tipo
		self.titulo = titulo
		self.descricao = descricao

	def __repr__(self):
   		return "<Material: {} - {}>".format(self.titulo, self.descricao)