from django.db import models
from Car.models import Car
from AppUser.models import AppUser

# Create your models here.
class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    advertisement_date = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller = models.ForeignKey(AppUser, on_delete=models.CASCADE)