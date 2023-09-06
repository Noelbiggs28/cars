from . import serializers
from rest_framework import generics,permissions
from . import models
# Create your views here.

class AllAppUser(generics.ListCreateAPIView):
    queryset=models.AppUser.objects.all()
    serializer_class=serializers.AppUserSerializer
    #permission_classes=[permissions.IsAuthenticated]