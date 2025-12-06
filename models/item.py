from extensions import db

class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    tipo = db.Column(db.String(50))

    dono_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    dono = db.relationship("Usuario", backref="itens")
