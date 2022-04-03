from flask import Flask, redirect, url_for, render_template, request
import main

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/select', methods=['POST'])
def makeSelections():
    main.unfulfilled_cores = request.form.getlist('checkbox')
    main.main()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

# commands ran:
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run
