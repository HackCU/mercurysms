# sheet2sms
Dynamically extract phone numbers from a defined GSheets to send bulk messages with Twilio.

## Setup
Needs: Python 3.X

- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`

### Create Google Sheets

Create a Google Sheets and make it available to anyone.

## Run server

### Local environment

Add 4 (1 optional) environment variables:

- **ACCOUNT_TWILIO**: Twilio account SID
- **TOKEN_TWILIO**: Twilio account SID
- **FROM_TWILIO**: Twilio phone number. **Needs to be able to send SMS to unverified numbers**
- **SHEETS_KEY**: Google Sheets key. Ex: https://docs.google.com/spreadsheets/d/**ajksdhalksdhalksdhlaksjawdlS83zL3I**/edit
- **SHEETS_GID**(optional): Tab that you want to extract from Google Sheets. Defaults to 0, first tab. You can find it on the URL. Ex: https://docs.google.com/spreadsheets/d/1Fo58xcUnCUN2-_1Rjua2lW6b85IDQ2gK9wdlS83zL3I/edit#**gid=0** 


Run server to 0.0.0.0
`python manage.py runserver 0.0.0.0:8000`

