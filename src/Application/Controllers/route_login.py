from flask import Flask, request, jsonify
from Application.Validators.login_validator import LoginService
from Infrastructure.http.login_repositorio import UserRepositorio
from Infrastructure.http.token import JWTProvider
from config.config import db
from Infrastructure.http.Model.login import User

app = Flask(__name__)


# Criar instâncias
user_repo = UserRepositorio()
jwt_provider = JWTProvider()
login_service = LoginService(user_repo, jwt_provider)

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    email = dados.get("email")

    token = login_service.authenticate(email)
    if not token:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    return jsonify({"token": token}), 200


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])

novo_usuario = User(email="gabrielly@email.com", password="123456")
db.session.add(novo_usuario)
db.session.commit()