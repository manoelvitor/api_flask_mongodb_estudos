from flask_restplus import fields
from mongoengine import Document, StringField, EmailField, DateField, SequenceField
from datetime import datetime

from src.server.instance import server

from flask import Blueprint

model_bp = Blueprint('model', __name__)



class Pessoa(Document):
    pessoa_id = SequenceField()
    nome = StringField(max_length=50)
    email = EmailField(max_length=50, unique=True)
    telefone = StringField(max_length=20)
    endereco = StringField(max_length=50)
    data_criacao = DateField(default=datetime.utcnow)


model = server.api.model(
  'Pessoa',
    {
        'pessoa_id' : fields.String(description='ID do registro'),
        'nome' : fields.String(description='Nome da pessoa'),
        'email' : fields.String(description='Email da pessoa'),
        'telefone' : fields.String(description='Telefone da pessoa'),
        'endereco' : fields.String(description='Endereco da pessoa'),
    }

)







