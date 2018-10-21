from fotografia import app
from flask import Flask, render_template, redirect, url_for, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/area_do_cliente/')
def areaDoCliente():
    return render_template('area_do_cliente.html')  