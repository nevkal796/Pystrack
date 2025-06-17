from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2shotsforHarden'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///psytrack.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import routes  # correct relative import
    app.register_blueprint(routes)

    return app
