from django import forms
from .models import CoffeeTypes


class CoffeeTypesForm(forms.Form):
    coffee_types = forms.ModelChoiceField(
        queryset=CoffeeTypes.objects.all(), label="Select coffee types"
    )
