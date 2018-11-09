import os
from flask import Flask, jsonify, render_template, url_for
from models import yRelocateDB
import json
from bson import json_util
from bson.json_util import dumps



##############################################################################

app = Flask(__name__)

##### Define routes #####################################################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/population")   
def population():
    print("---------------population-----------------")
    # Get the Data from MongoDc
    db = yRelocateDB()
    projects = db.retrive_population_data()
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    return json_projects    


################################################################################
################################################################################
if __name__ == '__main__':
    app.run(debug=True)    