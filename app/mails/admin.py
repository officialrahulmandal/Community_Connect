from django.contrib import admin
from .models import (
    UserExtended,
    SentMail,
    EmailDraft
)

admin.site.register(UserExtended)
admin.site.register(SentMail)
admin.site.register(EmailDraft)
