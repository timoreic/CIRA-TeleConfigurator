from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #build the app
app.config.from_object(Config) #load configuation

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
db.init_app(app)

from app import views