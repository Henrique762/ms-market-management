from flask import Blueprint, Flask,request, jsonify
from src.config.config import app
from src.Application.Validators.cadastro import create_user
from src.Application.Validators.wpp import ativacao_cod

cadastro_blueprint = Blueprint('cadastro', __name__, url_prefix='/api')
ativacao_blueprint = Blueprint('ativacao', __name__, url_prefix='/api')

@cadastro_blueprint.route('/sellers', methods=['POST'])
def cadastro():
    forms_cadastro = request.get_json()
    usuario = create_user(forms_cadastro)
    return jsonify(usuario)

@ativacao_blueprint.route('/sellers/activate', methods=['POST'])
def ativacao():
    forms_ativacao = request.get_json()
    ativacao_codigo = ativacao_cod(forms_ativacao)
    return jsonify(ativacao_codigo) 