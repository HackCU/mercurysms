<br>
<p align="center">
  <img alt="HackCU" src="https://github.com/hackcu/mercurysms/raw/master/hackculogo.png" width="200"/>
</p>
<br>

# MercurySMS
Dynamically extract phone numbers from a defined Google Sheets to send bulk messages with Twilio.

## Note

Your Twilio phone number can be blacklisted as spam by carriers if you're sending bulk SMS. Read this [FAQ](https://support.twilio.com/hc/en-us/articles/223181708-Can-my-Twilio-SMS-messages-be-blacklisted-as-spam-).
If you plan on sending bulk SMS on a regular basis, this is not the right software.
You should consider obtaining and using [short codes](https://www.twilio.com/sms/shortcodes) to avoid being blacklisted. They are also much faster than a normal Twilio phone number.
HackCU and its developers are not responsible if you are blacklisted while using this tool.

This was built for a hackathon and will be used only for about 2 days in a year to send notifications to participants (who are aware of this and voluntarily provided their phone numbers).
So, if your use case is similar, you shouldn't run into any issues of being blocked by carriers.

## Setup

Needs: Python 3.X

```shell
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Run server

### Local environment

Add 4 (2 optional) environment variables:

- **ACCOUNT_TWILIO**: Twilio account SID
- **TOKEN_TWILIO**: Twilio account SID
- **FROM_TWILIO**: Twilio phone number. **Needs to be able to send SMS to unverified numbers**
- **SHEETS_KEY**: Google Sheets key. Ex: https://docs.google.com/spreadsheets/d/**ajksdhalksdhalksdhlaksjawdlS83zL3I**/edit
- **SHEETS_GID**(optional): Tab that you want to extract from Google Sheets. Defaults to 0, first tab. You can find it on the URL. Ex: https://docs.google.com/spreadsheets/d/1Fo58xcUnCUN2-_1Rjua2lW6b85IDQ2gK9wdlS83zL3I/edit#**gid=0**
- **PROD**(optional): Run project on production mode. Any value will make it run as production mode.

Run server to 0.0.0.0
```shell
$ python manage.py runserver 0.0.0.0:8000
```

### Docker

In order to make deployment easier, there's an available built image.

Needs: docker

- Create a directory
- Copy `docker_run.sh` into the directory
- Create `env.list` file (you can use `env.list.template as a guide)`
- (Optional) Modify `docker_run.sh` to change the deployment port (default: 8000)
- Run `docker_run.sh`
- Login in the app as `admin` (password `admin`) and change the password for admin (and username too) from the admin console.
- Enjoy!

## Usage

### Create Google Sheets

Create a Google Sheets. Open to public for viewing.

### Add lists to Google Sheets

A list is a column in the mentioned Google Sheets. It is identified by each first row of a column. The rest of the rows must be the phone numbers.

### Send SMS to list

- Open root route. Ex: http://localhost:8000
- Login with user (you can login with the super user you created in your first steps)
- Send messages right away.

### Add new users

- Login with admin user
- Enter admin interface. Ex: http://localhost:8000/admin
- Add new user there


## Future

- [ ] Add ability to receive SMS
- [ ] Answer SMS received individually
- [ ] Keep a log of all messages sent and recipients


----------------

Made with :heart: at HackCU
