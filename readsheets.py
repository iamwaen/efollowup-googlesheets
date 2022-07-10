from __future__ import print_function

from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'credentials/key-sheets-api.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1MNuPdQ1NwTOGRiW3pOZQ_2tO_XYIldrc2iyCz_2wmnA'
RANGE_NAME = 'Summary_Result!A1:M'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

SPREADSHEET_ID2 = '1fE0B7jRrV0gpr2EN5l3Cdc2PAmR-P0OYQ6gwkueAl28'
RANGE_NAME2 = 'Summary_Result!A2:M'
service2 = build('sheets', 'v4', credentials=creds)
sheet2 = service2.spreadsheets()
result2 = sheet2.values().get(spreadsheetId=SPREADSHEET_ID2,
                              range=RANGE_NAME2).execute()
values2 = result2.get('values', [])

values.extend(values2)

print(values)
# print(values2)
