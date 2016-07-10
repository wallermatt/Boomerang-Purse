
from django.test import TestCase

from .services import get_weather_data_location_period

class WeatherAPIServicesTests(TestCase):

    def setUp(self):

        self.city_period_kwargs = {'city': 'London', 'startdate': '2016-01-01', 'enddate': '2016-01-02'}

        self.expected_weather_data = {"temp_max":10,"temp_mean":9,"humidity_min":77,"temp_min":8,"temp_median":9,"humidity_max":80,"humidity_mean":78, "humidity_median": 78}


    def test_get_weather_data_location_period(self):

        weather_data = get_weather_data_location_period(**self.city_period_kwargs)

        self.assertEquals(weather_data, self.expected_weather_data)
