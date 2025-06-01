from src.Infrastructure.Model import Produtos


def editar_produto(produto_id, dados):
    produto = Produtos.query.get(produto_id)
    if not produto:
        return {'message': 'Produto não encontrado', 'status_code': 404}

    try:
        if 'id_vendedor' in dados:
            produto.id_vendedor = dados['id_vendedor']
        if 'quantidade' in dados:
            produto.quantidade = dados['quantidade']
        if 'valor' in dados:
            produto.valor = dados['valor']
        if 'status' in dados:
            produto.status = dados['status']

        db.session.commit()
        return {'message': 'Produto atualizado com sucesso', 'status_code': 200}
    
    except Exception as e:
        db.session.rollback()
        return {'message': f'Erro ao atualizar produto: {str(e)}', 'status_code': 500}


def listar_produtos(filtros):
    query = Produtos.query

    if 'id_vendedor' in filtros and filtros['id_vendedor'] is not None:
        query = query.filter_by(id_vendedor=filtros['id_vendedor'])

    if 'status' in filtros and filtros['status']:
        query = query.filter_by(status=filtros['status'])

    produtos = query.all()
    return [
        {
            'id': p.id,
            'id_vendedor': p.id_vendedor,
            'quantidade': p.quantidade,
            'valor': p.valor,
            'status': p.status
        }
        for p in produtos
    ]