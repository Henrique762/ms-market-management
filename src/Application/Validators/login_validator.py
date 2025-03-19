from Infrastructure.http.login_repositorio import UserRepositorio
from Infrastructure.http.token import JWTProvider

class LoginService:
    def __init__(self, login_repositorio: UserRepositorio, token_provider: JWTProvider):
        self.login_repositorio = login_repositorio
        self.token_provider = token_provider

    def authenticate(self, email: str):
        user = self.login_repositorio.get_by_email(email)
        if not user:
            return None
        return self.token_provider.generate_token(user)
