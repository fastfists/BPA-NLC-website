from flask import Flask

host_name = "127.0.0.1"
port = 5000

def create_app() -> Flask:
    from . import routes, models
    app = Flask(__name__)
    routes.init_app(app)
    models.init_app(app)
    return app
