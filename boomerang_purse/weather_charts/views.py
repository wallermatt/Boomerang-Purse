from django.shortcuts import render_to_response
from django.template import RequestContext

from boomerang_purse.weather_api.services import get_weather_data_location_period


def display_city_period_chart(request):
    '''
    Gets city, startdate and enddate parameters then uses these in World Weather Online http://www.worldweatheronline.com/
    API and uses data returned to calculate min, max, mean and median temp and humidity.

    Then temp and humidity data is split up and used to create individual y-axis data lists.
    These are used with Plotly.js to produce bar charts.

    Inputs:
            city: city name text
            startdate: yyyy-mm-dd
            enddate: yyyy-mm-dd

    Outputs:
            city_period_chart.html: Two Plotly.js charts for max, min, mean, median for temp and humidity.
    '''
    city = request.GET['city']
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']
    # TODO bespoke parameter validation based on World Weather Online API.

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

