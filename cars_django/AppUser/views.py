from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import AppUser
from .serializers import AppUserSerializer
# Create your views here.

class AppUserView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            appuser = get_object_or_404(AppUser, pk=pk)
            serializer = AppUserSerializer(appuser)
        else:
            appusers = AppUser.objects.order_by("pk")
            serializer = AppUserSerializer(appusers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        newAppUser = AppUser.objects.create(**request.data)
        newAppUser.save()
        newAppUser.full_clean()
        newAppUser = json.loads(serialize('json', [newAppUser]))
        return Response(newAppUser)
    
    def patch(self, request, pk):
        appUser = get_object_or_404(AppUser, pk=pk)
        if "password" in request.data:
            new_password = request.data.get('password')
            appUser.password = new_password
        elif "email" in request.data:
            new_email = request.data.get('email')
            appUser.email = new_email
        appUser.full_clean()
        appUser.save()
        appUser = json.loads(serialize('json',[appUser]))
        return Response('updated duder')

    def delete(self, request, pk):
        appUser = get_object_or_404(AppUser, pk=pk)
        appUser.delete()
        return Response("deleted user")