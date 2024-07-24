from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
import requests
from urllib.parse import quote

def hello(request):
    # api_key = '00d1984177e841d58c64ccb59e49d5bb'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=00d1984177e841d58c64ccb59e49d5bb&units=metric'
    form = form1()
    
    if request.method == 'POST':
        a = form1(request.POST)
        if a.is_valid():
            NCity = a.cleaned_data['name']
            CCity = database.objects.filter(name=NCity).count()
            if CCity == 0:
                encoded_city = quote(NCity)  # Properly encode city name
                res = requests.get(url.format(encoded_city)).json()  # Use requests.get() to make the GET request
                print(res)
                if res['cod'] == 200:
                    a.save()
                    messages.success(request, f'{NCity} added successfully!')
                else:
                    messages.error(request, "City does not exist or API key is invalid.")
            else:
                messages.error(request, 'City already exists')
    form = form1()
    form11 = database.objects.all()
    data = []
    for city in form11:
        res = requests.get(url.format(city)).json()
        city_weather = {
            'city':city,
            'temperature':res['main']['temp'],
            'description':res['weather'][0]['description'],
            'country':res['sys']['country'],
            'icon':res['weather'][0]['icon']
        }
        data.append(city_weather)
    context = {'data': data, 'form':form}
    return render(request, "weatherapp.html", context)
    # return render(request, "weatherapp.html", {'form': form,'form11':form11})


def delete(request,CName):
    database.objects.get(name = CName).delete()
    messages.success(request, " "+ CName+ " Removed successfully...!!!")
    return redirect('hello')
