from utils import db

#Tabela usada no exemplo da prof:
class Atividade(db.Model):
	__tablename__= "atividade"
	id = db.Column(db.Integer, primary_key = True)
	codigo_prof = db.Column(db.Integer, db.ForeignKey('professor.codigo')
    numeracao_nv = db.Column(db.Integer, db.ForeignKey('nivel.numeracao')
    nome = db.Column(db.String(100))
    questoes = db.Column(db.String(100))
    habilidade_eng = db.Column(db.String(100))
	#respostas = db.Column(coloca oq aqui plmdds??)

    def __init__(self, nome, email, senha):
        self.codigo_prof = codigo_prof
        self.numeracao_nv = numeracao_nv
        self.questoes = questoes
        self.habilidade_eng = habilidade_eng
    
    def __repr__(self):
        return "<Atividade: {} - {} - {}>".format(self.codigo_prof.nome, self.nivel.numeracao, self.habilidade_eng)