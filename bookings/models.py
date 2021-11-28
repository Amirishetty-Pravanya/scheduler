from django.db import models
import datetime
# Create your models here.
class bookings(models.Model):
    username=models.TextField()
    classno=models.IntegerField()
    sub=models.TextField()
    date=models.DateField()
    time=models.TimeField()