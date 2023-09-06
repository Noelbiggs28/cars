from django.db import models
from CarModel.models import CarModel


# Create your models here.
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    number_of_owners = models.IntegerField()
    registration_number = models.TextField(unique=True)
    manufacture_year = models.IntegerField()
    number_of_doors = models.IntegerField(default=5)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    mileage = models.IntegerField(null=True, blank=True)  # Assuming mileage can be NULL