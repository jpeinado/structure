from flask import Blueprint

site = Blueprint('site', __name__, url_prefix='/site')
@site.route('/')
def index():
    return '<h1> Bienvenidos a mi pagina web </h1>'
    