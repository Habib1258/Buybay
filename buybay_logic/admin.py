from django.contrib import admin
from .models import Client,Car,Accessory,House,Home_appliance,Spar_parts,Laptop_phone,Clothing

# Register your models here.
admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Accessory)
admin.site.register(House)
admin.site.register(Home_appliance)
admin.site.register(Spar_parts)
admin.site.register(Laptop_phone)
admin.site.register(Clothing)