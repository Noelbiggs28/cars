from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    account_id=models.IntegerField()
    street_name=models.TextField(max_length=50,blank=False)
    street_number=models.BigIntegerField(blank=False)
    zip_code=models.BigIntegerField(blank=False)

    def __str__(self):
        return self.account_id

# class Product(models.Model):
#     category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
#     vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
#     title=models.CharField(max_length=200)
#     detail=models.TextField(null=True)
#     price=models.FloatField()

#     def __str__(self):
#         return self.title
    
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# # Assuming you want to utilize Django's authentication system
# class AppUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)

# class AppUser(AbstractBaseUser):
#     account_id = models.AutoField(primary_key=True)
#     first_name = models.TextField()
#     last_name = models.TextField()
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)  # Normally you'd use Django's auth system and wouldn't need to define this

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     objects = AppUserManager()

#     class Meta:
#         constraints = [
#             models.CheckConstraint(check=~models.Q(first_name__contains=' '), name='first_name_no_spaces'),
#             models.CheckConstraint(check=~models.Q(last_name__contains=' '), name='last_name_no_spaces')
#         ]


# class UserProfile(models.Model):
#     profile_id = models.AutoField(primary_key=True)
#     account = models.OneToOneField(AppUser, on_delete=models.CASCADE)
#     street_name = models.TextField()
#     street_number = models.TextField()
#     zip_code = models.TextField()
#     city = models.TextField()


# class CarModel(models.Model):
#     car_model_id = models.AutoField(primary_key=True)
#     make = models.TextField()
#     model = models.TextField()

#     class Meta:
#         unique_together = ['make', 'model']


# class Car(models.Model):
#     car_id = models.AutoField(primary_key=True)
#     number_of_owners = models.IntegerField()
#     registration_number = models.TextField(unique=True)
#     manufacture_year = models.IntegerField()
#     number_of_doors = models.IntegerField(default=5)
#     car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
#     mileage = models.IntegerField(null=True, blank=True)  # Assuming mileage can be NULL


# class Advertisement(models.Model):
#     advertisement_id = models.AutoField(primary_key=True)
#     advertisement_date = models.DateTimeField()
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     seller = models.ForeignKey(AppUser, on_delete=models.CASCADE)
