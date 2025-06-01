from src.Infrastructure.Model.produtos import Produtos
from src.config.config import db

def validar_produto_payload(data):
    erros = {}

    campos_obrigatorios = ['id_vendedor', 'quantidade', 'valor', 'status']
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

    return erros


def validar_filtros_listagem(args):
    erros = {}

    id_vendedor = args.get('id_vendedor')
    status = args.get('status')

    if id_vendedor is not None:
        try:
            int(id_vendedor)
        except ValueError:
            erros['id_vendedor'] = 'Deve ser um número inteiro'

    if status is not None and not isinstance(status, str):
        erros['status'] = 'Status deve ser uma string'

    return erros


def validar_id_produto(produto_id):
    erros = {}

    if not isinstance(produto_id, int) or produto_id <= 0:
        erros['id'] = 'ID do produto deve ser um número inteiro positivo'

    return erros

def mostrar_produto_por_id(id_vendedor, produto_id):
    erros = validar_id_produto(produto_id)
    if erros:
        return None, {'message': 'ID inválido', 'errors': erros}, 400

    produto = db.session.query(Produtos).filter_by(id=produto_id, id_vendedor=id_vendedor).first()

    if not produto:
        return None, {'message': 'Produto não encontrado'}, 404

    return produto.to_dict(), None, 200