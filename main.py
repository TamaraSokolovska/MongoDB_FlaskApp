from flask import Flask
import sqlite3
import pandas as pd
from IPython.display import display
app = Flask(__name__)
import re
import pymongo
from pymongo import MongoClient






def transformString(st):
    transform1 =  re.sub(r'\(.*\)', '', st)
    transform2 = re.sub(r',.*','',transform1)
    return transform2.replace(' - ','').replace('LIMITED', '').replace ('limited', '').replace('Limited', '').replace('LTD.', '').replace('LTD', '').lower().title()

@app.route('/')
def home():
    connector = sqlite3.connect('semos_companies_data.db')
    df = pd.read_sql("SELECT * FROM companies", con = connector)
    df['company_name_cleaned']= df['name'].apply(transformString)
    display(df[['company_name_cleaned','name']])
    #df.to_sql(name = 'companies',if_exists = 'replace',con = connector)
    client = MongoClient('localhost', 27017)
    db = client.semos_database
    collection = db.companies
    collection.insert_many(df.to_dict('records'))
    return "stignav"




app.run(debug = True)