from random import randint
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

    message = f'{greeting}, {name}!'

    n_dice = len(name)
    rolls = [randint(1, 6) for i in range(n_dice)]

    return render_template(
        'greeting.html',
        message=message,
        rolls=rolls,
    )

# This function produces a response for one type of request
@app.route('/greet-multiple')
def greet_multiple():
    # Data processing
    names = ['ryan', 'chase', 'jada', 'alec', 'david', 'daniel']
    greetings = [f'Hello, {name}!' for name in names]

    return render_template('greet-multiple.html', greetings=greetings)

@app.route('/order-pizza')
def show_order_pizza_form():
    return render_template('order-pizza-form.html')

@app.route('/order-pizza', methods=['POST'])
def handle_pizza_order_submission():

    topping1 = request.form['topping1']
    topping2 = request.form['topping2']
    pizza = f'{topping1} and {topping2}'

    return f'One pizza with {pizza} on the way!'

@app.route('/count-to')
def count_to():
    return render_template('counting-form.html')

@app.route('/count-to', methods=['POST'])
def handle_counting_form_submission():
    n = int(request.form['n'])
    numbers = range(1, n + 1)

    return render_template(
        'counting-results.html',
        numbers=numbers
    )
