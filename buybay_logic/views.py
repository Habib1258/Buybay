from django.shortcuts import render
from .models import  Client
from django.shortcuts import render, redirect

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

def new(request):
    return render(request,'new.html')

def about(request):
    return render(request,'ab.html')

def laptop(request):
    return render(request,'lap.html')

def accessories(request):
    return render(request,'acc.html')






