from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)

    from app.pizza import pizza
    app.register_blueprint(pizza)

    return app
