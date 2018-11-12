from flask import Flask

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/yrelocate_db"

import pymongo
app.mongo = pymongo

# mongo = PyMongo(app)

from app import routes, retrieve_population_data
