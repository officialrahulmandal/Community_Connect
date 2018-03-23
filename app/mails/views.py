from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SendMailForm
from django.contrib.sites.shortcuts import get_current_site
from django.views import View
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
                return redirect('\login')
        else:
            return redirect('\login')

    def post(self, request):
        if request.user.is_authenticated:
            is_admin = request.user.groups.filter(name='admin').exists()
            if is_admin:
                form = SendMailForm(request.POST)
                yield render(request, 'accounts/messages.html', {"msg_page_name": "Success", 'message': 'Your mail is send to users', "community": settings.COMMUNITY})
                if form.is_valid():
                    pass
                # Enter the logic to send mails Here
                else:
                    return render(request, 'accounts/messages.html', {"msg_page_name": "Failed", 'message': 'Could not send the mail', "community": settings.COMMUNITY})
            else:
                return redirect('\login')
        else:
            return redirect('\login')


# My Code to send mails. Ignore or delete if the sendmails part is done. - Ajay

# if form.is_valid():
#     recievers = []
#     message = cleaned_data.get('message')
#     mail_subject = cleaned_data.get('subject')
#     current_site = get_current_site(request)
    # message = render_to_string('mails/CreateMail.html', {
    #     'protocol': request.scheme,
    #     'message': message,
    #     "community": settings.COMMUNITY,
    #     'domain': current_site.domain,
    # })
#     for user in Users.objects.all():
#         recievers.append(user.email)
#     send_mail(subject, message, from_email, recievers)
