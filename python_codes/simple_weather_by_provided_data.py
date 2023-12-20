d = {
    'consolidated_weather': [{
        'id': 5756340131594240,
        'weather_state_name': 'Heavy Cloud',
        'weather_state_abbr': 'hc',
        'wind_direction_compass': 'W',
        'created': '2018-09-03T13:19:47.023710Z',
        'applicable_date': '2018-09-03',
        'min_temp': 13.7975,
        'max_temp': 22.1725,
        'the_temp': 14.47,
        'wind_speed': 4.825861634719902,
        'wind_direction': 269.0843199650456,
        'air_pressure': 986.85,
        'humidity': 77,
        'visibility': 9.997862483098704,
        'predictability': 71
    }, {
        'id': 6707457686503424,
        'weather_state_name': 'Clear',
        'weather_state_abbr': 'c',
        'wind_direction_compass': 'W',
        'created': '2018-09-03T13:19:50.520020Z',
        'applicable_date': '2018-09-04',
        'min_temp': 13.5025,
        'max_temp': 25.685000000000002,
        'the_temp': 24.23,
        'wind_speed': 5.112756833426125,
        'wind_direction': 270.2794344092529,
        'air_pressure': 987.6,
        'humidity': 64,
        'visibility': 9.997862483098704,
        'predictability': 68
    }, {
        'id': 6129188230660096,
        'weather_state_name': 'Light Cloud',
        'weather_state_abbr': 'lc',
        'wind_direction_compass': 'W',
        'created': '2018-09-03T13:19:53.914860Z',
        'applicable_date': '2018-09-05',
        'min_temp': 13.375,
        'max_temp': 25.925,
        'the_temp': 26.73,
        'wind_speed': 5.52573398022217,
        'wind_direction': 274.17536913320464,
        'air_pressure': 987.2,
        'humidity': 64,
        'visibility': 9.997862483098704,
        'predictability': 70
    }, {
        'id': 6028561710317568,
        'weather_state_name': 'Light Cloud',
        'weather_state_abbr': 'lc',
        'wind_direction_compass': 'W',
        'created': '2018-09-03T13:19:56.527170Z',
        'applicable_date': '2018-09-06',
        'min_temp': 13.7025,
        'max_temp': 26.322499999999998,
        'the_temp': 27.47,
        'wind_speed': 5.296090166759458,
        'wind_direction': 278.6409999622535,
        'air_pressure': 989.74,
        'humidity': 63,
        'visibility': 9.997862483098704,
        'predictability': 70
    }, {
        'id': 6695273375989760,
        'weather_state_name': 'Heavy Cloud',
        'weather_state_abbr': 'hc',
        'wind_direction_compass': 'WNW',
        'created': '2018-09-03T13:19:59.229340Z',
        'applicable_date': '2018-09-07',
        'min_temp': 14.6675,
        'max_temp': 26.37,
        'the_temp': 20.62,
        'wind_speed': 5.071978578435272,
        'wind_direction': 289.5,
        'air_pressure': 1012.59,
        'humidity': 57,
        'visibility': 9.997862483098704,
        'predictability': 71
    }, {
        'id': 5627284954284032,
        'weather_state_name': 'Heavy Cloud',
        'weather_state_abbr': 'hc',
        'wind_direction_compass': 'NW',
        'created': '2018-09-03T13:20:02.498590Z',
        'applicable_date': '2018-09-08',
        'min_temp': 14.755,
        'max_temp': 26.11,
        'the_temp': 19.47,
        'wind_speed': 5.78301625175641,
        'wind_direction': 305.0323351994134,
        'air_pressure': 1010.77,
        'humidity': 52,
        'visibility': 9.997862483098704,
        'predictability': 71
    }],
    'time': '2018-09-03T07:46:46.850600-07:00',
    'sun_rise': '2018-09-03T06:40:29.947547-07:00',
    'sun_set': '2018-09-03T19:35:30.177997-07:00',
    'timezone_name': 'LMT',
    'parent': {
        'title': 'California',
        'location_type': 'Region / State / Province',
        'woeid': 2347563,
        'latt_long': '37.271881,-119.270233'
    },
    'sources': [{
        'title': 'Forecast.io',
        'slug': 'forecast-io',
        'url': 'http://forecast.io/',
        'crawl_rate': 480
    }, {
        'title': 'HAMweather',
        'slug': 'hamweather',
        'url': 'http://www.hamweather.com/',
        'crawl_rate': 360
    }, {
        'title': 'OpenWeatherMap',
        'slug': 'openweathermap',
        'url': 'http://openweathermap.org/',
        'crawl_rate': 360
    }, {
        'title': 'Weather Underground',
        'slug': 'wunderground',
        'url': 'https://www.wunderground.com/?apiref=fc30dc3cd224e19b',
        'crawl_rate': 720
    }, {
        'title': 'World Weather Online',
        'slug': 'world-weather-online',
        'url': 'http://www.worldweatheronline.com/',
        'crawl_rate': 360
    }, {
        'title': 'Yahoo',
        'slug': 'yahoo',
        'url': 'http://weather.yahoo.com/',
        'crawl_rate': 180
    }],
    'title': 'Mountain View',
    'location_type': 'City',
    'woeid': 2455920,
    'latt_long': '37.39999,-122.079552',
    'timezone': 'America/Los_Angeles'
}
for forecast in d['consolidated_weather']:
    date = forecast['applicable_date']
    humidity = forecast['humidity']
    print(f"{date}\tHumidity: {humidity}") # /t is to insert tab