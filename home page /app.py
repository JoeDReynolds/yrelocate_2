import os
from flask import Flask, jsonify, render_template, url_for
import json
from bson import json_util
from bson.json_util import dumps
from flask_pymongo import PyMongo

from models import retrieve_population_data, insert_population_data,retrieve_Photos_data

##############################################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/yrelocate_db"
mongo = PyMongo(app)


##### Define routes #####################################################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/population")   
def population():
    print("---------------population-----------------")
    # Get the Data from MongoDc
    projects = retrieve_population_data(mongo)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    return json_projects   
#  retrive best Photos for citys
@app.route("/Photos") 
def Photos():
    print("---------------Photos-----------------")
    # Get the Data from MongoDc
    photo = retrieve_Photos_data(mongo)
    json_Photos = []
    for item in photo:
        json_Photos.append(item)
    json_Photos = json.dumps(json_Photos, default=json_util.default)
    return json_Photos  

################################################################################
################################################################################
if __name__ == '__main__':
    app.run(debug=True)    


# insert_population_data(mongo)