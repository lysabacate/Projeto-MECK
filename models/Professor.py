"""from utils import db

#Tabela usada no exemplo da prof:
class Professor(db.Model):
	__tablename__= "professor"
	codigo = db.Column(db.Integer, primary_key = True)
	usuario_matr = db.Column(db.Integer, db.ForeignKey('usuario.matricula')

	usuario = db.relationship('usuario', foreign_keys=usuario_matr)

	def __init__(self, usuario_matr):
    	self.usuario_matr = usuario_matr

	def __repr__(self):
		return "<Professor: {}>".format(self.usuario.nome)
"""
