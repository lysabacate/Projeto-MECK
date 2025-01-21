from utils import db

#Tabela usada no exemplo da prof:
class Classroom(db.Model):
	__tablename__= "classroom"
	id = db.Column(db.Integer, primary_key = True)
	codigo_prof = db.Column(db.Integer, db.ForeignKey('professor.codigo')
    numeracao_nv = db.Column(db.Integer, db.ForeignKey('nivel.numeracao')
	turma = db.Column(db.String(100))
	nome = db.Column(db.String(100))
							

    def __init__(self, nome, email, senha):
    professor = db.relationship('professor', foreign_keys=codigo_prof)
    nivel = db.relationship('nivel', foreign_keys=numeracao_nv)

    professor = db.relationship('professor', foreign_keys=codigo_prof)
    nivel = db.relationship('nivel', foreign_keys=numeracao_nv)

    def __init__(self, nome, email, senha):
        self.codigo_prof = codigo_prof
        self.numeracao_nv = numeracao_nv
    
    def __repr__(self):
        return "<Sala de Aula: {} - {}>".format(self.codigo_prof.nome, self.nivel.numeracao)