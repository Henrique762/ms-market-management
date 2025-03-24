import random
from src.Application.Service.wpp import validar_cod_e_tel

def gerar_codigo():
    codigo = ""
    for num in range(4):
        numero = str(random.randint(1, 9))
        codigo += numero
    return codigo

def ativacao_cod(form):
    validar = validar_cod_e_tel(form['codigo'], form['celular'])
    return validar
