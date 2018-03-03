from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    # url for admin panel
    url(r'^admin/', admin.site.urls),
    # url pattern for homepage
    url(r'', include('homepage.urls')),
    #url pattern for signup
    url(r'^signup/',include('signup.urls')),
]
