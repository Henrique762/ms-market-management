from src.config.config import db
from src.Infrastructure.Model.wpp import Validacao

def cadastrar_codigo(cliente, codigo):
    codigo_wpp = Validacao(codigo=codigo, cliente=cliente)
    db.session.add(codigo_wpp)
    db.session.commit()
    