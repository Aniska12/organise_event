from django.db import models

# Create your models here.
class meet(models.Model):
    date=models.DateField()
    time=models.TimeField()
