from rest_framework.views import APIView
from rest_framework.response import Response

from boomerang_purse.weather_api.services import get_weather_data_location_period

class DisplayCityPeriod(APIView):

    def get(self, request, format=None):
        city = request.GET['city']
        startdate = request.GET['startdate']
        enddate = request.GET['enddate']
        results = get_weather_data_location_period(city, startdate, enddate)
        return Response(results)

