from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from .routes.home import home_bp


    app.register_blueprint(home_bp, url_prefix='/')

    return app

