from django.conf.urls import url
from . import views
urlpatterns=[
#homepage url for Community Connect that redirects to homepage_detail view
url(r'^$',views.homepage_details,name='homepage_detail'),
]
