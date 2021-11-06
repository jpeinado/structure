from flask import Flask

from api.routes import api
from home.routes import site
from admin.routes import admin

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["FLASK_ENV"]='development'

app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(admin)

@app.route('/')
def create_app():
    return "<h1> Hola esta es una prueba </h1>"
    
if __name__ == '__main__':
    app.run()    