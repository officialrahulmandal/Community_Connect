from django import forms
from django.contrib.auth.models import User


class SendMailForm(forms.Form):
    '''
    This form will take input to send mails.
    '''
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(
        attrs={'id': 'formTextAreaFormat'}))
