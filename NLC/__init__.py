from flask import Flask

def create_app() -> Flask:
    from NLC import routes, models
    app = Flask(__name__)
    routes.init_app(app)
    models.init_app(app)
    return app
