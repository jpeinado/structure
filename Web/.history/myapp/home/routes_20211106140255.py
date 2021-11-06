from flask import Blueprint, render_template

site = Blueprint('site', __name__, url_prefix='/site')
@site.route('/')
def index():
    return '<h1> Bienvenidos a mi segunda pagina web </h1>'
    