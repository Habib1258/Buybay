from django.shortcuts import render
from django.core.paginator import Paginator

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