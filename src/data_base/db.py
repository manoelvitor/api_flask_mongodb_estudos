from pymongo import MongoClient
from mongoengine import connect


from flask import Blueprint

data_base_bp = Blueprint('data_base', __name__)


class ConectDataBase():
    client = MongoClient(
        'mongodb+srv://manoelvitor:35681553@cluster0.1jibp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client['base_de_dados']
    col = db['pessoa']
    connect(host='mongodb+srv://manoelvitor:35681553@cluster0.1jibp.mongodb.net/base_de_dados?retryWrites=true&w=majority')


db = ConectDataBase()


# db.col.insert_one(
#     {
#         'pessoa_id': 2,
#         'nome': "Mel Lis",
#         'email': "mel@gmail.com",
#         'telefone': "139920022225",
#         'endereco': "São Vicente",
#         'data_criacao': ""
#     }
# )
