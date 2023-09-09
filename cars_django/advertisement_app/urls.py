from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdvertisementViews.as_view()),
    path('<int:pk>', views.AdvertisementViews.as_view())
]