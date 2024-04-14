from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


category_choices = [
        ('car', 'Car'),
        ('houses', 'Houses'),
        ('laptop_phone', 'Laptop & Phone'),
        ('clothing', 'Clothing'),
        ('accessories', 'Accessories'),
        ('home_appliance', 'Home Appliance'),
        ('spare_parts', 'Spare Parts'),
    ]


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    num_telephone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'client'

def __str__(self):
        return self.name


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.CharField(max_length=1000000)
    category = models.CharField(max_length=20, null=False)
    year = models.IntegerField()
    finition = models.CharField(max_length=50)
    engine = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    price = models.CharField(max_length=10000)
    des = models.CharField(max_length=1000)
    image = models.BinaryField()
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_car'

def __str__(self):
    return f"{self.brand} {self.model} ({self.year})"
    


class Accessory(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_accessory'

    def __str__(self):
        return f"{self.brand} {self.model}"


class spar_parts(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_spar_parts'

    def __str__(self):
        return f"{self.brand} {self.model}"

class Home_appliance(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_Home_appliance'

    def __str__(self):
        return f"{self.brand} {self.model}"


class clothing(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    size = models.IntegerField()
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_clothing'

    def __str__(self):
        return f"{self.brand} {self.model}"


class laptop_phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    processor = models.IntegerField()
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50)
    graphic_card = models.CharField(max_length=20)
    display = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_laptop_phone'

    def __str__(self):
        return f"{self.brand} {self.model}"
    
class House(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=100,validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
    Type = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    area = models.CharField(max_length=100)
    facade = models.IntegerField()
    rooms = models.IntegerField()
    floor = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_house'