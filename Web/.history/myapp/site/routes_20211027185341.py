from flask import Blueprint

site = Blueprint('site',__name__)
@site.get('/')
def index():
    return '<h1> Bienvenidos a mi pagina web </h1>'
    