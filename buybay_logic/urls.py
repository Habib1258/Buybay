from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('lap.html',views.laptop, name="laptop"),
    path('acc.html',views.accessories, name="accessories"),
    path('cloth.html',views.clothing, name="clothing"),
    path('home.html',views.home, name="home"),
    path('new1.html',views.new1, name="new1"),
    path('new2.html',views.new2, name="new2"),
    path('new3.html',views.new3, name="new3"),
    path('new4.html',views.new4, name="new4"),
    path('new5.html',views.new5, name="new5"),
    path('new6.html',views.new6, name="new6"),
    path('new7.html',views.new7, name="new7"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

