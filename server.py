from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('Hello World!')

@app.route('/another-page')
def another_page():
    return 'This is another web page'

# /users/profile/123
# /users/gocodeup
@app.route('/hello/<name>')
def sayhello(name):
    return f'Hello, {name}!'

@app.route('/roll-dice')
def roll_dice():
    roll = randint(1, 6)
    return f'You rolled a {roll}'

@app.route('/roll-dice/<int:n>')
def roll_n_dice(n):
    rolls = [str(randint(1, 6)) for i in range(n)]
    return f'Your rolls are: {", ".join(rolls)}'

@app.route('/say/<greeting>/to/<name>')
def sayhelloto(greeting, name):
    return f'{greeting}, {name}!'
