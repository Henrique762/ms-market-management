from src.Infrastructure.Model.produtos import Produtos, alterar_quantidade
from src.Infrastructure.Model.vendas import adicionar_venda
from src.config.config import db

def valid_infos(form):
    id_produto = form['id_produto']
    produto = Produtos.query.filter_by(id=id_produto).first()
    print("Tá Parando AQUI")
    ### Validacao Existencia Produto
    if not produto:
        raise ValueError('Produto Inexistente')
    
    
    ### Validacao Quantidade em estoque
    
    quantidade = form['quantidade']
    quantidade_disponivel = produto.quantidade

    restante_estoque = quantidade_disponivel - quantidade

    if restante_estoque < 0:
        raise ValueError('Quantidade Indisponivel no Estoque', quantidade_disponivel)

    ### Valor Total Compra

    valor = produto.valor
    preco_total = valor * quantidade

    if adicionar_venda(form, valor, preco_total) == True:

        estoque = alterar_quantidade(id_produto, restante_estoque)

    return estoque
    




        

