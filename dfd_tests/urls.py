from django.conf.urls import include
from django.urls import path
from django.contrib import admin
import django

admin_urls = (admin.site.urls if (django.VERSION[0] >= 2) else include(admin.site.urls))

urlpatterns = [
    path('admin/', admin_urls),
]
