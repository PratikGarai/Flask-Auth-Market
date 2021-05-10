from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    context = {
        "items" : Item.query.all()
    }
    return render_template("market.html", **context)

@app.route('/register')
def register_page():
    form = RegisterForm()
    context = {
        "form" : form
    }
    return render_template("register.html", **context)