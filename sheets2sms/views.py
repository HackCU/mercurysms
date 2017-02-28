from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from sheets2sms import sheets
from sheets2sms import twilio
from sheets2sms.forms import SendSMSForm

SHEETS_KEY = getattr(settings, "SHEETS_KEY", None)
SHEETS_GID = getattr(settings, "SHEETS_GID", None)

sheet = sheets.Sheet(SHEETS_KEY, SHEETS_GID)


class SendSMSView(LoginRequiredMixin,TemplateView):
    template_name = 'sendSMS.html'

    def get_context_data(self, **kwargs):
        con = super(SendSMSView, self).get_context_data(**kwargs)
        lists = sheet.lists
        con.update({'form': SendSMSForm(lists), 'sheets_key': SHEETS_KEY})
        return con

    def post(self, request, *args, **kwargs):
        list = request.POST.get('list')
        numbers = sheet.get_list(list)
        message = request.POST.get('message')
        twilio.mass_sms(message, numbers)
        return redirect('send_form')
