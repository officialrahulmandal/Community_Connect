from django.contrib import admin
from .models import (
    User,
    SentMail,
    EmailDrafts
)

admin.site.register(User)
admin.site.register(SentMail)
admin.site.register(EmailDrafts)