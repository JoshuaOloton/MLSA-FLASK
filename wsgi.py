from flask import Flask, render_template
from app import create_app

app = create_app('development')

if __name__ == "_main__":
    app.run(debug=True)