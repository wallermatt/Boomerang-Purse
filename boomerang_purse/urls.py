"""
boomerang_purse URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weather_api/', include('boomerang_purse.weather_api.urls')),
    url(r'^weather_charts/', include('boomerang_purse.weather_charts.urls')),
]
