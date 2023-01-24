from flask import Flask
import sqlite3
import pandas as pd
from IPython.display import display
app = Flask(__name__)
import re
import pymongo
from pymongo import MongoClient
cluster = mongodb+srv://TamaraSokolovska:123Tam456@cluster0.jreinzo.mongodb.net/?retryWrites=true&w=majority
db = cluster["semos_companies_data"]





def transformString(st):
    transform1 =  re.sub(r'\(.*\)', '', st)
    transform2 = re.sub(r',.*','',transform1)
    return transform2.replace(' - ','').replace('LIMITED', '').replace ('limited', '').replace('Limited', '').replace('LTD.', '').replace('LTD', '').lower().title()
    return final_stringLTD

@app.route('/')
def home():
    connector = sqlite3.connect('semos_companies_data.db')
    df = pd.read_sql("SELECT * FROM companies", con = connector)
    #print(tabulate(df,headers = 'keys', tablefmt = 'psql'))
    df['name_cleaned']= df['name'].apply(transformString)
    display(df[['name_cleaned','name']])
    return 'asdasda'




app.run(debug = True)