""" 
yRelocate: This modules parces the csv file and insert it in MongoDb

"""
# from .app import mongo
#imports
import os 
import pandas as pd
import numpy as np
import json
# import pymongo
from geopy.geocoders import Nominatim
import time
from bson.objectid import ObjectId

# from .app import mongo

#### Set base directory ##################################################
basedir = os.path.abspath(os.path.dirname(__file__))

# collection_name = 'population' 
# db_population = mongo['population']
#self.db_population.remove()

def insert_population_data(mongo):
    ''' reads the population data from CSV and inserts
        it in mongodb 
        input: takes mongodb client '''
    #### Read from the population CSV file #####################################
    geolocator = Nominatim(user_agent="yRelocate")
    population_df = pd.read_csv(basedir + "/static/resources/USTexasPoulationAustin.csv", index_col = 0)
    population_df[['Texas', 'US','Austin']] = population_df[['Texas', 'US','Austin']].astype(str)
    mongo.db.population.remove()

    ### Convert it to Json
    try:
        for index, column in population_df.iteritems():
            # data = json.loads(pd.DataFrame({'year':column.index, 'population':column.values}).T.to_json(orient='index'))
            d = pd.DataFrame({'Year':column.index, 'population': column.values}).to_dict('records')
            print(d)
            location = geolocator.geocode(index)
            # print(column.strip().split()[0])
            records = {
                        "place_id" : location.raw["place_id"],
                        "coordinates": [location.raw["lat"], location.raw["lon"]],
                        "place" : index, 
                        "display_name" : location.raw["display_name"],
                        "boundingbox" : location.raw["boundingbox"],
                        "data": d
                        }
            #Insert only if place is not exist          
            if (mongo.db.population.find({"place_id": location.raw["place_id"]}).count() == 0):
                #print(records)
                mongo.db.population.insert(records)
            else:
                print("updating")
            #     self.db_population.update({"place_id": records["place_id"]}, records, upsert=True)
    except Exception as e: print(e)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def insert_home_rental_data(mongo):
    ''' reads the home and rental data from CSV and inserts
        it in mongodb 
        input: takes mongodb client '''
    # mongo.db.housing.remove()

    # Define geolocator to get lat long
    geolocator = Nominatim(user_agent="yRelocate")

    # get housing data
    df = pd.read_csv(basedir + "/static/resources/zip_singlefamily_home.csv", index_col = 0)
    home_df = pd.DataFrame()
    # Filter the colums
    home_df[['ZipCode','City', 'State', 'Metro', 'CountyName', 'AveHomePrice']] = df[ ['RegionName','City', 'State', 'Metro', 'CountyName', '2018-09']]

    # Get the rental data
    df = pd.read_csv("./static/resources/Zip_MedianRentalPrice_1Bedroom.csv", index_col = 0)
    rental_df = pd.DataFrame()
    rental_df[['City', 'State', 'Metro', 'CountyName', 'AveRentPrice']] = df[ ['City', 'State', 'Metro', 'CountyName', '2018-09']]    
    rental_df['ZipCode'] = rental_df.index

    # Merge the data 
    housing_df = home_df.merge(rental_df[['ZipCode', 'AveRentPrice']], left_on='ZipCode', right_on='ZipCode', how='left')

    #Search only for Austin
    housing_df = housing_df[housing_df['ZipCode'] > 70000]

    print(housing_df.head())
    ## Convert it to Json
    for index, row in housing_df.iterrows():
        # print(row['ZipCode'])
        zipCode = str(row['ZipCode']).zfill(5)
        print(f"{zipCode}")
        if (mongo.db.housing.find({"ZipCode": zipCode}).count() == 0):
            print(f"Not Found {zipCode}")
            try:
                location = geolocator.geocode(zipCode)
            except TimeoutError:
                return False
            except:
               return False 

            # # print(column.strip().split()[0])
            if (location):
                record = {
                            "place_id" : location.raw["place_id"],
                            "ZipCode": zipCode,
                            "coordinates": [location.raw["lat"], location.raw["lon"]],
                            "Address" : [row['City'], row['State']],
                            "CountyName" : row['CountyName'],
                            "display_name" : location.raw["display_name"],
                            "boundingbox" : location.raw["boundingbox"],
                            "AveHomePrice":row['AveHomePrice'],
                            "AveRentPrice":row['AveRentPrice']                   
                            }
                # mongo.db.housing.update( {"place_id": location.raw["place_id"]}, {'$set':{record}}, {'upsert': True} )
                if (mongo.db.housing.find({"place_id": location.raw["place_id"]}).count() == 0):
                    print(f"Inserting {zipCode}")
                    mongo.db.housing.insert(record)
    return False

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def insert_school_data(filename, collection):
    ''' reads the home and rental data from CSV and inserts
        it in mongodb 
        input: takes mongodb client '''
    # collection.remove()

    # Define geolocator to get lat long
    geolocator = Nominatim(user_agent="yRelocate")

    # get housing data
    df = pd.read_csv(basedir + "/static/resources/" + filename, index_col = 0)
    school_df = pd.DataFrame()
    # Filter the colums
    school_df = df[['Campus Name', 'District', 'County', 'Grade Range', 'Charter?', 'Magnet?', 'C@R Grade', 'State Rank', 'Regional Rank']]


    print(school_df.head())
    ## Convert it to Json
    for index, row in school_df.iterrows():
        # print(f"{row['Campus Name']}  {row['County']}")
        if (collection.find({"campusid": index}).count() == 0):
            # print(f"Not Found {row['Campus Name']}")
            try:
                location = geolocator.geocode(f"{row['Campus Name']}")
            except TimeoutError:
                return False

            # # print(column.strip().split()[0])
            if (location):
                print(f"found {row['Campus Name']}")
                record = {
                            "place_id" : location.raw["place_id"],
                            "ZipCode": location.raw['display_name'].split(", ")[-2],
                            "campusid": index,
                            "coordinates": [location.raw["lat"], location.raw["lon"]],
                            "CountyName" : row['County'],
                            "display_name" : location.raw["display_name"],
                            "boundingbox" : location.raw["boundingbox"],
                            "Grade_Range":row['Grade Range'],
                            "Charter":row['Charter?'],
                            "Magnet":row['Magnet?'],  
                            "CaR_Grade":row['C@R Grade'],
                            "state_Rank":row['State Rank'],      
                            "reginal_rank":row['Regional Rank']                                                                                                      
                            }
                # mongo.db.housing.update( {"place_id": location.raw["place_id"]}, {'$set':{record}}, {'upsert': True} )
                if (collection.find({"place_id": location.raw["place_id"]}).count() == 0):
                    print(f"Inserting {location.raw['display_name']}")
                    collection.insert(record)
            else:
                print(f"Not found {row['Campus Name']}")
    return True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# insert_population_data()
# cursor =list(db.retrive_population_data())
# for i in cursor:
#     print(i['coordinates'])




