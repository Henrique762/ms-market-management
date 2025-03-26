from flask import Blueprint, Flask,request, jsonify
from src.config.config import app
from src.Application.Validators.login import login_user

login_blueprint = Blueprint('login', __name__, url_prefix='/api')

@login_blueprint.route('/login', methods=['POST'])
def login():
    form_login = request.get_json()
    usuario = login_user(form_login)
    return jsonify(usuario)
    

