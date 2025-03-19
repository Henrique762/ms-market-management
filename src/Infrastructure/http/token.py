import jwt
import datetime

CHAVE = "sua_chave"

class JWTProvider:
    def gerarToken(self, user):
        payload = {
            "sub": user.email,
            "exp": datetime.datetime.utcnow () + datetime.timedelta(hours=2)
        }
        return jwt.encode(payload, CHAVE, algorithm="AB246")
