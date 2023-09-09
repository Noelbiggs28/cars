from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import Car
from .serializers import CarSerializer
from carmodel_app.models import CarModel

# Create your views here.

class CarViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            car = get_object_or_404(Car, pk=pk)
            serializer = CarSerializer(car)
        else:
            cars = Car.objects.order_by("pk")
            serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        model = get_object_or_404(CarModel,pk=request.data['car_model_id'])
        request.data['car_model_id']=model
        car = Car.objects.create(**request.data)
        car.save()
        car.full_clean()
        car = json.loads(serialize('json', [car]))
        return Response(car)
    
    def delete(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        return Response("Car deleted")