from flask import Flask
from flask_wtf.csrf import CSRFProtect
#from flask_migrate import Migrate
from .config import Config
from .auth import auth
from .item import item
#from .author import author
#from .book import book
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = "secretkey"
    app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
    #csrf = CSRFProtect(app)    
    #csrf.init_app(app)
    app.register_blueprint(item)
    app.register_blueprint(auth)
    #app.register_blueprint(author)
    #app.register_blueprint(book)
    db.init_app(app)
    #Migrate(app, db, directory='./migrations')
    return app