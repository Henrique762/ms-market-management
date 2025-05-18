from src.config.config import app, db
from src.Application.Controllers.route import cadastro_blueprint, ativacao_blueprint, venda_blueprint
from src.Application.Controllers.route_login import login_blueprint

app.register_blueprint(cadastro_blueprint)
app.register_blueprint(ativacao_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(venda_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])