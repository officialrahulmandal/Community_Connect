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
            for user in User.objects.filter(is_superuser=0):
                finalMessage = render_to_string('mails/CreateMail.html', {
                    'protocol': request.scheme,
                    'message': message,
                    'username': user.username,
                    'unsubscribe': UserExtended.objects.get(user=user).userKey,
                    "community": settings.COMMUNITY,
                    'domain': current_site.domain,
                })
                try:
                    email = EmailMessage(
                        subject, finalMessage, to=[user.email])
                    email.send()
                except:
                    # This needs to be changed, instead of raise we want to use logging.
                    raise('Check Email Setup, something might be wrong')
        else:
            raise('Error While sending mails, form not valid.')
