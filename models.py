"""
yRelocate: This modules parces the csv file and insert it in MongoDb

"""
# from .app import mongo
# imports

import os
import pandas as pd
# import numpy as np
import json
# import pymongo
from geopy.geocoders import Nominatim

# from .app import mongo

# Set base directory ##################################################

basedir = os.path.abspath(os.path.dirname(__file__))

# collection_name = 'population'
# db_population = mongo['population']
# self.db_population.remove()


def insert_population_data(mongo):

    # Read from the population CSV file #####################################
    geolocator = Nominatim()
    population_df = pd.read_csv(basedir +
                                "/static/resources/USTexasPoulationAustin.csv",
                                index_col=0)
    mongo.db.population.remove()

    # Convert it to Json
    try:
        for column in population_df:
            records = json.loads(population_df[column].T
                                 .to_json(orient='index'))
            location = geolocator.geocode(column.strip().split()[0])
            # print(column.strip().split()[0])
            records = {
                        "place_id": location.raw["place_id"],
                        "coordinates": [location.raw["lat"],
                                        location.raw["lon"]],
                        "place": column.strip().split()[0],
                        "type": column.strip(),
                        "display_name": location.raw["display_name"],
                        "boundingbox": location.raw["boundingbox"],
                        "data": records
                        }
            # Insert only if place is not exist
            if (mongo.db.population
                        .find({"place_id": location.raw["place_id"]})
                        .count() == 0):
                print(records)
                mongo.db.population.insert(records)
            else:
                print("updating")
            # self.db_population.update({"place_id": records["place_id"]},
            # records, upsert=True)
    except Exception as e:
        print(e)


def retrive_population_data(mongo):
    """"If found return latest all records.
    Returns nothing
    -------
    """
    # sort = [('_id', -1)]
    db_population = mongo['population']
    result = db_population.find({}, {'_id': False})
    # print (result)
    if result.count():
        return result

    return None

# insert_population_data()
# cursor =list(db.retrive_population_data())
# for i in cursor:
#     print(i['coordinates'])
