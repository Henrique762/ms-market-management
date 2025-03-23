import random
from src.Infrastructure.http.wpp import gerar_msg
from src.Application.Service.wpp import info_usuario

def gerar_codigo():
    codigo = ""
    for num in range(4):
        numero = str(random.randint(1, 9))
        codigo += numero
    return codigo

