from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import LoginForm, RegisterForm
from market import db
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/market')
@login_required
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
                            password = form.password1.data)
        db.session.add(user_to_create)
        flash(f'Success! You are logged in as {user_to_create.username}', 'success')
        db.session.commit()
        login_user(user_to_create)
        return redirect(url_for('market_page'))

    if form.errors != {} :
        for err_msg in form.errors.values() :
            flash('Error creating user : '+str(err_msg[0]) , category='danger')

    return render_template("register.html", **context)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    context = {
        "form" : form
    }

    if form.validate_on_submit():
        attempt_user = User.query.filter_by(username=form.username.data).first()
        if attempt_user and attempt_user.check_password(form.password.data):
            login_user(attempt_user)
            flash(f'Success! You are logged in as {attempt_user.username}', 'success')
            return redirect(url_for('market_page'))
        
        elif attempt_user:
            flash('Invalid credentials', 'danger')
        
        else :
            flash('User does not exist!', 'danger')
        
    if form.errors != {} :
        for err_msg in form.errors.values() :
            flash('Invalid credentials' , category='danger')

    return render_template("login.html", **context)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))