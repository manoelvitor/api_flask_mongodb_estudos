from pymongo import MongoClient
from mongoengine import connect

from flask import Blueprint

data_base_bp = Blueprint('data_base', __name__)


class ConectDataBase():
    client = MongoClient('localhost')
    db = client['base_de_dados']
    col = db['pessoa']
    connect(db='base_de_dados')


db = ConectDataBase()





  