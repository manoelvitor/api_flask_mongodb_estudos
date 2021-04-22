from pymongo import MongoClient
from mongoengine import connect
from src.model.pessoa import Pessoa
from src.data_base.db import db

from flask import Blueprint

service_bp = Blueprint('service', __name__)


class PessoaService:
    def __init__(self):
        self.db = db

    def findAll(self):
        return self.db.col.find()

    def save(self, nome, email, telefone, endereco):
        self.pessoa = Pessoa()   
        self.pessoa.nome = nome
        self.pessoa.email = email
        self.pessoa.telefone = telefone
        self.pessoa.endereco = endereco
        self.pessoa.save()

    def update(self, id, nome, email, telefone, endereco):
        self.pessoa = Pessoa.objects(pessoa_id = int(id))
        self.pessoa.update(nome = nome)
        self.pessoa.update(email = email)
        self.pessoa.update(telefone = telefone)
        self.pessoa.update(endereco = endereco)
    
    def getByName(self, nome):
        self.pessoa = self.db.col.find_one({'nome': nome})
        if self.pessoa:
            self.data = {
                'pessoa_id': self.pessoa['pessoa_id'],
                'nome': self.pessoa['nome'],
                'email': self.pessoa['email'],
                'telefone': self.pessoa['telefone'],
                'endereco': self.pessoa['endereco'],
                'data_criacao': self.pessoa['data_criacao']
            }
        else:
            self.data = 'Sem resultados'
        return self.data
    
    def getById(self, id):
        self.pessoa = self.db.col.find_one({'pessoa_id': int(id)})
        if self.pessoa:
            self.data = {
                'pessoa_id': self.pessoa['pessoa_id'],
                'nome': self.pessoa['nome'],
                'email': self.pessoa['email'],
                'telefone': self.pessoa['telefone'],
                'endereco': self.pessoa['endereco'],
                'data_criacao': self.pessoa['data_criacao']
            }
        else:
            self.data = 'Sem resultados'
        return self.data

    def deleteById(self,id):
        pessoa = db.col.find_one({'pessoa_id': id})
        if pessoa:
            db.col.delete_one({'pessoa_id':id})
            resposta = 'Deletado com sucesso'          
        else:
            resposta = 'Não foi possivel deletar'
        return resposta
      






service = PessoaService()







