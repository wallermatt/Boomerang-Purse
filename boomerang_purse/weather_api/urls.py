from django.conf.urls import patterns, url

from .views import DisplayCityPeriod

urlpatterns = patterns('',
    url(r'^display_city_period/$', DisplayCityPeriod.as_view(), name='disply_city_period'),
)
