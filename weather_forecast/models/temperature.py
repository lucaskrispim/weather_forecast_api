from django.db import models
import datetime

# Create your models here.
class Temperature(models.Model):
    id = models.IntegerField('id',primary_key=True)
    querydt = models.DateField(default=datetime.date.today)
    dt = models.IntegerField()
    day = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    night = models.FloatField()
    eve = models.FloatField()
    morn = models.FloatField()
    lat  = models.FloatField()
    lon  = models.FloatField()

