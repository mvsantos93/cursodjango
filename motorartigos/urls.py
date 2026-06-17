from django.urls import path
from motorartigos.views import index

urlpatterns = [
    path('', index),
]