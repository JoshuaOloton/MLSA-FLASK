from flask import Blueprint

pizza = Blueprint('pizza', __name__)

from app.pizza import views