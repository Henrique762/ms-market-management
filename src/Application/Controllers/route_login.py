from flask import Blueprint, Flask,request, jsonify
from src.Application.Validators.login import login_user, login_auth
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.config.config import app
from src.Application.Validators.login import login_user

login_blueprint = Blueprint('login', __name__, url_prefix='/api')

@login_blueprint.route('/login', methods=['POST'])
def login():
    form_login = request.get_json()
    usuario = login_user(form_login)
    return jsonify(usuario), usuario['status']
    
@login_blueprint.route('/login/auth', methods=['GET'])
@jwt_required()
def protected():
    vendedor_id = get_jwt_identity()
    vendedor = login_auth(vendedor_id)
    return jsonify(vendedor), vendedor['status']
