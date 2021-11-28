from django.db import models
import datetime
# Create your models here.
class ChemistryClass(models.Model):
    classno=models.IntegerField()
    slotno=models.IntegerField()
    totstu=models.IntegerField()
    allstu=models.IntegerField()
    mindose=models.IntegerField()
    time=models.TimeField()
    date=models.DateField()