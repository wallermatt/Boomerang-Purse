import json
from django.core.urlresolvers import reverse
from django.test import TestCase

class WeatherAPITests(TestCase):

    def setUp(self):

        self.display_city_period_url = '%s?city=London&startdate=2016-01-01&enddate=2016-01-02' % reverse('display_city_period')

        self.result = json.loads('{"temp_max":10,"temp_mean":9,"humidity_min":77,"temp_min":8,"temp_median":9,"humidity_max":80,"humidity_mean":78, "humidity_median": 78}')

        # TODO: build urls that will cause errors to test API's failure modes

    def test_display_city_period(self):

        response = self.client.get(self.display_city_period_url)

        self.assertEquals(response.status_code, 200)

        self.assertEqual(json.loads(response.content), self.result)


    # TODO: test API's failure modes