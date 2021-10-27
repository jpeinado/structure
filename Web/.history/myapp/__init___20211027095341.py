from flask import Flask
from .api.routes import api
from .site.routes import site
app = Flask(__name__)
@app.route('/',methods=['GET'])
def create_app():
    app.config["DEBUG"] = True
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app
if __name__ == '__main__':
    app.run()