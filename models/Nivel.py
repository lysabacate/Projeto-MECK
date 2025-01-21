from utils import db

class Nivel(db.Model):
	__tablename__= "nivel"
	numeracao = db.Column(db.Integer, primary_key = True)
	conteudo = db.Column(db.String(100))

    def __init__(self, conteudo):
            self.conteudo = conteudo

	def __repr__(self):
		return "<Nível: {}".format(self.nivel.conteudo)