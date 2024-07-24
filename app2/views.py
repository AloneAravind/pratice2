from django.shortcuts import render
import requests

def get_weather(city):
    api_key = '00d1984177e841d58c64ccb59e49d5bb'  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'main' in data and 'weather' in data:
        weather = {
            'city': city,
            'temperature': round(data['main']['temp'] - 273.15, 2),  # Convert temperature to Celsius
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

def weather_view(request):
    city = 'London'  # Default city
    if 'city' in request.GET:
        city = request.GET['city']
    weather = get_weather(city)
    print(weather)  # Debugging print
    return render(request, 'weatherapp.html', {'weather': weather})
