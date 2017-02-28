from django import forms
from django.forms import Form


class SendSMSForm(Form):
    message = forms.CharField(max_length=60, required=True)

    def __init__(self, lists, *args, **kwargs):
        super(SendSMSForm, self).__init__(*args, **kwargs)
        self.fields['list'] = forms.ChoiceField(
            required=True,
            choices=[(l, str(l)) for l in lists]
        )
