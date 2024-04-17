from django.db import models

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
        return {self.nom, self.prenom, self.email, self.num_telephone}


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.CharField(max_length=1000000)
    category = models.CharField(max_length=20, null=False)
    approved = models.BooleanField(default=False)
    year = models.IntegerField()
    finition = models.CharField(max_length=50)
    engine = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    price = models.CharField(max_length=10000)
    des = models.CharField(max_length=1000)
    image = models.FileField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_car'

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} {self.fuel} {self.price} {self.des} {self.image} {self.engine} {self.mileage}"
    


class Accessory(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, null=False)
    approved = models.BooleanField(default=False)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)

    class Meta:  
        managed = False
        db_table = 'buybay_logic_accessory'

    def __str__(self):
        return f"{self.brand} {self.model} {self.condition} {self.description} {self.price} {self.image}"


class Spar_parts(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    approved = models.BooleanField(default=False)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=100000)
    image = models.ImageField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_spar_parts'

    def __str__(self):
        return f"{self.brand} {self.model} {self.condition} {self.description} {self.price} {self.image}"

class Home_appliance(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    approved = models.BooleanField(default=False)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_Home_appliance'

    def __str__(self):
        return f"{self.brand} {self.model} {self.condition} {self.description} {self.price} {self.image}"


class Clothing(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    approved = models.BooleanField(default=False)
    size = models.IntegerField()
    condition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=100000)
    image = models.ImageField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_clothing'

    def __str__(self):
        return f"{self.brand} {self.model} {self.condition} {self.description} {self.price} {self.size} {self.image}"


class Laptop_phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=category_choices)
    processor = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50)
    graphic_card = models.CharField(max_length=20)
    display = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'buybay_logic_laptop_phone'

    def __str__(self):
        return f"{self.brand} {self.model} {self.ram} {self.rom} {self.description} {self.display} {self.image} {self.price} {self.graphic_card} "
    


class House(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)  
    category = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    facade = models.IntegerField()
    rooms = models.IntegerField()
    floor = models.IntegerField()
    description = models.TextField()
    price = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='buybay_logic/images/')
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE , null=True)

    class Meta:
        managed = False
        db_table = 'buybay_logic_house'

    def __str__(self):
        return f"{self.Type} {self.location} {self.category} {self.area} {self.floor} {self.rooms} {self.facade} {self.image} {self.price}"
    


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)

    class Meta:
            managed = False
            db_table = 'buybay_logic_moderator'

    def __str__(self):
            return f"{self.title} {self.content} {self.published}"
