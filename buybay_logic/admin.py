from django.contrib import admin
from .models import Client,Car,Accessory,House,Home_appliance,spar_parts,laptop_phone,clothing

# Register your models here.
admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Accessory)
admin.site.register(House)
admin.site.register(Home_appliance)
admin.site.register(spar_parts)
admin.site.register(laptop_phone)
admin.site.register(clothing)