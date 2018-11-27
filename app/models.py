""" 
yRelocate: This modules parces the csv file and insert it in MongoDb

"""
# from .app import mongo
#imports
import os 
import pandas as pd
import numpy as np
import json
import pymongo
from geopy.geocoders import Nominatim
from flask_pymongo import PyMongo

# from .app import mongo

#### Set base directory ##################################################
basedir = os.path.abspath(os.path.dirname(__file__))

# collection_name = 'population' 
# db_population = mongo['population']
#self.db_population.remove()

def insert_population_data(mongo):
    #### Read from the population CSV file #####################################
    geolocator = Nominatim()
    population_df = pd.read_csv(basedir + "/static/resources/USTexasPoulationAustin.csv", index_col = 0)
    mongo.db.population.remove()

    ### Convert it to Json
    try:
        for column in population_df:
            records = json.loads(population_df[column].T.to_json(orient='index'))
            location = geolocator.geocode(column.strip().split()[0])
            # print(column.strip().split()[0])
            records = {
                        "place_id" : location.raw["place_id"],
                        "coordinates": [location.raw["lat"], location.raw["lon"]],
                        "place" : column.strip().split()[0], 
                        "type" : column.strip(),
                        "display_name" : location.raw["display_name"],
                        "boundingbox" : location.raw["boundingbox"],
                        "data":records
                        }
            #Insert only if place is not exist          
            if (mongo.db.population.find({"place_id": location.raw["place_id"]}).count() == 0):
                print(records)
                mongo.db.population.insert(records)
            else:
                print("updating")
            #     self.db_population.update({"place_id": records["place_id"]}, records, upsert=True)
    except Exception as e: print(e)
# ######################### population data #####################################
def retrive_population_data(mongo):
   ''' retriveds population data from mongodb and returns the result
       input: takes mongodb client
       return: mongodb cursor'''

   #sort = [('_id', -1)]
   result = mongo.db.population.find({}, {'_id': False})
   #print (result)
   if result.count():
       return result

   return None
# ################### housing data ######################
def retrive_housing_data(mongo):
   ''' retriveds population data from mongodb and returns the result
       input: takes mongodb client
       return: mongodb cursor'''

   #sort = [('_id', -1)]
   result = mongo.db.housing.find({ "ZipCode":  {"$gt": "78610","$lt" :"78759" } }, {'_id': False})
   if result.count():
       return result

   return None

# ############################################ school data #######################
#     . 
# retrive_elementary school_data
def retrive_elementary_data(mongo):
   ''' retriveds population data from mongodb and returns the result
       input: takes mongodb client
       return: mongodb cursor'''

   #sort = [('_id', -1)]
   result = mongo.db.elementary.find({}, {'_id': False})
   #print (result)
   if result.count():
       return result
   return None

#  high school data 

def retrive_highschool_data(mongo):
   ''' retriveds population data from mongodb and returns the result
       input: takes mongodb client
       return: mongodb cursor'''

   #sort = [('_id', -1)]
   result = mongo.db.highschool.find({}, {'_id': False})
   #print (result)
   if result.count():
       return result
   return None

#  middle school data 
def retrive_middleschool_data(mongo):
   ''' retriveds population data from mongodb and returns the result
       input: takes mongodb client
       return: mongodb cursor'''

   #sort = [('_id', -1)]
   result = mongo.db.middleschool.find({}, {'_id': False})
   #print (result)
   if result.count():
       return result
   return None




