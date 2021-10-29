from flask import Flask

from api.routes import api
#from site.routes import site
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["FLASK_ENV"]='development'
def create_app():
    app.register_blueprint(api)
    #app.register_blueprint(site)

    return app