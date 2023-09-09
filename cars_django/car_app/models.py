from django.db import models
from carmodel_app.models import CarModel
# Create your models here.

class Car(models.Model):
    car_model_id=models.ForeignKey(CarModel, on_delete=models.CASCADE)
    number_of_owners=models.IntegerField()
    registration_number=models.IntegerField()
    manufacture_year=models.IntegerField()
    number_of_doors=models.IntegerField()
    milege=models.IntegerField()

    def __str__(self):
        return self.car_model_id