from datetime import date, datetime

from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=64)

    def watered_today(self):
        if self.water_set.latest('time').time.date() == date.today():
            return True
        return False
