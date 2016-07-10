# Boomerang-Purse
Weather data REST API, plus weather data charts.

**API** to enter a city and period defined by startdate and enddate. Dates should be in the format yyyy-mm-dd.
Year (yyyy) must be the same for both dates and not less than 2008 (uses www.worldweatheronline.com historical API)

Returns min, max, mean and median temperature and humidity for city and time period in format:

{'temp_max': `<integer>`, 'temp_min': `<integer>`, 'temp_mean': `<integer>`, 'temp_median': `<integer>`, 'humidity_max': `<integer>`, 'humidity_min': `<integer>`, 'humidity_mean': `<integer>`, 'humidity_median': `<integer>`}

Url: /weather_api/display_city_period/?city=`<city>`&startdate=`<yyyy-mm-dd>`&enddate=`<yyyy-mm-dd>`

**Charts** to display above data in two bar charts for tempaerature and humidity.

Url: /weather_charts/display_city_period_chart/?city=`<city>`&startdate=`<yyyy-mm-dd>`&enddate=`<yyyy-mm-dd>`


