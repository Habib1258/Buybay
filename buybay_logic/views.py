from django.shortcuts import render, redirect ,get_object_or_404
from .models import Client,Car,House,Home_appliance,Spar_parts,Clothing,Laptop_phone,Accessory
from django.http import HttpResponse, JsonResponse
from itertools import zip_longest
from django.contrib.auth import authenticate, login




# Create your views here.

def index(request):
    return render(request,'index.html')

def cars(request):
    all_cars = Car.objects.filter(approved =1)
    chunked_items = zip_longest(*[iter(all_cars)]*3, fillvalue=None) 
    return render(request,'cars.html',{'all_c' : all_cars, 'chunked_items': chunked_items,})


def profil(request):
    persons = Client.objects.all()
    return render(request,'profil.html', {'person' : persons})

def piece(request):
    all_pieces = Spar_parts.objects.all()
    return render(request,'pie.html',{'all_p' : all_pieces})
    
def an(request):
    return render(request,'an.html')

def item_house(request):
    houses = House.objects.all()
    persons = Client.objects.all()
    return render(request,'item_house.html',{'houses' : houses, 'person' : persons})

def item_lap(request):
    laptop_phones = Laptop_phone.objects.all()
    persons = Client.objects.all()
    return render(request,'item_lap.html',{'laptop_phones' :laptop_phones, 'person' : persons})

def item_accessory(request):
    accessories = Accessory.objects.all()
    persons = Client.objects.all()
    return render(request,'item_house.html',{'accessories' :accessories, 'person' : persons})

def item_clothing(request):
    clothings = Clothing.objects.all()
    persons = Client.objects.all()
    return render(request,'item_clothing.html',{'clothings' :clothings, 'person' : persons})

def item_pie(request):
    spare_parts = Spar_parts.objects.all()
    persons = Client.objects.all()
    return render(request,'item_clothing.html',{'spare_parts' : spare_parts, 'person' : persons})

def item_home(request):
    Home_appliance = Home_appliance.objects.all()
    persons = Client.objects.all()
    return render(request,'it.html', {'home_appliance' :Home_appliance ,'person' : persons})


def item_car(request):
    cars = Car.objects.all()
    try:
        img = Car.objects.get(brand=request.GET.get('brand'))
    except Car.DoesNotExist:
        img = None
    persons = Client.objects.all()
    return render(request,'item_car.html',{'cars' : cars, 'person' : persons,  'img': img if img else None})

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




def model(request):
    return render(request,'model.html')

def categorie(request):
    return render(request,'categorie.html')

