from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    salary = models.IntegerField(default=0)


    