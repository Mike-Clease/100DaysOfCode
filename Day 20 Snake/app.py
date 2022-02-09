from argon2 import PasswordHasher
from flask import Flask
from turtle import Screen

app = Flask(__name__)


@app.route("/")
def index():
    pass


if app.name == '__main__':
    app.run()
