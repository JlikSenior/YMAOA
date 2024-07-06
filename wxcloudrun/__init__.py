from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config

# pymysql.install_as_MySQLdb()

app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password, config.db_address)

# db = SQLAlchemy(app)

app.config.from_object('config')

from wxcloudrun.views import bp as mainbp
app.register_blueprint(mainbp)