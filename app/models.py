from flask_sqlalchemy import SQLAlchemy
from datetime import date
db = SQLAlchemy()

item_has_entrada = db.Table('item_has_entrada',
    db.Column('entrada_id', db.Integer, db.ForeignKey('entrada.id_entrada'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id_patrimonio'), primary_key=True)
)
item_has_saida = db.Table('item_has_saida',
    db.Column('saida_id', db.Integer, db.ForeignKey('saida.id_saida'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id_patrimonio'), primary_key=True)
)
class Item(db.Model):
    id_patrimonio = db.Column(db.Integer, primary_key=True)
    data_cadastro = db.Column(db.Date, nullable=False, default=date.today)
    nome = db.Column(db.String(80), nullable=False)
    mac = db.Column(db.String(12), nullable=False)
    fonte = db.Column(db.String(80), nullable=False)
    volts = db.Column(db.Integer, primary_key=False)
    ampere = db.Column(db.Float(2,2), primary_key=False)
    obs_item = db.Column(db.String(455), nullable=False)
    categoria = db.relationship('Categoria', backref='item', lazy='dynamic')
    produto = db.relationship('Produto', backref='item', lazy='dynamic')
    
    def __init__(self, nome, mac, fonte, volts, ampere, categoria):
        self.nome = nome
        self.mac = mac
        self.fonte = fonte
        self.volts = volts
        self.ampere = ampere
        self.categoria = categoria

class Categoria(db.Model):
    id_categoria = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id_patrimonio'))
    
    def __init__(self, descricao, item_id):
        self.descricao = descricao
        self.item_id = item_id

class Entrada(db.Model):
    id_entrada = db.Column(db.Integer, primary_key=True)
    data_create = db.Column(db.Date, nullable=False, default=date.today)
    documento = db.Column(db.String(45), nullable=False)
    qtd = db.Column(db.Integer, primary_key=False)
    motivo = db.Column(db.String(100), nullable=False)
    obs_entrada = db.Column(db.String(455), nullable=False)