from flask import Flask

# Init app with proper name
app = Flask(__name__)

# Load config
app.config.from_object('config')


@app.route('/test')
def hello_world():
    return '<h1>Hello World</h1>'
