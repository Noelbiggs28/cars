from django.urls import path
from . import views


urlpatterns = [
    path('', views.CarViews.as_view()),
    path('<int:pk>', views.CarViews.as_view())
]