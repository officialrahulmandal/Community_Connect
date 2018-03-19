from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    COMMUNITY_CHOICES = (
        ('PYDELHI', 'PyDelhi'),
        ('ILUGD', 'ILUG-D')
    )
    channels_Subscribe = models.CharField(
        max_length=70, 
        choices=COMMUNITY_CHOICES, 
        default='PYDELHI'
    )
    administrator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SentMail(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    time = models.DateTimeField()
    sender = models.EmailField()
    open_counter = models.IntegerField()

    def __str__(self):
        return self.subject


class EmailDrafts(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    variable = models.CharField(max_length=255)
    timer = models.DateTimeField()

    def __str__(self):
        return self.subject
