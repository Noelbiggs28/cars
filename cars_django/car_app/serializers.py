from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("car_model_id", "number_of_owners", "registration_number", "manufacture_year", "number_of_doors","milege")