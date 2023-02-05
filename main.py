from bson import json_util
from flask import Flask
import sqlite3
import pandas as pd
from IPython.display import display
app = Flask(__name__)
import re
import pymongo
from pymongo import MongoClient
import flask
import json





def transformString(st):
    transform1 =  re.sub(r'\(.*\)', '', st)
    transform2 = re.sub(r',.*','',transform1)
    return transform2.replace(' - ','').replace('LIMITED', '').replace ('limited', '').replace('Limited', '').replace('LTD.', '').replace('LTD', '').lower().title()

@app.route('/insert_to_mongo')
def insert_into_mongo():
    connector = sqlite3.connect('semos_companies_data.db')
    df = pd.read_sql("SELECT * FROM companies", con=connector)
    df = df.drop(['name'], axis=1)
    client = MongoClient('localhost', 27017)
    db = client.semos_database
    collection = db.companies
    final_list = []
    for item in df.to_dict('records'):
        final_dct = {}
        key = item.pop('company_name_cleaned')
        final_dct[key] = item
        final_list.append(final_dct)

    collection.insert_many(final_list)
    return "Finished inserting into MongoDB database"

@app.route("/clear_data")
def clear_data():
    connector = sqlite3.connect('semos_companies_data.db')
    df = pd.read_sql("SELECT * FROM companies", con = connector)
    df['company_name_cleaned']= df['name'].apply(transformString)
    df.to_sql(name = 'companies',if_exists = 'replace',con = connector, index = False)
    return "Finished transforming the data and writing to SQL database"


@app.route('/show_data')
def show_mongo_results():
    client = MongoClient('localhost', 27017)
    db = client.semos_database
    collection = db.companies
    res_cursor = collection.find({}).limit(20)
    lst = []
    for item in res_cursor:
        lst.append(json.loads(json_util.dumps(item)))

    return lst


@app.route('/')
def home():
    return flask.render_template('main.html')




app.run(debug = True)