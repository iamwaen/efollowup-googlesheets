from __future__ import print_function

from googleapiclient.discovery import build
from google.oauth2 import service_account

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def home():
    SERVICE_ACCOUNT_FILE = 'credentials/key-sheets-api.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SPREADSHEET_ID = '1ry4S9dDev1K2cS4_yYXV_Gfx4_QSGJjDsnwaGoXbsCk'
    RANGE_NAME = 'Sheet1!A1:G'

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,  range=RANGE_NAME).execute()
    values = result.get('values')
       
    return render_template("index.html", len = len(values), listdata = values)

if __name__ == '__main__':
    app.run(debug=True)