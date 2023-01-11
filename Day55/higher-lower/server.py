from flask import Flask
import random

app = Flask(__name__)

print(__name__)


@app.route("/")
def guess_a_number():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:user_guess>")
def user_actually_guessing_the_number(user_guess):
    if user_guess == the_number:
        return "<h1>Bravo, you have guessed the right number!</h1>" \
               "<img src='https://media.giphy.com/media/kBZBlLVlfECvOQAVno/giphy.gif'>"
    elif user_guess > the_number:
        return "<h1>Can we get much higher? (Your guess is too high!)</h1>" \
               "<img src='https://media.giphy.com/media/MXi8nBJjIBgKbyA1MM/giphy.gif'>"
    elif user_guess < the_number:
        return "<h1>That's too low!</h1>" \
               "<img src='https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif'>"


the_number = random.randint(0, 9)

# if __name__ == '__main__':
app.run()
