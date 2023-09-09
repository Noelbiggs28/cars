from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import UserModel
from AppUser.models import AppUser
from .serializers import UserModelSerializer

# Create your views here.

class UserProfileViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            appuser = get_object_or_404(UserModel, pk=pk)
            serializer = UserModelSerializer(appuser)
        else:
            appusers = UserModel.objects.order_by("pk")
            serializer = UserModelSerializer(appusers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        appuser = get_object_or_404(AppUser, pk = request.data['account_id'])
        request.data['account_id'] = appuser
        newUser = UserModel.objects.create(**request.data)
        newUser.save()
        newUser.full_clean()
        newUser = json.loads(serialize('json', [newUser]))
        return Response(newUser)
    
    def delete(self, request, pk):
        guy = get_object_or_404(AppUser, pk=pk)
        guy.delete()
        return Response("appuser terminated")