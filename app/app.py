# import os
# from flask import Flask, jsonify, render_template, url_for
import json
from bson import json_util
from flask import Flask, render_template
# from bson.json_util import dumps
from flask_pymongo import PyMongo

from models import retrive_population_data

# ########################################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/yrelocate_db"
mongo = PyMongo(app)


# Define routes ###############################################################
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/population")
def population():
    print("---------------population-----------------")
    # Get the Data from mongodb
    projects = retrive_population_data(mongo)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    return json_projects


# ###########################################################################
# ################################3##########################################

if __name__ == '__main__':
    app.run(debug=True)


# insert_population_data(mongo)
