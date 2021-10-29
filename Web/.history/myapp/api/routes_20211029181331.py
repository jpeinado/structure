from flask import Blueprint

api = Blueprint('api',__name__, url_prefix='/api')
@api.route('/')
def getdata():
    return "<h1> Bienvenidos mi primer pagina </h1>"
    