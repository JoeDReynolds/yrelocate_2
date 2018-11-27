from flask import Flask
import os

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://joe_reynolds:op3nupd4n@ds155903.mlab.com:55903/heroku_j29mjxk2'

# "mongodb://localhost:27017/yrelocate_db"

# Set base directory ##################################################
app.config['basedir'] = os.path.abspath(os.path.dirname(__file__))

from flask_pymongo import PyMongo
# store the PyMongo/MongoDBB client object in the flask app.config
app.config['pymongo_db'] = PyMongo(app)

from app import routes, models   # retrieve_population_data
# import app