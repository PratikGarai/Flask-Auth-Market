from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db

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

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    context = {
        "form" : form
    }

    if form.validate_on_submit():
        user_to_create = User(
                            username = form.username.data,
                            email = form.email.data,
                            password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        print("Here")
        return redirect(url_for('market_page'))

    return render_template("register.html", **context)