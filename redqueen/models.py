from django.db import models
from django.utils import timezone


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=200, default='undefined')
    sex = models.CharField(max_length=10, default='man')
    role = models.CharField(max_length=30, default='father')
    phone = models.CharField(max_length=11, default='0124567890')
    photo = models.FileField(upload_to='humans/', default=None, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.role)

class Message (models.Model):
    channel = models.CharField(max_length=200, default='System\Diags')
    signal = models.TextField()
    published = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.channel, self.signal, self.published)

class Device(models.Model):
    name = models.CharField(max_length=200, default='untitled')
    channel = models.CharField(max_length=200, default='System\Diags')
    value = models.CharField(max_length=200, default='None')
    group = models.CharField(max_length=200, default='System')
    action = models.CharField(max_length=10, default='GET')

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name, self.group, self.channel)

class Rule(models.Model):
    name = models.CharField(max_length=200, default='untitled')
    group = models.CharField(max_length=200, default='System')
    action = models.CharField(max_length=200, default='None')
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(default=timezone.now)
    repeat = models.CharField(max_length=200, default='no')

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name, self.group, self.action)