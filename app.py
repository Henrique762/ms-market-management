from src.config.config import app, db
from src.Application.Controllers.route import cadastro_blueprint, login_blueprint

app.register_blueprint(cadastro_blueprint)
app.register_blueprint(login_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])