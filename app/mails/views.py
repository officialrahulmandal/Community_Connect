from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from mails.forms import SendMailForm
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from mails.models import UserExtended
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .tasks import send

class DraftMail(View):
    '''
    This view is where the user drafts the mail and it is send to the users.
    '''

    def get(self, request):
        if request.user.is_authenticated:
            is_admin = request.user.groups.filter(name='admin').exists()
            if is_admin:
                form = SendMailForm()
                return render(request, 'mails/draft.html', {'form': form, 'is_admin': is_admin, "community": settings.COMMUNITY})
            else:
                return redirect('login')
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            is_admin = request.user.groups.filter(name='admin').exists()
            if is_admin:
                self.sendAllMails(request)
                return render(request, 'accounts/messages.html', {"msg_page_name": "Success", 'message': 'Your Mails have successfully been send.', "community": settings.COMMUNITY})
            else:
                return redirect('login')
        else:
            return redirect('login')

    def sendAllMails(self, request):
        form = SendMailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('body')
            current_site = get_current_site(request)
            send.delay(subject, message)
        else:
            raise('Error While sending mails, form not valid.')
