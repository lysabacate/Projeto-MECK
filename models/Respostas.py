from utils import db

#Tabela usada no exemplo da prof:
class Repostas(db.Model):
	__tablename__= "respostas"
	resposta = db.Column(db.Integer, primary_key = True)
	id_atividade = db.Column(db.Integer, db.ForeignKey('atividade.id'))

    def __init__(self, usuario_matr):
        self.id_atividade = id_atividade

	def __repr__(self):
		return "<Respostas: {} - {}".format(self.atividade.id, self.atividade.nome)