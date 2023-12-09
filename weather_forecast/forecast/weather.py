from django.conf import settings
import requests

def get_weather_data(lat, lon):
    try:
        key = settings.API_KEY
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            extracted_data = []
            for daily_item in data['daily']:
                dt = daily_item['dt']
                temp = daily_item['temp']
                extracted_data.append({
                    'dt': dt,
                    'day': temp['day'],
                    'min': temp['min'],
                    'max': temp['max'],
                    'night': temp['night'],
                    'eve': temp['eve'],
                    'morn': temp['morn'],
                    'lat': lat,
                    'lon': lon
                })
            return extracted_data
        else:
            error_message = f"Erro: {response.status_code} - {response.text}"
            raise requests.RequestException(error_message)
    except requests.RequestException as e:
        raise requests.RequestException(f"Erro na requisição: {e}")
