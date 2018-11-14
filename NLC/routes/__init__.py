from .home import home_bp
from .register import regis_bp
from .twitter import twitter_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(regis_bp)
    app.register_blueprint(twitter_bp)