from src.config.config import db

class Produtos(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey('vendedores.id', ondelete="CASCADE"), nullable=False)
    quantidade= db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False, default='Inativo')

    def to_dict(self):
        return {
            "id": self.id,
            "id_vendedor": self.id_vendedor,
            "quantidade": self.quantidade,
            "valor": self.valor,
            "status": self.status
        }

def listar_produto(id):
    produtos = db.session.query(Produtos).filter_by(id_vendedor=id).all()
    resultado = [a.to_dict() for a in produtos]

    return resultado


def alterar_quantidade(id, quant):
    produto = db.session.query(Produtos).filter_by(id=id).first()
    
    produto.quantidade = quant

    db.session.commit()

    produto = db.session.query(Produtos).filter_by(id=id).first()

    return produto.quantidade

def alterar_produto(data):
    produto_id = data['id_produto']
    produto = Produtos.query.get(produto_id)
    try:
        produto.id_vendedor = data['id_vendedor']
        produto.quantidade = data['quantidade']
        produto.valor = float(data['valor'])
        produto.status = data['status']

        db.session.commit()
        return {'message': 'Produto atualizado com sucesso', "status_code": 200}

    except Exception as e:
        db.session.rollback()
        return {'message': f'Erro ao atualizar produto: {str(e)}', "status_code": 500}  