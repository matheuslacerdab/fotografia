from fotografia import app, db, lm
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from fotografia.models.forms import LoginForm
from fotografia.models.models import User

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
        else:
            flash("Invalid Login.")
    
    return render_template('index.html') 

@app.route('/area_do_cliente/', methods=["GET","POST"])
def areaDoCliente():
    form = LoginForm()
    return render_template('area_do_cliente.html', form=form) 

@app.route('/logout/')
def logout():
    logout_user()
    flash("Logged Out.")
    return redirect(url_for("index"))


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')