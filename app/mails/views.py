from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View


def admin_panel(request):
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='admin').exists()
        return render(request, 'mails/admin_panel.html', {'is_admin': is_admin, "community": settings.COMMUNITY})
    else:
        return render(request, 'index.html')


def draft(request):
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='admin').exists()
        return render(request, 'mails/draft.html', {'is_admin': is_admin, "community": settings.COMMUNITY})
    else:
        return render(request, 'index.html')
