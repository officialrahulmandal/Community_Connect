from django.db import models
from django.contrib.auth.models import User

class Options(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return self.key

class Statistics(models.Model):
    key = models.CharField(max_length=255)
    counter = models.IntegerField()
    types = models.CharField(max_length=255)
    
    def __str__(self):
        return self.key


class Logs(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    types = models.CharField(max_length=255)
    
    def __str__(self):
        return self.key


class Content(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    types = models.CharField(max_length=255)
    date_added = models.DateField()
    
    def __str__(self):
        return self.title


class ContentMeta(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    content_id = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return self.key


class EmailGroups(models.Model):
    group_name = models.CharField(max_length=255)
    label = models.TextField()

    def __str__(self):
        return self.group_name


class EmailSchedules(models.Model):
    content_id = models.ForeignKey('Content', on_delete=models.CASCADE)
    email_group = models.ForeignKey('EmailGroups', on_delete=models.CASCADE)
    schedule_time = models.DateField()
    status = models.IntegerField()


class EmailRelations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('EmailGroups', on_delete=models.CASCADE)