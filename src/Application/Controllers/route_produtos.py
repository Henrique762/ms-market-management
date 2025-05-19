from flask import Blueprint, request, jsonify
from src.Infrastructure.Model.produtos import Produtos
from src.config.config import db

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/produtos', methods=['POST'])
def cadastrar_produto():
    try:
        dados = request.get_json()
        
        novo_produto = Produtos(
            id_vendedor=dados['id_vendedor'],
            quantidade=dados['quantidade'],
            valor=dados['valor'],
            status='Ativo'
        )
        
        db.session.add(novo_produto)
        db.session.commit()
        
        return jsonify({
            'message': 'Produto cadastrado com sucesso',
            'produto': {
                'id': novo_produto.id,
                'id_vendedor': novo_produto.id_vendedor,
                'quantidade': novo_produto.quantidade,
                'valor': novo_produto.valor,
                'status': novo_produto.status
            }
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@produtos_bp.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        produto = Produtos.query.get(id)
        
        if not produto:
            return jsonify({'message': 'Produto não encontrado'}), 404
        
        db.session.delete(produto)
        db.session.commit()
        
        return jsonify({'message': 'Produto deletado com sucesso'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400 