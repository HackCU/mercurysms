from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from sheets2sms import sheets
from sheets2sms import twilio
from sheets2sms.forms import SendSMSForm

SHEETS_KEY = getattr(settings, "SHEETS_KEY", None)
SHEETS_GID = getattr(settings, "SHEETS_GID", None)


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
        err_nums, cost = twilio.mass_sms(message, list(numbers))
        url = reverse('sms_sent') + '?q=1'
        if err_nums:
            url += '&nums=' + ','.join(err_nums)
        if cost:
            url += '&cost=' + str(cost)
        return redirect(url)


@login_required
def succesfully_sent(request):
    nums = request.GET.get('nums', None)
    cost = request.GET.get('cost', 0.0)
    context = {'nums': nums, 'cost': cost}
    return render(request, 'sms_sent.html', context=context)
