import os
import requests
import numpy

WWO_API_URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx'
WWO_API_KEY = os.environ['WWO_API_KEY']

WEATHER_DATA_TEMPLATE = {'temp_max': 0, 'temp_min': 0, 'temp_mean': 0, 'temp_median': [], 'humidity_max': 0, 'humidity_min': 0, 'humidity_mean': 0, 'humidity_median': []}  


def build_weather_data(value_type, value, count, weather_data):
    '''
    For each row of weather data this updates max and min values for value type.
    Mean is used to hold total value, and median a list of all values.

    Inputs:
            value_type: string for 'temp', 'humidity' etc.
            value: integer for temp, humidity etc.
            count: number of records integer - used only to determine first iteration
                   to set min.
            weather_data: as WEATHER_DATA_TEMPLATE, but mean is total of all values,
                          and mean a list of all values

    Outputs:
            weather_data: as WEATHER_DATA_TEMPLATE, but mean is total of all values,
                          and mean a list of all values
    '''
    for key in weather_data:
        if value_type in key:
            if 'max' in key:
                if value > weather_data[key] or count == 0:
                    weather_data[key] = value
            elif 'min' in key:
                if value < weather_data[key] or count == 0:
                    weather_data[key] = value
            elif 'mean' in key:
                weather_data[key] += value
            elif 'median' in key:
                weather_data[key].append(value)
    return weather_data


def calculate_final_weather_data(count, weather_data):
    '''
    Calculates mean and median once weather_results_json has been processed

    Inputs:
            count: number of records integer
            weather_data: as WEATHER_DATA_TEMPLATE, but mean is total of all values,
                          and mean a list of all values

    Outputs:
            weather_data: as WEATHER_DATA_TEMPLATE
    '''
    for key in weather_data:
        if 'mean' in key:
            weather_data[key] = weather_data[key] / count
        elif 'median' in key:   
            weather_data[key] = int(numpy.median(numpy.array(weather_data[key])))
    return weather_data


def get_json_weather_data_from_weatheronline(city, startdate, enddate):
    '''
    Gets weather data from World Weather online API.

    Inputs:
            city: city name text
            startdate: yyyy-mm-dd
            enddate: yyyy-mm-dd

    Outputs:
            weather_results_json
    '''
    params = {'key': WWO_API_KEY, 'q': city, 'date': startdate, 'enddate': enddate, 'format': 'json', 'tp': 24} # tp=time period=24 hours
    weather_results = requests.get(WWO_API_URL, params=params)
    weather_results_json = weather_results.json()
    return weather_results_json

           
def calculate_weather_data_results(weather_results_json):
    '''
    Calculates weather data (temp and humidity max, min, mean, median) from json output of
    World Weather online.

    Inputs:
            weather_results_json: World Weather online format

    Outputs:
            weather_data: dictionary of type WEATHER_DATA_FORMAT
    '''
    weather_data = WEATHER_DATA_TEMPLATE.copy()
    count = 0
    for day in weather_results_json['data']['weather']:
        for time in day['hourly']:
            weather_data = build_weather_data('temp', int(time['tempC']), count, weather_data)
            weather_data = build_weather_data('humidity', int(time['humidity']), count, weather_data)
            count += 1

    weather_data = calculate_final_weather_data(count, weather_data)

    return weather_data

                
def get_weather_data_location_period(city, startdate, enddate):
    '''
    Gets daily weather data for city for the period between startdate and enddate.
    Then claculates max, min, mean and median temps and humidity.

    Inputs:
            city: city name text
            startdate: yyyy-mm-dd
            enddate: yyyy-mm-dd

    Outputs:
            weather_data: dictionary of type WEATHER_DATA_FORMAT
    '''
    weather_results_json = get_json_weather_data_from_weatheronline(city, startdate, enddate)
    weather_data = calculate_weather_data_results(weather_results_json)
    return weather_data
            


