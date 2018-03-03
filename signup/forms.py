from django import forms
from .models import user_details
class SignupForm(forms.ModelForm):
    class Meta:
        model=user_details
        fields=('name','email','password',)
