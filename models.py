""" 
yRelocate: This modules parces the csv file and insert it in MongoDb

"""

#imports
import os 
import pandas as pd
import numpy as np
import json
import pymongo
from geopy.geocoders import Nominatim



class yRelocateDB:

    def __init__(self):
        self.geolocator = Nominatim()

        #### Set base directory ##################################################
        self.basedir = os.path.abspath(os.path.dirname(__file__))

        ### Create MongoDb connection
        self.mng_client = pymongo.MongoClient('localhost', 27017)
        self.mng_db = self.mng_client['yRelocate_db'] 
        self.collection_name = 'population' 
        self.db_population = self.mng_db[self.collection_name]
        #self.db_population.remove()

    def insert_population_data(self):
        #### Read from the population CSV file #####################################
        population_df = pd.read_csv(self.basedir + "/static/resources/USTexasPoulationAustin.csv", index_col = 0)

        ### Convert it to Json
        for column in population_df:
            records = json.loads(population_df[column].T.to_json(orient='index'))
            location = self.geolocator.geocode(column.strip().split()[0])
            print(column.strip().split()[0])
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
            if (self.db_population.find({"place_id": location.raw["place_id"]}).count() == 0):
                print("inserting")
                self.db_population.insert(records)
            # else:
            #     print("updating")
            #     self.db_population.update({"place_id": records["place_id"]}, records, upsert=True)

    def retrive_population_data(self):
        """If found return latest all records.
        Returns nothing
        -------
        """
        #sort = [('_id', -1)]
        result = self.db_population.find({}, {'_id': False})
        #print (result)
        if result.count():
            return result

        return None


db = yRelocateDB()
#db.insert_population_data()
cursor =list(db.retrive_population_data())
for i in cursor:
    print(i['coordinates'])




