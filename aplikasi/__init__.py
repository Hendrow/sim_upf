from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_pyfile('config.py')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from aplikasi import models

from aplikasi.main.routes import mod
app.register_blueprint(mod)

from aplikasi.user.routes import mod
app.register_blueprint(mod)

from aplikasi.alat.routes import mod
app.register_blueprint(mod)

from aplikasi.fasyankes.routes import mod
app.register_blueprint(mod)

from aplikasi.pinjam.routes import mod
app.register_blueprint(mod)