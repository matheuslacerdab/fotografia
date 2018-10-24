# encoding: utf-8
from fotografia import app
from flask import Flask, render_template, redirect, url_for, request
from fotografia.models.models import Evento, Foto
from fotografia import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/area_do_cliente/')
def areaDoCliente():
    return render_template('area_do_cliente.html')  

@app.route('/cad_evento/',methods=['GET', 'POST'])
def cadEvento():
    if request.method == 'POST':
        descricao = request.form['descricao']
        
        e = Evento(descricao)        
        db.session.add(e)
        db.session.commit()

        return redirect(url_for('cadFoto'))

    return render_template('cad_evento.html')

@app.route('/cad_foto/',methods=['GET', 'POST'])
def cadFoto():
    if request.method == 'POST':
        filename = photos.save(request.files['img'])
        url = photos.url(filename) 
        
        f = Evento(filename, url)        
        db.session.add(f)
        db.session.commit()

    return render_template('cad_foto.html')

