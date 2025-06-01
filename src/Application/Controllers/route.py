from flask import Blueprint, Flask,request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.config.config import app
from src.Application.Validators.cadastro import create_user
from src.Application.Validators.vendas import create_venda
from src.Application.Validators.wpp import ativacao_cod
from src.Application.Validators.login import login_user
from src.Application.Validators.produto import edit_produto, listar_produto, mostrar_produto_por_id

cadastro_blueprint = Blueprint('cadastro', __name__, url_prefix='/api')
ativacao_blueprint = Blueprint('ativacao', __name__, url_prefix='/api')
venda_blueprint = Blueprint('venda', __name__, url_prefix='/api')
login_blueprint = Blueprint('login', __name__, url_prefix='/api')
produtos_bp = Blueprint('produtos', __name__, url_prefix='/api')


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
    id = get_jwt_identity()
    data = request.get_json()
    data['id_vendedor'] = int(id)
    data['id_produto'] = int(produto_id)
    result = edit_produto(data)

    return jsonify(result), result['status_code']

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