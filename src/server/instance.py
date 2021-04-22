from flask import Flask, Blueprint
from flask_restplus import Api


server_bp = Blueprint('server', __name__)


#A classe Api tem o objetivo de  documentar a api, e trabalhar em conjunto do flask que no caso foi instanciado como app
#API(nome servidor, versão, titulo, descrição, rota da documentacao)

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='Cadastro Pessoas',
            description='Api simples para cadastro de pessoa, com fins de estudo (ESTÁGIO)',
            doc='/docs'
        )
    
    # para startar a aplicação
    def run(self,):
        self.app.run(
            debug= True
        )

#instanciando o server para ser usado no main

server = Server()