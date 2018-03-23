from django.contrib import admin
from .models import (
    User_Channel,
    SentMail,
    EmailDraft
)

admin.site.register(User_Channel)
admin.site.register(SentMail)
admin.site.register(EmailDraft)
