from django.db import models

# Create your models here.



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
