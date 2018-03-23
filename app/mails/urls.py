from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('draft/', views.DraftMail.as_view(), name='draft'),
]
