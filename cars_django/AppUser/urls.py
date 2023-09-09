from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppUserView.as_view()),
    path('<int:pk>', views.AppUserView.as_view())
]