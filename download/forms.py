from django import forms
from .models import Request


class RequestForm(forms.Form):
    email = forms.EmailField(max_length=100)
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')

    class Meta:
        model = Request
        fields = [
            'email'
            'url'
        ]
