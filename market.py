from flask import Flask
from flask import render_template
from datas import items

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    context = {
        "items" : items
    }

    return render_template("market.html", **context)