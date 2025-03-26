from flask import Blueprint, Flask,request, jsonify
from src.config.config import app
from src.Application.Validators.login import login_user

login_blueprint = Blueprint('login', __name__, url_prefix='/api')


@login_blueprint.route('/login', methods=['POST'])
def login():
    form_login = request.get_json()
    usuario = login_user(form_login)
    return jsonify(usuario)
    
    # vendedor = vendedor_senha.query.filter_by(email=forms_login['email']).first()

    # if not vendedor:
    #     return jsonify({"message": "Usuário não encontrado.", "status": False})
    

    # if not check_password_hash(vendedor.senha, forms_login['senha']):
    #     return jsonify({"message": "Senha incorreta.", "status": False}) 

    
    # if vendedor.status != "Ativo":
    #     return jsonify({"message": "Usuário inativo. Não é possível fazer login.", "status": False})

