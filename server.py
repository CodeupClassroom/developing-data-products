from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/another-page')
def another_page():
    return 'This is another web page'

# /users/profile/123
# /users/gocodeup
@app.route('/hello/<name>')
def sayhello(name):
    return f'Hello, {name}!'
