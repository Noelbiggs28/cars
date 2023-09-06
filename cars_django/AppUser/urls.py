from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllAppUser.as_view())
]