from flask import Flask
from random import choice

app = Flask(__name__)

number = choice(range(1, 10))


@app.route("/")
def main_page():
    return (
        "<h1> Guess a number between 0 and 9 </h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


@app.route("/<int:num>")
def check(num):
    if num > number:
        return (
            "<h1>Too High! Try again.</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        )

    elif num < number:
        return (
            "<h1> Too low! Try again.</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        )
    else:
        return (
            "<h1>Correct!</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        )


if __name__ == "__main__":
    app.run(debug=True)
