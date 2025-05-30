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

#### Cdastro Vendas ####
@venda_blueprint.route('/sellers/venda', methods=['POST'])
@jwt_required()
def venda():
    id = get_jwt_identity()
    forms_venda = request.get_json()
    forms_venda['id_vendedor'] = int(id)
    venda = create_venda(forms_venda)
    return jsonify(venda), venda['status_code']