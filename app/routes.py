from flask import Flask, jsonify, render_template, url_for
import json
from bson import json_util
# import flask   # import Flask, render_template
# # from bson.json_util import dumps
# from flask_pymongo import PyMongo

from app import app

# ########################################################################



# Define routes ###############################################################
@app.route("/")
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/population')
def population():
    print("---------------population-----------------")
    # Get the Data from mongodb
    projects = retrieve_population_data(app.mongo)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    return json_projects
    # return 'More to come!! - Population dump!'

# ###########################################################################
# ###########################################################################

if __name__ == '__main__':
    app.run(debug=True)

# insert_population_data(mongo)
