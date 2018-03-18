from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('draft/', views.draft, name='draft'),

]
