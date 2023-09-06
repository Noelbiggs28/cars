from django.db import models

# Create your models here.
class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    make = models.TextField()
    model = models.TextField()

    class Meta:
        unique_together = ['make', 'model']