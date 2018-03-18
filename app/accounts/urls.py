from django.urls import path
from django.contrib.auth.views import (
    login,
    logout,
    logout_then_login
)
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Registration
    path('register/',
         views.AccountRegistration.as_view(), name='register'),
    path('volunteer/register/',
         views.AccountVolunteerRegister.as_view(), name='multi-register'),
    path('multiple/register/',
         views.AccountVolunteerRegister.as_view(), name='multi-register'),
    path('reset/<uidb64>/<token>',
         views.AccountActivation.as_view(), name='reset'),
    # Accounts
    path('login/', login, {
        'redirect_authenticated_user': True,
        'template_name': 'accounts/forms.html',
        'extra_context': {
            "form_page_name": 'Login',
            "community": settings.COMMUNITY,
        }
    }, name='login'),
    path('logout/', logout, {
        'template_name': 'accounts/messages.html',
        'extra_context': {
            "msg_page_name": "Success",
            'message': 'You have logged out successfully.',
            "community": settings.COMMUNITY,
        }
    }, name='logout'),
    path('logout-then-login/', logout_then_login, {
        'extra_context': {
            "community": settings.COMMUNITY,
        }
    }, name='logout_then_login'),

]
