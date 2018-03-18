from django.contrib import admin
from .models import (
    Options,
    Statistics,
    Logs,
    Content,
    ContentMeta,
    EmailGroups,
    EmailSchedules,
    EmailRelations
)

admin.site.register(Options)
admin.site.register(Statistics)
admin.site.register(Logs)
admin.site.register(Content)
admin.site.register(ContentMeta)
admin.site.register(EmailGroups)
admin.site.register(EmailSchedules)
admin.site.register(EmailRelations)


