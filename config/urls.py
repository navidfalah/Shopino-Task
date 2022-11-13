from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/linkshortener/', include('linkshortener.urls')),
]
