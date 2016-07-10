from rest_framework.views import APIView
from rest_framework.response import Response

from boomerang_purse.weather_api.services import get_weather_data_location_period

class DisplayCityPeriod(APIView):
    '''
    Gets city, startdate and enddate parameters then uses these in World Weather Online http://www.worldweatheronline.com/
    API and uses data returned to calculate min, max, mean and median temp and humidity.

    Inputs:
            city: city name text
            startdate: yyyy-mm-dd
            enddate: yyyy-mm-dd

    Outputs:
            weather_data: json dictionary of type services.WEATHER_DATA_FORMAT
                          {'temp_max': <integer>, 'temp_min': <integer>, 'temp_mean': <integer>, 'temp_median': <integer>, 'humidity_max': <integer>, 'humidity_min': <integer>, 'humidity_mean': <integer>, 'humidity_median': <integer>}

    '''
    def get(self, request, format=None):
        city = request.GET['city']
        startdate = request.GET['startdate']
        enddate = request.GET['enddate']
        # TODO bespoke parameter validation based on World Weather Online API.
        results = get_weather_data_location_period(city, startdate, enddate)
        return Response(results)

