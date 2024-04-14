from django.shortcuts import render
from .models import  Client
from django.shortcuts import render, redirect
from .models import Car,House,Home_appliance,spar_parts,clothing,laptop_phone,Accessory
from buybay_logic.models import House
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request,'index.html')

def cars(request):
    
    return render(request,'cars.html')


def profil(request):
    return render(request,'profil.html')

def piece(request):
    return render(request,'pie.html')
    
def an(request):
    return render(request,'an.html')

def item(request):
    return render(request,'item1.html')

def it(request):
    return render(request,'it.html')

def car_cat(request):
    return render(request,'car_cat.html')

def sign(request):
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            name = request.POST.get('name')
            num_telephone = request.POST.get('num_telephone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cli=Client(nom=first_name, prenom=name, num_telephone=num_telephone, email=email, password=password)
            cli.save()
            return redirect('index.html')
        return render(request,'si.html')

def mod(request):
    return render(request,'mod.html')


def model(request):
    return render(request,'model.html')

def categorie(request):
    return render(request,'categorie.html')

def immobilier(request):
    return render(request,'im.html')

def login(request):
    return render(request,'lo.html')

def mod1(request):
    return render(request,'mod1.html')



category_choices = [
        ('car', 'Car'),
        ('houses', 'Houses'),
        ('laptop_phone', 'Laptop & Phone'),
        ('clothing', 'Clothing'),
        ('accessories', 'Accessories'),
        ('home_appliance', 'Home Appliance'),
        ('spare_parts', 'Spare Parts'),
    ]
        
def new(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('Model')  
        category = request.POST.get('category_choices')
        year = request.POST.get('Year')
        engine = request.POST.get('Engine')
        mileage = request.POST.get('Mileage')
        des = request.POST.get('Description')
        finition = request.POST.get('Finition')
        fuel = request.POST.get('fuel')
        image = request.FILES.get('image')
        
        price = request.POST.get('Price')
        

        if image is None:
            pass
        
        car = Car(
            brand=brand, model=model, year=year, engine=engine,
            mileage=mileage, des=des, finition=finition, price=price, image=image, fuel=fuel, category=category
        )
        car.save()
        messages.success(request, 'Car added successfully')
        return redirect('cars.html')
    return render(request, 'new.html')


def about(request):
    return render(request,'ab.html')

def laptop(request):
    return render(request,'lap.html')

def accessories(request):
    return render(request,'acc.html')

