import requests
import numpy

WWO_API_URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx'
WWO_API_KEY = 'e5559e14ee924310bbe212846160907'

WEATHER_DATA = {'temp_max': 0, 'temp_min': 0, 'temp_mean': 0, 'temp_median': [], 'humidity_max': 0, 'humidity_min': 0, 'humidity_mean': 0, 'humidity_median': []}  

def build_weather_data(value_type, value, count):
    for key in WEATHER_DATA:
        if value_type in key:
            if 'max' in key:
                if value > WEATHER_DATA[key] or count == 0:
                    WEATHER_DATA[key] = value
            elif 'min' in key:
                if value < WEATHER_DATA[key] or count == 0:
                    WEATHER_DATA[key] = value
            elif 'mean' in key:
                WEATHER_DATA[key] += value
            elif 'median' in key:
                WEATHER_DATA[key].append(value)


def calculate_final_weather_data(count):
    for key in WEATHER_DATA:
        if 'mean' in key:
            WEATHER_DATA[key] = WEATHER_DATA[key] / count
        elif 'median' in key:   
            WEATHER_DATA[key] = numpy.median(numpy.array(WEATHER_DATA[key]))
        
                
def get_weather_data_location_period(city, startdate, enddate):
    params = {'key': WWO_API_KEY, 'q': city, 'date': startdate, 'enddate': enddate, 'format': 'json'}
    weather_results = requests.get(WWO_API_URL, params=params)
    weather_results_json = weather_results.json()

    count = 0
    for day in weather_results_json['data']['weather']:
        for time in day['hourly']:
            build_weather_data('temp', int(time['tempC']), count)
            build_weather_data('humidity', int(time['humidity']), count)
            count += 1

    calculate_final_weather_data(count)
    return WEATHER_DATA
            


#print get_weather_data_location_period('London', '2016-07-03', '2016-07-04')
