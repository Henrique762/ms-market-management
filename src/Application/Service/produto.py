from src.Infrastructure.Model.produtos import Produtos, alterar_produto
from src.config.config import db

def validar_produto(data):
    produto_id = data['id_produto']
    produto = db.session.query(Produtos).filter_by(id=produto_id).first()

    if not produto:
        return {'message': 'Produto não encontrado', "status_code": 400}

    return alterar_produto(data)    