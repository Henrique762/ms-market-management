from src.Infrastructure.Model.usuario import Vendedores
from src.config.config import db

def adicionar_vendedor(form):
    print(form)
    usuario = Vendedores(nome=form['nome'], cnpj=form['cnpj'], email=form['email'], senha=form['senha'], numero_cel=form['celular'], status=form['status'])
    db.session.add(usuario)
    db.session.commit()
    return 'Usuario Cadastrado'

def validacao_vendedor(form):

    vendedor_cnpj = Vendedores.query.filter_by(cnpj=form['cnpj']).first()
    if vendedor_cnpj:
        return "CNPJ já cadastrado."
    
    vendedor_email = Vendedores.query.filter_by(email=form['email']).first()
    if vendedor_email:
        return "Email já cadastrado."
    
    return True
