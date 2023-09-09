from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import Advertisement
from .serializers import AdvertisementSerializer
from AppUser.models import AppUser
from car_app.models import Car


# Create your views here.

class AdvertisementViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            ad = get_object_or_404(Advertisement, pk=pk)
            serializer = AdvertisementSerializer(ad)
        else:
            cars = Advertisement.objects.order_by("pk")
            serializer = AdvertisementSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        seller = get_object_or_404(AppUser,pk=request.data['seller_account_id'])
        request.data['seller_account_id']=seller
        car = get_object_or_404(Car,pk=request.data['car_id'])
        request.data['car_id']= car
        ad = Advertisement.objects.create(**request.data)
        ad.save()
        ad.full_clean()
        ad = json.loads(serialize('json', [ad]))
        return Response('ad created')
    
    def delete(self, request, pk):
        Ad = get_object_or_404(Advertisement, pk=pk)
        Ad.delete()
        return Response("ad deleted")