from src.Infrastructure.Model.usuario import Vendedores
from flask_jwt_extended import create_access_token, jwt_required

def vendedor_cadastrado(form):
    
    vendedor = Vendedores.query.filter_by(email=form['email']).first()
    if vendedor:
        return True
    else:
        return False
    

def vendedor_senha(form):

    vendedor = Vendedores.query.filter_by(email=form['email']).first()
    if vendedor and vendedor.senha == form['senha']:
        if vendedor.status != 'Ativo':
            return {"message": "Usuário inativo. Não é possível fazer login.", "status": False}
        
        access_token = create_access_token(identity=vendedor.id)

        return {"message": access_token, "status": True}

    else:
        return {"message": "Senha incorreta.", "status": False}
        
        
        


