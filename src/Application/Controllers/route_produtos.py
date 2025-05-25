from flask import Blueprint, request, jsonify
from src.Infrastructure.Model.produtos import Produtos
from src.config.config import db
import os
from werkzeug.utils import secure_filename
import time

produtos_bp = Blueprint('produtos', __name__)

# Configuração para upload de imagens
UPLOAD_FOLDER = 'uploads/produtos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Criar pasta de uploads se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@produtos_bp.route('/produtos', methods=['POST'])
def cadastrar_produto():
    try:
        # Verificar se tem arquivo de imagem
        imagem = None
        if 'imagem' in request.files:
            file = request.files['imagem']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Adicionar timestamp ao nome do arquivo para evitar duplicatas
                filename = f"{int(time.time())}_{filename}"
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                imagem = filepath

        # Pegar os outros dados do formulário
        dados = request.form
        
        novo_produto = Produtos(
            nome=dados['nome'],
            preco=float(dados['preco']),
            quantidade=int(dados['quantidade']),
            status='Ativo',
            imagem=imagem
        )
        
        db.session.add(novo_produto)
        db.session.commit()
        
        return jsonify({
            'message': 'Produto cadastrado com sucesso',
            'produto': {
                'id': novo_produto.id,
                'id_vendedor': novo_produto.id_vendedor,
                'nome': novo_produto.nome,
                'quantidade': novo_produto.quantidade,
                'valor': novo_produto.valor,
                'status': novo_produto.status,
                'imagem': novo_produto.imagem
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
        
        # Se existir uma imagem, deletar o arquivo
        if produto.imagem and os.path.exists(produto.imagem):
            os.remove(produto.imagem)
        
        db.session.delete(produto)
        db.session.commit()
        
        return jsonify({'message': 'Produto deletado com sucesso'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400 