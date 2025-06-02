from flask import Blueprint, Flask,request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.config.config import app
from src.config.config import db
from src.Application.Validators.cadastro import create_user
from src.Application.Validators.vendas import create_venda
from src.Application.Validators.wpp import ativacao_cod
from src.Application.Controllers.route_produtos import produtos_bp
from src.Infrastructure.Model.produtos import Produtos
from werkzeug.utils import secure_filename
import os
import time

cadastro_blueprint = Blueprint('cadastro', __name__, url_prefix='/api')
ativacao_blueprint = Blueprint('ativacao', __name__, url_prefix='/api')
venda_blueprint = Blueprint('venda', __name__, url_prefix='/api')
produtos_blueprint = Blueprint('produtos', __name__, url_prefix='/api')

@cadastro_blueprint.route('/sellers', methods=['POST'])
def cadastro():
    forms_cadastro = request.get_json()
    usuario = create_user(forms_cadastro)
    return jsonify(usuario), usuario['status_code']

@ativacao_blueprint.route('/sellers/activate', methods=['POST'])
def ativacao():
    forms_ativacao = request.get_json()
    ativacao_codigo = ativacao_cod(forms_ativacao)
    return jsonify(ativacao_codigo) 

@venda_blueprint.route('/sellers/venda', methods=['POST'])
@jwt_required()
def venda():
    id = get_jwt_identity()
    forms_venda = request.get_json()
    forms_venda['id_cliente'] = int(id)
    venda = create_venda(forms_venda)
    return jsonify(venda), venda['status_code']

UPLOAD_FOLDER = 'uploads/produtos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@produtos_blueprint.route('/produtos', methods=['POST'])
@jwt_required()
def cadastrar_produto():
    try:
        imagem = None
        if 'imagem' in request.files:
            file = request.files['imagem']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = f"{int(time.time())}_{filename}"
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                imagem = filepath

        dados = request.form
        id_vendedor = get_jwt_identity()
        
        novo_produto = Produtos(
            nome=dados['nome'],
            preco=float(dados['preco']),
            quantidade=int(dados['quantidade']),
            status='Ativo',
            imagem=imagem,
            id_vendedor=int(id_vendedor)
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
                'preco': novo_produto.preco,
                'status': novo_produto.status,
                'imagem': novo_produto.imagem
            }
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@produtos_blueprint.route('/produtos/<int:id>', methods=['DELETE'])
@jwt_required()
def deletar_produto(id):
    try:
        produto = Produtos.query.get(id)
        
        if not produto:
            return jsonify({'message': 'Produto não encontrado'}), 404
        
        if produto.imagem and os.path.exists(produto.imagem):
            os.remove(produto.imagem)
        
        db.session.delete(produto)
        db.session.commit()
        
        return jsonify({'message': 'Produto deletado com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
