from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminmv/', admin.site.urls),
    path('', include('motorartigos.urls'),)
]