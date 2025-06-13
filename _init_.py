from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manage= LoginManager()
login_manage.login_view = "login"

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '2shotsforHarden'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///psytrack.db'

    db.init_app(app)
    login_manage.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app

