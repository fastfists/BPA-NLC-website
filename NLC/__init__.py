from flask import Flask

host_name = "127.0.0.1"
port = 5000

def create_app() -> Flask:
    from . import routes, models
    from .services import twitter
    app = Flask(__name__)
    routes.init_app(app)
    models.init_app(app)
    twitter.run()
    return app
