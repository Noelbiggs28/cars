
from django.db import models
from AppUser.models import AppUser
# Create your models here.


class UserModel(models.Model):
    account_id=models.ForeignKey(AppUser, on_delete=models.CASCADE)
    street_name=models.TextField(max_length=50,blank=False)
    street_number=models.BigIntegerField(blank=False)
    zip_code=models.BigIntegerField(blank=False)
    city=models.TextField(max_length=50,blank=False)


    def __str__(self):
        return self.account_id
    
    