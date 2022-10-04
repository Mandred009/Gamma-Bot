import datetime
import requests


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = '219931a4c2f0a9b8be334d1c931bbfc0'
    city = city
    url = base_url + 'appid=' + api_key + '&q=' + city
    try:
        response = requests.get(url).json()
        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
    except:
        return "City Invalid"
    return "temperature:{} humidity:{} describe:{}".format(int(temp_celsius),humidity,description)

