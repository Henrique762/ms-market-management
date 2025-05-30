from src.config.config import db

class Produtos(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey('vendedores.id', ondelete="CASCADE"), nullable=False)
    quantidade= db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False, default='Inativo')


def alterar_quantidade(id, quant):
    produto = db.session.query(Produtos).filter_by(id=id).first()
    
    produto.quantidade = quant

    db.session.commit()

    produto = db.session.query(Produtos).filter_by(id=id).first()

    return produto.quantidade