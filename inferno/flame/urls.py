from django.urls import path 
from flame.views import index

from . import views

app_name = "flame"

urlpatterns = [
    path("laptops/", views.index)
]