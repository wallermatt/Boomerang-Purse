from django.shortcuts import render_to_response
from django.template import RequestContext

from boomerang_purse.weather_api.services import get_weather_data_location_period


def display_city_period_chart(request):
        city = request.GET['city']
        startdate = request.GET['startdate']
        enddate = request.GET['enddate']
        results = get_weather_data_location_period(city, startdate, enddate)
        title_string = '%s, from %s to %s - ' %(city, startdate, enddate)
        value_keys = 'Max, Min, Mean, Median'
        temp_values = [results['temp_max'], results['temp_min'], results['temp_mean'], results['temp_median']]
        humidity_values = [results['humidity_max'], results['humidity_min'], results['humidity_mean'], results['humidity_median']]
        return render_to_response('city_period_chart.html',
                            {'title_string': title_string,
                             'value_keys': value_keys,
                             'temp_values': temp_values,
                             'humidity_values': humidity_values},
                            context_instance=RequestContext(request))

