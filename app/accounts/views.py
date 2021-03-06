# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views import View
from mails.models import SentMail, UserExtended
import random
import string
from accounts.forms import (
    LoginForm,
    UserRegistrationForm,
    ResetPassword,
    VolunteerUserRegistrationForm,
    UserEditProfileForm
)


def dashboard(request):
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='admin').exists()
        sentMails = (SentMail.objects.order_by('-time')[:10]).values()
        return render(request, 'accounts/dashboard.html', {'mails': sentMails, 'is_admin': is_admin, "community": settings.COMMUNITY})
    else:
        return redirect('login')


def request_reset_password(request):
    if request.user.is_authenticated:
        user = request.user
        return redirect('reset',
                        str(urlsafe_base64_encode(
                            force_bytes(request.user.pk)), 'utf-8'),
                        account_activation_token.make_token(user)
                        )
    else:
        return redirect('login')


class EditProfile(View):
    '''
    If user decides to edit some information of his/her account,
    the control is transfered to this function.
    '''

    def get(self, request):
        if request.user.is_authenticated:
            is_admin = request.user.groups.filter(name='admin').exists()
            form = UserEditProfileForm(user=request.user)
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Edit Information',
                'form': form,
                'is_admin': is_admin,
                "form_page_name": 'Edit Profile',
                "community": settings.COMMUNITY})
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            is_admin = request.user.groups.filter(name='admin').exists()
            form = UserEditProfileForm(request.POST, user=request.user)
            if form.is_valid():
                cd = form.cleaned_data
                User.objects.filter(pk=request.user.pk).update(
                    username=cd['username'], email=cd['email'], first_name=cd['first_name'], last_name=cd['last_name'])
                form = UserEditProfileForm(user=request.user)
                return redirect('dashboard')
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Edit Profile',
                'form': form,
                'is_admin': is_admin,
                "form_page_name": 'Edit Profile',
                "community": settings.COMMUNITY})
        else:
            return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form,
            "form_page_name": 'Login',
            "community": settings.COMMUNITY})


class AccountActivation(View):
    '''
    AccountActivation class used for activating new user's account.
    Once a user clicks on the link from their email. It gives them an oppertunity to set their password.
    '''

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            form = ResetPassword()
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Activate Account',
                'form': form,
                "form_page_name": 'Set Password',
                "community": settings.COMMUNITY})
        else:
            return render(request, 'accounts/messages.html', {"msg_page_name": "Failed", 'message': 'Link is invalid!', "community": settings.COMMUNITY})

    def post(self, request, uidb64, token):
        form = ResetPassword(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(password=cd['password'])
            try:
                uid = force_text(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'accounts/messages.html', {"msg_page_name": "Failed", 'message': 'Link is invalid!', "community": settings.COMMUNITY})
        else:
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Activate Account',
                'form': form,
                "form_page_name": 'Set Password',
                "community": settings.COMMUNITY})


class AccountRegistration(View):
    '''
    AccountRegistration class used for registration of new users.
    It sends an email containing set password instructions to user if the form data is valid in post request.
    '''

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/forms.html', {
            'form_btn_name': 'Register',
            'form': form,
            "form_page_name": 'Sign-Up',
            "community": settings.COMMUNITY})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            userKey = ''.join(random.choice(string.ascii_uppercase +
                                            string.ascii_lowercase + string.digits) for _ in range(25))
            UserExtendedSave = UserExtended(
                user=user, userKey=userKey)
            UserExtendedSave.save()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Create Account',
                'form': form,
                "form_page_name": 'Sign Up',
                "community": settings.COMMUNITY})


class AccountVolunteerRegister(View):
    '''
    AccountRegistration class used for registration of new users.
    It sends an email containing set password instructions to user if the form data is valid in post request.
    '''

    def get(self, request):
        form = VolunteerUserRegistrationForm()
        return render(request, 'accounts/forms.html', {
            'form_btn_name': 'Create Account',
            'form_btn_name': 'Edit Information',
            'form': form, "form_page_name": 'Sign-Up',
            "community": settings.COMMUNITY})

    def post(self, request):
        form = VolunteerUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(User.objects.make_random_password())
            user.is_active = False
            user.save()
            userKey = ''.join(random.choice(string.ascii_uppercase +
                                            string.ascii_lowercase + string.digits) for _ in range(25))
            UserExtendedSave = UserExtended(
                user=user, userKey=userKey)
            UserExtendedSave.save()
            current_site = get_current_site(request)
            mail_subject = '[PyDelhi] Please activate your account.'
            message = render_to_string('accounts/activate.html', {
                'protocol': request.scheme,
                'user': user,
                'domain': current_site.domain,
                'uid': str(urlsafe_base64_encode(force_bytes(user.pk)), 'utf-8'),
                'token': account_activation_token.make_token(user),
                "community": settings.COMMUNITY,
                "unsubscribe": userKey,
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            form = VolunteerUserRegistrationForm()
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Create Account',
                'form': form,
                "form_page_name": 'Sign-Up',
                "community": settings.COMMUNITY})
        else:
            return render(request, 'accounts/forms.html', {
                'form_btn_name': 'Create Account',
                'form': form,
                "form_page_name": 'Sign Up',
                "community": settings.COMMUNITY})


def unsubscribe(request, username, unsubscribe):
    try:
        user = UserExtended.objects.get(user__username=username)
    except UserExtended.DoesNotExist:
        return render(request, 'accounts/messages.html', {"msg_page_name": "Failed", 'message': 'You are already unsubscribed, If you think this is an error, please contact the community volunteers.', "community": settings.COMMUNITY})
    if unsubscribe == user.userKey:
        User.objects.filter(pk=user.user.pk).delete()
        return render(request, 'accounts/messages.html', {"msg_page_name": "Success", 'message': 'You have unsubscribed, if you wish to subscribe again, please sign-up again.', "community": settings.COMMUNITY})
    else:
        return render(request, 'accounts/messages.html', {"msg_page_name": "Failed", 'message': 'Incorrect unsubscribe Key!', "community": settings.COMMUNITY})


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html', {"community": settings.COMMUNITY})
