from utils import db

#Tabela usada no exemplo da prof:
class Classroom(db.Model):
	__tablename__= "classroom"
	id = db.Column(db.Integer, primary_key = True)
	codigo_prof = db.Column(db.Integer, db.ForeignKey('professor.codigo')
    numeracao_nv = db.Column(db.Integer, db.ForeignKey('nivel.numeracao')

def __init__(self, nome, email, senha):
        self.codigo_prof = codigo_prof
        self.numeracao_nv = numeracao_nv
    
def __repr__(self):
    return "<Sala de Aula: {} - {}>".format(self.codigo_prof.nome, self.nivel.numeracao)