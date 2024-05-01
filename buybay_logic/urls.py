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
    path('im.html',views.immobilier, name="immobilier"),
    path('lo.html',views.login, name="login"),
    path('pie.html',views.piece, name="piece"),
    path('si.html',views.sign, name="sign"),
    path('categorie.html',views.categorie, name="categorie"),
    path('mod.html',views.mod, name=" mod"),
    path('item_house.html',views.item_house, name="item_house"),
    path('item_home.html',views.item_home, name="item_home"),
    path('item_car.html',views.item_car, name="item_car"),
    path('item_lap.html',views.item_lap, name="item_lap"),
    path('item_accessory.html',views.item_accessory, name="item_accessory"),
    path('item_pie.html',views.item_pie, name="item_pie"),
    path('item_clothing.html',views.item_clothing, name="item_clothing"),
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
    path('mod.html', views.moderator_page, name='moderator_page'),
    path('approve/<int:id>/', views.approve_post, name='approve_post'),
    path('reject/<int:id>/', views.reject_post, name='reject_post'),
    path('mod.html', views.moderator_page, name='mod'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

