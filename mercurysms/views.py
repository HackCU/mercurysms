from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.http import urlencode
from django.views.generic import TemplateView

from mercurysms import sheets
from mercurysms import twilio
from mercurysms.forms import SendSMSForm

SHEETS_KEY = getattr(settings, "SHEETS_KEY", None)
SHEETS_GID = getattr(settings, "SHEETS_GID", None)
SMS_COST = float(getattr(settings, "SMS_COST", '0.0075'))


def custom_redirect(url_name, *args, **kwargs):
    from django.core.urlresolvers import reverse
    url = reverse(url_name, args=args)
    params = urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)


class SendSMSView(LoginRequiredMixin, TemplateView):
    template_name = 'sendSMS.html'

    def __init__(self):
        super(SendSMSView, self).__init__()
        self.sheet = sheets.Sheet(SHEETS_KEY, SHEETS_GID)

    def get_context_data(self, **kwargs):
        con = super(SendSMSView, self).get_context_data(**kwargs)
        lists = self.sheet.lists
        con.update({'form': SendSMSForm(lists), 'lists': lists,
                    'sheets_url': sheets.SHEETS_URL.format(key=SHEETS_KEY, gid=SHEETS_GID)})
        return con

    def post(self, request, *args, **kwargs):
        lists = request.POST.getlist('lists')
        numbers = set()
        for list_ in lists:
            numbers = numbers.union(set(self.sheet.get_list(list_)))
        message = request.POST.get('message')
        twilio.new_mass_sms(message, numbers)
        return custom_redirect('sms_sent', nums=len(numbers), cost=len(numbers) * SMS_COST)


@login_required
def succesfully_sent(request):
    context = {'nums': request.GET.get('nums'), 'cost': request.GET.get('cost')}
    return render(request, 'sms_sent.html', context=context)