def immobilier(request):
    return render(request,'im.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,'lo.html')



def mod(request):
    cars = Car.objects.filter(approved=0)
    return render(request,'mod.html', {'cars': cars})

def home(request):
    return render(request,'home.html')

def clothing(request):
    return render(request,'cloth.html')





def new(request):
    category_choices = [
        ('car', 'Car'),
        ('houses', 'Houses'),
        ('laptop_phone', 'Laptop & Phone'),
        ('clothing', 'Clothing'),
        ('accessories', 'Accessory'),
        ('home_appliance', 'Home Appliance'),
        ('spare part', 'Spare Parts'),
    ]
    cat = request.POST.get('cate')
    
    if cat == 'car' :
        new1(request)
        return redirect("cars.html")
    elif cat == 'houses' :
        new2(request)
        return redirect("im.html")
    elif cat == 'home appliance' :
        new3(request)
        return redirect("home.html")
    elif cat == 'accessories' :
        new4(request)
        return redirect("acc.html")
    elif cat == 'spare part' :
        new5(request)
        return redirect("pie.html")
    elif cat == 'clothing' :
        new6(request)
        return redirect("cloth.html")
    elif cat == 'laptop_phone' :
        new7(request)
        return redirect("lap.html")
    return render(request,'new.html')

def new1(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('Model')  
        category = request.POST.get('cate')
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

        all_cars = Car.objects.all()
        
        car = Car(
            brand=brand, model=model, year=year, engine=engine,
            mileage=mileage, des=des, finition=finition, price=price, image=image, fuel=fuel, category=category
        )
        car.save()
        return render(request, 'cars.html' ,{'all' : all_cars} )
    return HttpResponse("Response")




def new2(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        Type = request.POST.get('Type')  
        category = request.POST.get('cate')
        Facade=request.POST.get('Facade')
        area = request.POST.get('Area')
        floor = request.POST.get('Floor')
        rooms = request.POST.get('Rooms')
        description = request.POST.get('Description')
        image = request.FILES.get('image')
        price = request.POST.get('Price')
        

        if image is None:
            pass
        
        house = House(
            location=location, Type=Type, area=area, floor=floor,
            rooms=rooms, description=description, facade=Facade, price=price, image=image, 
            category=category
        )
        house.save()
        messages.success(request, 'House added successfully')
        return redirect('im.html')
    return HttpResponse("Response")

def new4(request):
    if request.method == 'POST':
        brand = request.POST.get('Brand')
        model = request.POST.get('Model')  
        category = request.POST.get('cate')
        condition = request.POST.get('Condition')
        description = request.POST.get('Description')
        image = request.FILES.get('image')
        price = request.POST.get('Price')
        

        if image is None:
            pass
        
        accessory = Accessory(
            brand=brand, model=model, condition=condition, description=description
            , price=price, image=image, category=category
        )
        accessory.save()
        return redirect('acc.html')
    return HttpResponse("Response")

def new3(request):
    if request.method == 'POST':
        Brand = request.POST.get('Brand')
        model = request.POST.get('Model')  
        category = request.POST.get('cate')
        condition = request.POST.get('Condition')
        description = request.POST.get('Description')
        image = request.FILES.get('image')
        price = request.POST.get('Price')
        

        if image is None:
            pass
        
        home_appliance = Home_appliance(
            brand=Brand, model=model, condition=condition, description=description,
             price=price, image=image, category=category
        )
        home_appliance.save()
        return redirect('im.html')
    return HttpResponse("Response")



def new5(request):
    if request.method == 'POST':
        Brand = request.POST.get('Brand')
        Model = request.POST.get('Model')  
        category = request.POST.get('cate')
        Condition = request.POST.get('Condition')
        Description = request.POST.get('Description')
        image = request.FILES.get('image')
        price = request.POST.get('Price')
        

        if image is None:
            pass
        
        spar_parts = Spar_parts(
            brand=Brand, model=Model, condition=Condition, description=Description,
              price=price, image=image, category=category
        )
        spar_parts.save()
        return redirect('pie.html')
    return render(request, 'new5.html')

def new6(request):
    if request.method == 'POST':
        brand = request.POST.get('Brand')
        model = request.POST.get('Model')  
        category = request.POST.get('cate')
        size = request.POST.get('Size')
        condition = request.POST.get('Condition')
        description = request.POST.get('Description')
        image = request.FILES.get('image')
        price = request.POST.get('Price')

        

        if image is None:
            pass
        
        clothing =Clothing(
            brand=brand, model=model, size=size, condition=condition,
            description=description, price=price, image=image, category=category
        )
        clothing.save()
        return redirect('im.html')
    return render(request, 'new6.html')

def new7(request):
    if request.method == 'POST':
        Brand = request.POST.get('Brand')
        Model = request.POST.get('Model')  
        category = request.POST.get('cate')
        Processor = request.POST.get('Processor')
        Ram = request.POST.get('RAM')
        Rom = request.POST.get('ROM')
        Display = request.POST.get('Display')
        Graphic_card = request.POST.get('Graphic_card')
        Description = request.POST.get('Description')

        image = request.FILES.get('image')
        price = request.POST.get('Price')
        

        if image is None:
            pass
        
        laptop_phone = Laptop_phone(
            brand=Brand, model=Model, processor=Processor, ram=Ram,
            rom=Rom, display=Display, price=price, image=image, category=category
            , description=Description, graphic_card=Graphic_card
        )
        laptop_phone.save()
        return redirect('lap.html')
    return render(request, 'new7.html')



def about(request):
    return render(request,'ab.html')

def laptop(request):
    return render(request,'lap.html')

def accessories(request):
    return render(request,'acc.html')





def moderator_page(request):
    unapproved_posts = Car.objects.filter(approved=0)
    return render(request, 'moderator/mod1.html', {'unapproved_posts': unapproved_posts})

def approve_post(request, id):
        car = Car.objects.get(id=id)
        car.approved = True
        car.save()
        return redirect('mod')


def reject_post(request, id):
    
    post = Car.objects.get(id=id)
    post.delete()
    return redirect('mod.html')
