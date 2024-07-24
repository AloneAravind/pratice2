from django.shortcuts import render,redirect

from .models import *
from .forms import *


def view_(request):
    s = employ.objects.all()
    return render(request, 'demoapp/view.html', {'key': s})

def create_(req):
    d = demo_form()
    if req.method == "POST":
        f = demo_form(req.POST)
        if f.is_valid():
            f.save()
            return redirect("view_") # url name
    return render(req , 'demoapp/forms.html',{'crt':d})
    

def dele(request,id):
    s = employ.objects.get(id = id)
    s.delete()
    return redirect('view_')


def update(request,id):
    s = employ.objects.get(id = id)
    f = demo_form(instance = s)
    if request.method == "POST":
        f=demo_form(request.POST , instance = s)
        if f.is_valid():
            f.save()
            return redirect('view_')
    return render(request , "demoapp/forms.html" , {'crt': f})

