from django import forms
from .models import Car

class SellItemForm(forms.Form):
    category = forms.ChoiceField(choices=[
        ('none', 'Categories'),
        ('car', 'Car'),
        ('houses', 'Houses'),
        ('laptop_phone', 'Laptop & Phone'),
        ('clothing', 'Clothing'),
        ('accessories', 'Accessories'),
        ('home_appliance', 'Home Appliance'),
        ('spare_part', 'Spare Parts')
    ])
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    engine = forms.CharField(max_length=100)
    mileage = forms.DecimalField()
    description = forms.CharField(widget=forms.Textarea)
    finition = forms.CharField(max_length=100)
    fuel = forms.CharField(max_length=100)
    price = forms.DecimalField()
    image = forms.ImageField(required=False)
