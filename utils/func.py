import io, string, random, requests


def generate_password(length):
    symbols = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(symbols) for _ in range(length))


def get_rate(from_currency, to_currency):
    url = 'https://api.frankfurter.app/latest'
    data = requests.get(url, params={'from': from_currency, 'to': to_currency}).json()
    return data['rates'][to_currency]


def get_weather(city):
    geo_url = 'https://geocoding-api.open-meteo.com/v1/search'
    weather_url = 'https://api.open-meteo.com/v1/forecast'

    geodata = requests.get(geo_url, params={'name': city, 'count': 1}).json()

    if 'results' in geodata:
        place = geodata['results'][0]
        
        params = {
            'latitude': place['latitude'],
            'longitude': place['longitude'],
            'current_weather': True
        }

        data = requests.get(weather_url, params=params).json()
        weather_data = data['current_weather']
        weather_data['place'] = place['name']
        
        return weather_data


def get_youtube_stream_data(video):
    stream = video.streams.get_highest_resolution()
    
    buffer = io.BytesIO()
    stream.stream_to_buffer(buffer)
    return buffer
