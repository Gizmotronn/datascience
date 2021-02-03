# Import required modules/libraries
from flask import flask

# Setup application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

if __ name__ == '__main__':
    app.run()