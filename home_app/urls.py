from django.urls import path
from . import views


app_name = "home_app"

urlpatterns = [
    path('', views.index),
    path('contacts/', views.contacts),
    path('about/', views.about)
]
