from app.pizza import pizza
from flask import render_template


@pizza.route('/')
@pizza.route('/home')
def index():
    return render_template('index.html')

@pizza.route('/new')
def new_pizza():
    pass

@pizza.route('/delete')
def delete_pizza():
    pass