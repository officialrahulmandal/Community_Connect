from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class UserExtended(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    CHANNELS_CHOICES = (
        ('nextevent', 'Next Event Update'),
        ('resources', 'Resources'),
        ('hire', 'Hiring and Pitching'),
        ('feedback', 'Feedback'),
        ('volunteer', 'Volunteers')
    )

    channels_Subscribe = MultiSelectField(
        max_length=70,
        choices=CHANNELS_CHOICES,
        blank=True,
        null=True
    )
    userKey = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "UserExtended"


class SentMail(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    time = models.DateTimeField()
    sender = models.EmailField()
    open_counter = models.IntegerField()

    def __str__(self):
        return self.subject


class EmailDraft(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    variable = models.CharField(max_length=255, null=True, blank=True)
    timer = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject
