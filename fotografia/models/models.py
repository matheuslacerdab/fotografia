# encoding: utf-8
from fotografia import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Usuário: %r>" % self.username


class Evento(db.Model):
    __tablename__ = "evento"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, unique=True)
    
    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return "<Evento: %r>" % self.descricao


class Foto(db.Model):
    __tablename__ = "foto"

    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'),
        nullable=False)
    filename = db.Column(db.String, unique=True)
    url = db.Column(db.String, unique=True)

    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return "<Imagem: %r>" % self.filename


