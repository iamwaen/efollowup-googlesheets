# efollowup-googlesheets

### Setup project
  - **Create Sheets API**
    - Link Python Quickstart https://developers.google.com/sheets/api/quickstart/python#prerequisites
    - Download Service account key
    - Create folder credentials -> copy Service account key and paste it to folder credentials
  - **Prepare environment**
    - `pip install virtualenv`
    - `virtualenv venv`
    - `venv/scripts/activate`
  - **Install package (make sure you have activated venv)**
    - `pip install -r requirements.txt`
  - **Change Variables**
    - SERVICE_ACCOUNT_FILE
    - SPREADSHEET_ID
    - RANGE_NAME
  - **Run app**
    - py app.py