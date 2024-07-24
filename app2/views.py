from django.shortcuts import render

from django.http import HttpResponse
import datetime

from .models import *

def two(request):
    return HttpResponse('<h1> this is my class</h1>')

def one(request):
    return render(request , 'demoapp/demo.html')


def third_js(request):
    return render(request , 'demoapp/javas.html')

# dynamic template
def three(pyt):
    # name = "python"
    # name2 = "HTML"
    # return render (pyt, 'demoapp/dynamic.html', {'key_sample' : name,'key_sample1': name2})
 
    # name = "python"
    # name2 = "HTML"
    # dict = {"key_sample" : name, "key_sample1" : name2 , "value1" : 1}
    # return render (pyt, 'demoapp/dynamic.html', context = dict)
 
    name = "python"
    name2 = "HTML"
    tym = datetime.datetime.now()
    dict = {"key_sample" : name, "key_sample1" : name2 , "value1" : 1, "time" : tym}
    return render (pyt, 'demoapp/dynamic.html', context = dict)


def routing(request):
    return render(request , 'demoapp/demo.html')

def table1(req):
    s = sample.objects.all()
    return render(req, 'demoapp/table1.html', {'datakey' : s})