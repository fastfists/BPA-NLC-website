from .home import home_bp
from .register import regis_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(regis_bp)