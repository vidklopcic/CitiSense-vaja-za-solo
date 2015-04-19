from django.db import models
from django.contrib.auth.models import User

class Measurements(models.Model):
    owner = models.ForeignKey(User)
    name = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class VesnaReading(models.Model):
    measurements = models.ForeignKey(Measurements)
    time = models.DateTimeField()
    CO = models.FloatField()
    NO2 = models.FloatField()
    O3 = models.FloatField()
    humidity = models.FloatField()
    movement = models.FloatField()
    temp = models.FloatField()

    def __str__(self):
        return str(self.measurements)