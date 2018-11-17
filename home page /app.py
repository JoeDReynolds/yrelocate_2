import os
from flask import Flask, jsonify, render_template, url_for
import json
from bson import json_util
from bson.json_util import dumps
from flask_pymongo import PyMongo

from models import retrive_population_data, insert_population_data,retrive_housing_data,retrive_elementary_data

##############################################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://joe_reynolds:op3nupd4n@ds155903.mlab.com:55903/heroku_j29mjxk2"
mongo = PyMongo(app)


##### Define routes #####################################################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/population")   
def population():
    print("---------------population-----------------")
    # Get the Data from MongoDc
    projects = retrive_population_data(mongo)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    return json_projects   
#  retrive best Photos for citys

@app.route("/housing") 
def housing():
    print("---------------housing-----------------")
    # Get the Data from MongoDc
    housedata = retrive_housing_data(mongo)
    json_housing = []
    for item in housedata:
        json_housing.append(item)
    json_housing = json.dumps( json_housing, default=json_util.default)
    return  json_housing  


@app.route("/elementary") 
def school():
    print("---------------elementary-----------------")
    # Get the Data from MongoDc
    schooldata = retrive_elementary_data(mongo)
    json_school = []
    for school in schooldata:
        json_school.append(school)
    json_school = json.dumps( json_school, default=json_util.default)
    return  json_school 




################################################################################
################################################################################
if __name__ == '__main__':
    app.run(debug=True)    
