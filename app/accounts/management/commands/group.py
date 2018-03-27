'''
Automatic registration of admin group and adding all the
superusers to group `admin`. However, this code can be 
used only after the application's migrations have been made.
'''
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from mails.models import (
    UserExtended,
    SentMail,
    EmailDraft
)
from django.contrib.auth.models import (
    Group,
    Permission
)


class Command(BaseCommand):
    help = "This command will register a new group called `admin` give it permission to portal.models and all all superusers to the group"

    def handle(self, *args, **options):

        admin, created = Group.objects.get_or_create(name='admin')
        # Code to add permission to group
        userExtendedModel = ContentType.objects.get(model='userextended').pk
        sentMailModel = ContentType.objects.get(model='sentmail').pk
        emailDraftModel = ContentType.objects.get(model='emaildraft').pk
        allPermissions = Permission.objects.filter(content_type_id__in=[
            userExtendedModel, sentMailModel, emailDraftModel])
        for permission in allPermissions:
            admin.permissions.add(permission)

        superUserslist = User.objects.filter(is_superuser=1)

        for superuser in superUserslist:
            admin.user_set.add(superuser)
        print("Success! All superusers have access to the admin panel now!")
