import logging

from django.conf import settings
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

ACCOUNT_TWILIO = getattr(settings, "ACCOUNT_TWILIO", None)
TOKEN_TWILIO = getattr(settings, "TOKEN_TWILIO", None)
FROM_TWILIO = getattr(settings, "FROM_TWILIO", None)

SMS_COST = float(getattr(settings, "SMS_COST", '0.0075'))

logger = logging.getLogger(__name__)


def get_client():
    return TwilioRestClient(ACCOUNT_TWILIO, TOKEN_TWILIO)


def mass_sms(message, numbers):
    error_numbers = []
    for number in numbers:
        if '+' not in number:
            number = '+' + number
        try:
            get_client().messages.create(to=number, from_=FROM_TWILIO,
                                         body=message)
        except TwilioRestException as e:
            logger.error(e.msg)
            error_numbers += [number]

    cost = float((len(numbers)-len(error_numbers)))*SMS_COST

    return (error_numbers, cost)
