from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('adminmv/', admin.site.urls),
    path('', include('motorartigos.urls'),)
]+ static(settings.MEDIA, document_root=settings.MEDIA_ROOT)