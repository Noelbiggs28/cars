from django.db import models
from AppUser.models import AppUser
from car_app.models import Car
# Create your models here.
class Advertisement(models.Model):
    advertisement_date=models.DateField(auto_now=True)
    seller_account_id=models.ForeignKey(AppUser, on_delete=models.CASCADE)
    car_id=models.ForeignKey(Car, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.advertisement_date