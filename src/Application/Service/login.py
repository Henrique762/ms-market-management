from flask import request, jsonify 
from src.Infrastructure.Model.usuario import Vendedores

def vendedor_cadastrado(form):
    vendedor = Vendedores.query.filter_by(email=form['email']).first()
    return vendedor is not None 

def vendedor_senha(form):
    vendedor = Vendedores.query.filter_by(email=form['email']).first()

    if not vendedor or vendedor.senha != form['senha']:
        return {"message": "E-mail ou senha inválidos.", "status": False}

    if vendedor.status != 'Ativo':
        return {"message": "Usuário inativo. Não é possível fazer login.", "status": False}

    return {"message": "Login realizado com sucesso.", "status": True}

