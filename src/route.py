from config.config import app, request, jsonify
from Application.Controllers.cadastro import validacao

@app.route('/cadastro', methods=['POST'])
def cadastro():
    forms_cadastro = request.get_json()
    validacao_retorno = validacao(forms_cadastro)
    return jsonify(validacao_retorno)

@app.route('/cadastro/validacao', methods=['POST'])
def validar():
    


@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    username = dados.get('username')
    email = dados.get('email')
    celular = dados.get('celular')
    senha = dados.get('senha')


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])

    
