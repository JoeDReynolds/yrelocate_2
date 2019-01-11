import os
from flask import Flask, jsonify, render_template, url_for
import json
from bson import json_util
from bson.json_util import dumps
from flask_pymongo import PyMongo

from models import retrive_population_data, insert_population_data, insert_home_rental_data, insert_school_data

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


# @app.route("/housing")
# def housing():
        
#     print("---------------housing-----------------")
#      # Get the Data from MongoDc
#     housedata = retrive_housing_data(mongo)
#     json_housing = []
#     for item in housedata:        
#         json_housing.append(item)
#     json_housing = json.dumps( json_housing, default=json_util.default)
#     return  jsonify(json_housing)

################################################################################
################################################################################
if __name__ == '__main__':
    app.run(debug=True)  


# insert_population_data(mongo)
#insert_home_rental_data(mongo)
# while (True):
#     if(insert_home_rental_data(mongo)):
#         break; 
#     else:
#         print("Trying again")
# insert_home_rental_data(mongo)

# insert_school_data("2018 Austin - High.csv", mongo.db.highschool)