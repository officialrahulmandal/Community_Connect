from django.urls import path
from django.contrib.auth.views import (
    login,
    logout,
    logout_then_login,
    password_change,
    password_change_done
)
from . import views
from django.conf import settings

urlpatterns = [
# views/accounts/
path('',views.dashboard, name='dashboard'),
path('register/', views.AccountRegistration.as_view(), name='register'),
path('reset/<uidb64>/<token>',views.AccountActivation.as_view(), name='reset'),
# views/registration/
path('login/', login, {
        'template_name': 'accounts/forms.html',
        'extra_context': {
            "form_page_name":'Login',
            "community": settings.COMMUNITY,
        }
    }, name='login'),
path('logout/', logout, {
        'template_name': 'accounts/messages.html',
        'extra_context': {
            "msg_page_name": "Success",
            'message': 'We have send you a mail to activate your account.',
            "community": settings.COMMUNITY,
        }
    }, name='logout'),
path('logout-then-login/', logout_then_login, {
        'extra_context': {
            "community": settings.COMMUNITY,
        }
    }, name='logout_then_login'),

]
