from flask import Blueprint

api = Blueprint('api',__name__, url_prefix='/api')
@api.get('/')
def getdata():
    return "<h1>Esta es una prueba</h1>"
    