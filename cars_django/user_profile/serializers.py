from rest_framework import serializers

from .models import UserModel
from AppUser.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("first_name",)
    def to_representation(self, instance):
        return instance.first_name

class UserModelSerializer(serializers.ModelSerializer):
    account_id = AppUserSerializer()
    class Meta:
        model = UserModel
        fields = ("account_id", "street_name", "street_number", "zip_code", "city")
    
