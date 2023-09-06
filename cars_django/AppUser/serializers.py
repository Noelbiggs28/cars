from rest_framework import serializers

from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("account_id", "first_name", "last_name", "email", "password")
    
    def __init__(self, *args, **kwargs):
        super(AppUserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1