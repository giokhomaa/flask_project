from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '321321c21321c321s321212c1d2'
    return app