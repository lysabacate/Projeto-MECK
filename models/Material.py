from utils import db

class Material(db.Model):
    __tablename__ = "material"
    id = db.Column(db.Integer, primary_key = True)
    codigo_prof = db.Column(db.Integer, db.ForeignKey('professor.codigo'))
    numeracao_nv = db.Column(db.Integer, db.ForeignKey('nivel.numeracao'))
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(100))

    professor = db.relationship('Professor', foreign_keys=[codigo_prof])
    nivel = db.relationship('Nivel', foreign_keys=[numeracao_nv])

    def __init__(self, codigo_prof, numeracao_nv, tipo):
        self.codigo_prof = codigo_prof
        self.numeracao_nv = numeracao_nv
        self.tipo = tipo

    def __repr__(self):
        return "<Material: {} - {} - {}>".format(self.professor.nome, self.nivel.numeracao, self.tipo)
