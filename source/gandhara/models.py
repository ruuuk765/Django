from django.db import models
from django.utils import timezone

class Job(models.Model):
    name = models.CharField(max_length=64, blank=True, null=False, default='DEFAULT VALUE')

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default='DEFAULT VALUE')
    job = models.ForeignKey(Job, on_delete=models.PROTECT, null=False, default='DEFAULT VALUE')
    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name