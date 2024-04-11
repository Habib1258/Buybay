from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  

    class Meta:
          db_table = "User"

def __str__(self):
        return self.name
