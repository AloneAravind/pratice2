from django.forms import ModelForm,TextInput
from .models import *

class form1(ModelForm):
    class Meta:

        model = database
        fields = '__all__'
        widgets = {'name': TextInput(attrs={ 'placeholder':'City Name'})} # This is a dictionary specifying custom widgets for form fields
