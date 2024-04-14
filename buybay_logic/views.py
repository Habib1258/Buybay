from django.shortcuts import render
from .models import  Client
from django.shortcuts import render, redirect
from .models import Car,House,Home_appliance,spar_parts,clothing,laptop_phone,Accessory
from buybay_logic.models import House




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
    category = category_choices
    category = request.POST.get('category')
    if category == 'car':
        if request.method == 'POST':
            category = request.POST.get('category')
            brand = request.POST.get('brand')
            model = request.POST.get('Model')  
            year = request.POST.get('Year')
            engine = request.POST.get('Engine')
            mileage = request.POST.get('Mileage')
            des = request.POST.get('Description')
            finition = request.POST.get('Finition')
            fuel = request.POST.get('fuel')
            image = request.FILES.get('image') 
            price = request.POST.get('Price')
            car = Car(
                brand=brand, model=model, year=year, category=category, engine=engine,
                mileage=mileage, des=des, finition=finition, price=price, image=image, fuel=fuel
            )
            car.save()
            return redirect('index.html')  
    elif category == 'houses': 
         if request.method == 'POST':
            category = request.POST.get('category')
            type = request.POST.get('type')
            location = request.POST.get('location')  
            floor = request.POST.get('floor')
            rooms = request.POST.get('rooms')
            area = request.POST.get('area')
            description = request.POST.get('Description')
            facade = request.POST.get('facade')
            image = request.FILES.get('image') 
            price = request.POST.get('Price')
            house = House(
                type=type, location=location, floor=floor, rooms=rooms, area=area,
                facade=facade, des=description, price=price, image=image,
            )
            house.save()
            return redirect('index.html')
    return render(request,'new.html')


def about(request):
    return render(request,'ab.html')

def laptop(request):
    return render(request,'lap.html')

def accessories(request):
    return render(request,'acc.html')

