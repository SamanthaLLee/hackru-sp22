from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# commands ran:
# export FLASK_APP=hello.py
# export FLASK_ENV=development
# flask run

# 