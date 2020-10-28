from django.conf.urls import include, url
from django.contrib import admin
import django

admin_urls = (admin.site.urls if (django.VERSION[0] >= 2) else include(admin.site.urls))

urlpatterns = [
    url(r'^admin/', admin_urls),
]
