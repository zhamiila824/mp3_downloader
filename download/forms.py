from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    email = forms.EmailField(label="Email: ")
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')

    class Meta:
        model = Request
        exclude = ['email', 'url']
