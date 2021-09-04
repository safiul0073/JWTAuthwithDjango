from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=59, null=True)
    text = models.CharField(max_length=200, null=True)
    userId = models.IntegerField(null=True)