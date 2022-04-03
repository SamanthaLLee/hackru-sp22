from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/select', methods=['POST'])
def makeSelections():
    print(request.form.getlist('checkbox'))
    # example result: ['AHq', 'WCr']
    # do something
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

# commands ran:
# export FLASK_APP=hello.py
# export FLASK_ENV=development
# flask run
