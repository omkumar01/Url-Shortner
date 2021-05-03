from django.db import models

# Create your models here.


class InputUrl(models.Model):
    link = models.URLField(max_length=10000)
    uuid = models.CharField(max_length=10)