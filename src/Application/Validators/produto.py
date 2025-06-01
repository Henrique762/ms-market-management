from src.Infrastructure.Model.produtos import Produtos
from src.Application.Service.produto import validar_produto
from src.config.config import db

def validar_id_produto(produto_id):
    erros = {}

    if not isinstance(produto_id, int) or produto_id <= 0:
        erros['id'] = 'ID do produto deve ser um número inteiro positivo'

    return erros

def validar_produtos(data):
    campos_obrigatorios = ['quantidade', 'valor', 'status']
    erros = {}

    for campo in campos_obrigatorios:
        if campo not in data:
            erros[campo] = 'Campo obrigatório'

    if 'quantidade' in data and not isinstance(data['quantidade'], int):
        erros['quantidade'] = 'Deve ser um número inteiro'

    if 'valor' in data:
        try:
            float(data['valor'])
        except (ValueError, TypeError):
            erros['valor'] = 'Deve ser um número válido'

    if erros:
        return {'message': 'Dados inválidos', 'errors': erros, "status_code": 400}

def edit_produto(data):
    validar_produtos(data)
    result = validar_produto(data)

    return result

def mostrar_produto_por_id(id_vendedor, produto_id):
    erros = validar_id_produto(produto_id)
    if erros:
        return None, {'message': 'ID inválido', 'errors': erros}, 400

    produto = db.session.query(Produtos).filter_by(id=produto_id, id_vendedor=id_vendedor).first()

    if not produto:
        return None, {'message': 'Produto não encontrado'}, 404

    return produto.to_dict(), None, 200    

def listar_produto(id):
    produtos = db.session.query(Produtos).filter_by(id_vendedor=id).all()
    resultado = [a.to_dict() for a in produtos]

    return resultado