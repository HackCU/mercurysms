from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from mercurysms import sheets
from mercurysms import twilio
from mercurysms import worker
from mercurysms.forms import SendSMSForm

SHEETS_KEY = getattr(settings, "SHEETS_KEY", None)
SHEETS_GID = getattr(settings, "SHEETS_GID", None)

bg_worker = worker.Worker()

class SendSMSView(LoginRequiredMixin, TemplateView):
    template_name = 'sendSMS.html'

    def __init__(self):
        super(SendSMSView, self).__init__()
        self.sheet = sheets.Sheet(SHEETS_KEY, SHEETS_GID)
        bg_worker = worker.Worker()

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
        bg_worker.start_process(message, list(numbers))
        return redirect('sending')


@login_required
def succesfully_sent(request):
    nums = bg_worker.err_nums
    cost = bg_worker.cost
    bg_worker.reset()
    context = {'nums': nums, 'cost': cost}
    return render(request, 'sms_sent.html', context=context)


@login_required
def sending(request):
    return render(request, 'sending.html')


def status(request):
    data = { 'finished': bg_worker.done }
    return JsonResponse(data)
