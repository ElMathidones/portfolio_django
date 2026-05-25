from django.contrib import admin
from django.urls import path

from core.views import post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post),
]
