from flask import Blueprint, Flask,request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.config.config import app
from src.Application.Validators.cadastro import create_user
from src.Application.Validators.vendas import create_venda
from src.Application.Validators.wpp import ativacao_cod
from src.Application.Validators.login import login_user

cadastro_blueprint = Blueprint('cadastro', __name__, url_prefix='/api')
ativacao_blueprint = Blueprint('ativacao', __name__, url_prefix='/api')
venda_blueprint = Blueprint('venda', __name__, url_prefix='/api')
login_blueprint = Blueprint('login', __name__, url_prefix='/api')



@login_blueprint.route('/login/auth', methods=['POST'])
def login():
    form_login = request.get_json()
    usuario = login_user(form_login)
    print(type(usuario))
    return jsonify(usuario), usuario['status']
    

#### Cadastro Sellers ####
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

#### Cadastro Vendas ####
@venda_blueprint.route('/sellers/venda', methods=['POST'])
@jwt_required()
def venda():
    id = get_jwt_identity()
    forms_venda = request.get_json()
    forms_venda['id_vendedor'] = int(id)
    venda = create_venda(forms_venda)
    return jsonify(venda), venda['status_code']

#### ROTAS PRODUTOS ####

@produtos_bp.route('/produtos/<int:produto_id>', methods=['PUT'])
@jwt_required()
def editar_produto(produto_id):
    data = request.get_json()
    id = get_jwt_identity()

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
        return jsonify({'message': 'Dados inválidos', 'errors': erros}), 400

    produto = Produtos.query.get(produto_id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404

    try:
        produto.id_vendedor = id
        produto.quantidade = data['quantidade']
        produto.valor = float(data['valor'])
        produto.status = data['status']

        db.session.commit()
        return jsonify({'message': 'Produto atualizado com sucesso'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Erro ao atualizar produto: {str(e)}'}), 500

@produtos_bp.route('/produtos', methods=['GET'])
@jwt_required()
def listar_produtos():
    
    id = get_jwt_identity()

    produtos = listar_produto(id)
    
    return jsonify(produtos), 200

@produtos_bp.route('/produtos/<int:produto_id>', methods=['GET'])
@jwt_required()
def obter_produto(produto_id):
    id_vendedor = get_jwt_identity()

    produto_dict, erro_response, status_code = mostrar_produto_por_id(id_vendedor, produto_id)

    if erro_response:
        return jsonify(erro_response), status_code

    return jsonify(produto_dict), 200