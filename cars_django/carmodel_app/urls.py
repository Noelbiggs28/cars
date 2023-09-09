from django.urls import path
from . import views


urlpatterns = [
    path('', views.CarModelViews.as_view()),
    path('<int:pk>', views.CarModelViews.as_view())
]