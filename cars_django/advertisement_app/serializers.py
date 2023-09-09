from rest_framework import serializers

from .models import Advertisement
from car_app.models import Car
from AppUser.models import AppUser
from carmodel_app.models import CarModel

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("make","model")


class CarSerializer(serializers.ModelSerializer):
    car_model_id = CarModelSerializer()
    class Meta:
        model = Car
        fields = ("car_model_id", "number_of_owners", "registration_number", "manufacture_year", "number_of_doors","milege")

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ( "first_name", "last_name", "email" )

class AdvertisementSerializer(serializers.ModelSerializer):
    car_id = CarSerializer()
    seller_account_id = AppUserSerializer()
    class Meta:
        model = Advertisement
        fields = ("advertisement_date","seller_account_id","car_id")