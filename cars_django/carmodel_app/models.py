from django.db import models
# Create your models here.

class CarModel(models.Model):
    make=models.TextField(max_length=50,blank=False)
    model=models.TextField(max_length=50, blank=False)


    def __str__(self):
        return self.model