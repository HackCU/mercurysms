# MercurySMS
Dynamically extract phone numbers from a defined Google Sheets to send bulk messages with Twilio.

## Setup
Needs: Python 3.X

- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`



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


## Usage

### Create Google Sheets

Create a Google Sheets. Open to public for viewing.

### Add lists to Google Sheets

A list is a column in the mentioned Google Sheets. It is identified by each first row of a column. The rest of the rows must be the phone numbers.

### Send SMS to list

- Open root route. Ex: http://localhost:8000
- Login with user (you can login with the super user you created in your first steps)
- Send messages right away. Let's SPAM those users :D

### Add new users

- Login with admin user
- Enter admin interface. Ex: http://localhost:8000/admin
- Add new user there


## Future

- Add hability to receive SMS
- Answer SMS received individually
- Keep a log of all messages sent and to what numbers


----------------

Made with :heart: at HackCU
