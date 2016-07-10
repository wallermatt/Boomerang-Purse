from django.conf.urls import patterns, url

from .views import display_city_period_chart

urlpatterns = [
    url(r'^display_city_period_chart/$', display_city_period_chart, name='display_city_period_chart'),
]
