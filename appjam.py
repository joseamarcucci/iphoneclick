import streamlit as st
import os
import datetime
import gspread
import urllib.request
import pandas as pd

from flask import Flask

FRT = datetime.timezone(datetime.timedelta(hours=+2))

app = Flask(__name__)




def record_to_sheets_default(event):

    # Copy service account json file to local.
    if not os.path.isfile('service_account.json'):
        urllib.request.urlretrieve(<URL to JSON file of GCP service account key>,"service_account.json")
    
    # gspread client.
    client = gspread.service_account(filename='service_account.json')

    # Access target sheet.
    sheet = client.open("Record iPhone Click").sheet1

    # event record data frame.
    eve_df = pd.DataFrame({'event':[event + ' (from Heroku)'], 'time':[str(datetime.datetime.now(FRT))]})

    # Record event to target sheet.
    sheet.insert_rows(eve_df.values.tolist(),2)

country = st.text_input('evento')

@app.route("/feed-baby")
def record_to_sheets1():
    event = 'Feed baby'
    record_to_sheets_default(event)
    return event + " noted from Heroku!"

@app.route("/baby-wakes-up")
def record_to_sheets2():
    event = 'Baby wakes up'
    record_to_sheets_default(event)
    return event + " noted from Heroku!"
    
@app.route("/arrive-at-office")
def record_to_sheets3():
    event = 'Arrived at office'
    record_to_sheets_default(event)
    return event + " noted from Heroku!"
    
@app.route("/leave-office")
def record_to_sheets4():
    event = 'Left office'
    record_to_sheets_default(event)
    return event + " noted from Heroku!"
    
if __name__=="__main__":
    app.run()








