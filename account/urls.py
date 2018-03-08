from django.conf.urls import url
#from django.contrib.auth.views import login
from . import views
urlpatterns = [
url(r'^login/$',views.user_login,name='login'),
]
