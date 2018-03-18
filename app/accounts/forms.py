from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    '''
    This form will help users login.
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ResetPassword(forms.Form):
    '''
    This form will help users reset their password.
    '''
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(
        label="Repeat Password", widget=forms.PasswordInput)

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] is None:
            raise forms.ValidationError('Enter a password.')
        elif cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        elif cd['password'] == cd['repeat_password']:
            return cd['repeat_password']
        else:
            raise forms.ValidationError(
                'Unknown Error! Please report to developers.')


class UserRegistrationForm(forms.ModelForm):
    '''
    This form will help in registration of new users.
    '''
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(
        label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError('Username can\'t be Null.')
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Email can\'t be Null.')
        else:
            return email

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] is None:
            return cd['repeat_password']
        elif cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Password don\'t match.')
        elif cd['password'] == cd['repeat_password']:
            return cd['repeat_password']
        else:
            raise forms.ValidationError(
                'Unknown Error! Please report to developers.')


class VolunteerUserRegistrationForm(forms.ModelForm):
    '''
    This form will help in registration of new users when the registration is done by a volunteer.
    '''
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError('Username can\'t be Null.')
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Email can\'t be Null.')
        else:
            return email
