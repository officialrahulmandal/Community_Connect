from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class User_Channel(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE)
    CHANNELS_CHOICES = (
        ('nextevent', 'Next Event Update'),
        ('resources', 'Resources'),
        ('hire', 'Hiring and Pitching'),
        ('feedback', 'Feedback'),
        ('volunteer', 'Volunteers')
    )
    channels_Subscribe = MultiSelectField(
        max_length=70,
        choices=CHANNELS_CHOICES
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "User_Channels"


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
