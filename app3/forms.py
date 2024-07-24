from django import forms
from .models import employ

class demo_form(forms.ModelForm):
    class Meta:
        # models = employ # for multiple functions
        model = employ
        fields = '__all__' # ['name', 'reg_num']

        