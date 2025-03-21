from flask import Blueprint, Flask,request, jsonify
from src.config.config import app
from src.Application.Validators.cadastro import create_user

cadastro_blueprint = Blueprint('cadastro', __name__, url_prefix='/api')

@cadastro_blueprint.route('/sellers', methods=['POST'])
def cadastro():
    forms_cadastro = request.get_json()
    usuario = create_user(forms_cadastro)
    return jsonify(usuario)