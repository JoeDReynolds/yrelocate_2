import os
from flask import Flask, jsonify, render_template, url_for
import json
from bson import json_util
from bson.json_util import dumps
from flask_pymongo import PyMongo
import pandas as pd

from models import retrive_population_data, insert_population_data,retrive_housing_data,retrive_elementary_data,retrive_highschool_data,retrive_middleschool_data

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


@app.route("/housing") 
def housing():
    print("---------------housing-----------------")
    # Get the Data from MongoDc
    housedata = retrive_housing_data(mongo)
    json_housing = []
    df=pd.DataFrame(list(housedata))
    df1=pd.DataFrame()
    # replace null value for rent housing to 1100 $
    df1[["AveRentPrice", "coordinates","ZipCode","AveHomePrice" ,"display_name" ] ]=df[["AveRentPrice", "coordinates","ZipCode","AveHomePrice" ,"display_name" ]]
    df1["AveRentPrice"].fillna(1000, inplace = True)
    # df1=df1.dropna()
    json_housing=df1.T.to_dict().values()
    json_housing = json.dumps( json_housing, default=json_util.default)
    print(json_housing)
    return  json_housing


@app.route("/elementary") 
def school():
    print("---------------elementary-----------------")
    # Get the Data from MongoDc
    schooldata = retrive_elementary_data(mongo)
    json_elementary = []
    ele_df=pd.DataFrame(list(schooldata))
    elementary_df=pd.DataFrame()
    elementary_df[["ZipCode","coordinates","display_name","state_Rank","reginal_rank"]] = ele_df[["ZipCode","coordinates","display_name","state_Rank","reginal_rank"]]
    elementary_df=elementary_df.dropna()
    json_elementary=elementary_df.T.to_dict().values()
    json_elementary = json.dumps( json_elementary, default=json_util.default)
    return  json_elementary 

    # ********
@app.route("/highschool") 
def highschool():
    print("---------------highschool-----------------")
    # Get the Data from MongoDc
    highschooldata = retrive_highschool_data(mongo)
    json_highschool= []
    high_df=pd.DataFrame(list(highschooldata))
    highschool_df=pd.DataFrame()
    highschool_df[["ZipCode","coordinates","display_name","state_Rank","reginal_rank"]] = high_df[["ZipCode","coordinates","display_name","state_Rank","reginal_rank"]]
    highschool_df=highschool_df.dropna()
    json_highschool=highschool_df.T.to_dict().values()
    json_highschool = json.dumps( json_highschool, default=json_util.default)
    return  json_highschool 

# ******
@app.route("/middleschool") 
def middleschool():
    print("---------------middleschool-----------------")
    # Get the Data from MongoDc
    midschooldata = retrive_middleschool_data(mongo)
    json_midschool= []
    mid_df=pd.DataFrame(list(midschooldata))
    midschool_df=pd.DataFrame()
    midschool_df[["ZipCode","coordinates","display_name","state_Rank","reginal_rank"]] = mid_df[["ZipCode","coordinates","display_name","state_Rank","reginal_rank"]]
    midschool_df=midschool_df.dropna()
    json_midschool=midschool_df.T.to_dict().values()
    json_midschool = json.dumps( json_midschool, default=json_util.default)
    return  json_midschool 


################################################################################
################################################################################
if __name__ == '__main__':
    app.run(debug=True)    

