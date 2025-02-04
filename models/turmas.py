from utils import db
from flask_login import UserMixin


#Tabela usada no exemplo da prof:
class Usuario(db.Model, UserMixin):
	__tablename__= "usuario"
	id = db.Column(db.Integer, primary_key = True)
    imagem_url = db.Column(db.String(255))
    codigo = db.Column(db.Integer)
	nome = db.Column(db.String(100))
	nivel = db.Column(db.Integer)
	descricao = db.Column(db.String(300))

	def __init__(self, matricula, nome, email, senha, admin):
		self.imagem_url = imagem_url
		self.codigo = codigo
		self.nome = nome
		self.nivel = nivel
		self.descricao = descricao

    def __repr__(self):
   		return "<Turma: {} - {}>".format(self.nome, self.nivel)