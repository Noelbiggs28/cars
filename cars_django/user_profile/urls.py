from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserProfileViews.as_view()),
    path('<int:pk>', views.UserProfileViews.as_view())
]