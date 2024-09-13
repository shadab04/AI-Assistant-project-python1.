import requests
api_key = '9013d84cc21a448d0cf15ca130f68949'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def get_weather_info(city):
    result = requests.get(url.format(city, api_key))

    if result.status_code == 200:
        data = result.json()

        city_name = data['name']
        country = data['sys']['country']
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        min_temperature = data['main']['temp_min']
        max_temperature = data['main']['temp_max']
        humidity = data['main']['humidity']

        weather_info = {
            'city': city_name,
            'country': country,
            'weather_desc': weather_desc,
            'temperature': temperature,
            'min_temperature': min_temperature,
            'max_temperature': max_temperature,
            'humidity': humidity,
        }

        return weather_info
    else:
        return None
