import json
import logging

from django.conf import settings
from twilio.rest import Client

ACCOUNT_TWILIO = getattr(settings, "ACCOUNT_TWILIO", None)
TWILIO_SERVICE_ID = getattr(settings, "TWILIO_SERVICE_ID", None)
TOKEN_TWILIO = getattr(settings, "TOKEN_TWILIO", None)
FROM_TWILIO = getattr(settings, "FROM_TWILIO", None)


logger = logging.getLogger(__name__)


def get_client():
    return Client(ACCOUNT_TWILIO, TOKEN_TWILIO)


def parse_num(num):
    num = num.replace('-', '').strip()
    if '+' not in num:
        num = '+1' + num
    return num


def new_mass_sms(message, numbers):
    bindings = [json.dumps({'binding_type': 'sms', 'address': parse_num(num)}) for i, num in enumerate(numbers) if num]
    notification = get_client().notify.services(TWILIO_SERVICE_ID) \
        .notifications.create(
        to_binding=bindings,
        body=message)
    print(notification)
