from flask import Blueprint, Flask,request, jsonify
from src.config.config import app
from src.Application.Validators.cadastro import create_user
from src.Application.Validators.login import login_user

cadastro_blueprint = Blueprint('cadastro', __name__, url_prefix='/api')

login_blueprint = Blueprint('login', __name__, url_prefix='/api')

@cadastro_blueprint.route('/cadastro', methods=['POST'])
def cadastro():
    forms_cadastro = request.get_json()
    usuario = create_user(forms_cadastro)
    return jsonify(usuario)

@login_blueprint.route('/login', methods=['POST'])
def login():
    form_login = request.get_json()
    usuario = login_user(form_login)
    return jsonify(usuario)