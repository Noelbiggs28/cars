from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404

from .models import CarModel
from .serializers import CarModelSerializer

# Create your views here.

class CarModelViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            Model = get_object_or_404(CarModel, pk=pk)
            serializer = CarModelSerializer(Model)
        else:
            Models = CarModel.objects.order_by("pk")
            serializer = CarModelSerializer(Models, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        model = CarModel.objects.create(**request.data)
        model.save()
        model.full_clean()
        model = json.loads(serialize('json', [model]))
        return Response(model)
    
    def delete(self, request, pk):
        carmodel = get_object_or_404(CarModel, pk=pk)
        carmodel.delete()
        return Response("Model user")