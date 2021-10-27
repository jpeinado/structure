from flask import Blueprint

api = Blueprint('api',__name__, url_prefix='/api')
@api.get('/')
def getdata():
    return {'key' : 'value'}
    