from django.urls import path
from django.contrib.auth.views import login, logout, logout_then_login,password_change,password_change_done
from . import views
from django.conf import settings

urlpatterns = [
# views/accounts/
path('',views.dashboard, name='dashboard'),
path('register/', views.register, name='register'),
# views/registration
path('login/', login, { 'extra_context': { "community": settings.COMMUNITY,} }, name='login'),
path('logout/', logout, { 'extra_context': { "community": settings.COMMUNITY,} }, name='logout'),
path('logout-then-login/', logout_then_login, { 'extra_context': { "community": settings.COMMUNITY,} }, name='logout_then_login'),
path('password-change/', password_change, { 'extra_context': { "community": settings.COMMUNITY,} }, name="password_change"),
path('password-change/done/', password_change_done, { 'extra_context': { "community": settings.COMMUNITY,} }, name="password_change_done"),
]
