from Infrastructure.http.Model.login import User

class UserRepositorio:
    def get_by_email(self, email: str):
        return User.query.filter_by(email=email).first()