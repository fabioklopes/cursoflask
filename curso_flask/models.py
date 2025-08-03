from curso_flask import db
from datetime import datetime


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    assunto = db.Column(db.String(255), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    respondeu = db.Column(db.Integer, default = 0)