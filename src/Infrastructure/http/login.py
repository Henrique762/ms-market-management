from config import db 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(120), nullable=False)
   
    def to_dict(self ):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'celular': self.celular,
            'senha': self.senha
        }
