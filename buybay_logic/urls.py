from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name="buybay"),
    path('index.html',views.index, name="homepage"),
    path('cars.html',views.cars, name="cars"),
    path('profil.html',views.profil, name="profil"),
    path('an.html',views.an, name="an"),
    path('it.html',views.it, name="item"),
    path('item1.html',views.item, name="item1"),
    path('im.html',views.immobilier, name="immobilier"),
    path('lo.html',views.login, name="login"),
    path('pie.html',views.piece, name="piece"),
    path('si.html',views.sign, name="sign"),
    path('categorie.html',views.categorie, name="categorie"),
    path('mod.html',views.mod, name="mod1"),
    path('mod1.html',views.mod1, name=" mod"),
    path('cat_car.html',views.car_cat, name="car_cat"),
    path('model.html',views.model, name="model"),
    path('new.html',views.new, name="new"),
    path('ab.html',views.about, name="about"),
]

