from flask import Flask, jsonify, request,Response
from flask_restplus import Api, Resource
from src.model.pessoa import Pessoa
from src.model.pessoa import model


from src.data_base.db import db
from src.server.instance import server
from src.service.pessoa_service import service


from flask import Blueprint


controller_bp = Blueprint('controller', __name__)

app = server.app
api = server.api




@api.route('/pessoas')
class Pessoas(Resource): 
    @api.expect(model)
    def get(self,):
        data=[]
        for pessoa in service.findAll():
            data.append({
                'pessoa_id': pessoa['pessoa_id'],
                'nome': pessoa['nome'],
                'email': pessoa['email'],
                'telefone': pessoa['telefone'],
                'data_criacao': pessoa['data_criacao'],
                'endereco': pessoa['endereco']            
        })  
        return jsonify(data)
  

    
    @api.expect(model)
    def post(self,):    
        nome = request.json['nome']
        email = request.json['email']
        telefone = request.json['telefone']
        endereco = request.json['endereco']
        service.save(nome, email, telefone, endereco)
        return  Response({'Dados Enviados'}, status=201, mimetype='application/json')


@api.route('/pessoas/<id>')
class Pessoa(Resource):      
    @api.expect(model)
    def get(self, id):
        return jsonify(service.getById(id))
    
    @api.expect(model)
    def put(self,id):
        nome = request.json['nome']
        email = request.json['email']
        telefone = request.json['telefone']
        endereco = request.json['endereco'] 
        pessoa = db.col.find_one({'pessoa_id': int(id)})
        if pessoa:
            service.update(id, nome, email, telefone, endereco)
            return  Response({'Dados Atualizados'}, status=204, mimetype='application/json')
        else:
            return  Response({'Não foi possivel atualizar, verifique os dados'}, status=204, mimetype='application/json')  
  
    def delete(self,id):
        return jsonify(service.deleteById(int(id)))



    

        




