from flask import Flask, render_template, request, redirect, url_for, flash
from . import item
from ..models import db, Item

@item.route("/index")
def index():
    all_data = Item.query.all()
    return render_template("index.html", employees=all_data)


@item.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        nome = request.form['nome']
        mac = request.form['mac']
        fonte = request.form['fonte']
        volts = request.form['volts']
        ampere = request.form['ampere']
        categoria = request.form['categoria']

        my_data = Item(nome, mac, fonte, volts, ampere, categoria)

        db.session.add(my_data)
        db.session.commit()

        flash("Item adicionado com sucesso")

        return redirect(url_for('item.index'))


@item.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Item.query.get(request.form.get('id_patrimonio'))
        my_data.nome = request.form['nome']
        my_data.mac = request.form['mac']
        my_data.fonte = request.form['fonte']
        my_data.volts = request.form['volts']
        my_data.ampere = request.form['ampere']
        my_data.categoria = request.form['categoria']
        db.session.commit()

        flash("Item atualizado com sucesso")

        return redirect(url_for('item.index'))


@item.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
 
    my_data = Item.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Item deletado com sucesso")

    return redirect(url_for('item.index'))
