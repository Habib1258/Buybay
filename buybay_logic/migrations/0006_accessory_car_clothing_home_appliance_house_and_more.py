# Generated by Django 5.0.3 on 2024-04-14 00:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buybay_logic', '0005_alter_client_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('car', 'Car'), ('houses', 'Houses'), ('laptop_phone', 'Laptop & Phone'), ('clothing', 'Clothing'), ('accessories', 'Accessories'), ('home_appliance', 'Home Appliance'), ('spare_parts', 'Spare Parts')], max_length=20)),
                ('condition', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
            options={
                'db_table': 'buybay_logic_accessory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='clothing',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('car', 'Car'), ('houses', 'Houses'), ('laptop_phone', 'Laptop & Phone'), ('clothing', 'Clothing'), ('accessories', 'Accessories'), ('home_appliance', 'Home Appliance'), ('spare_parts', 'Spare Parts')], max_length=20)),
                ('size', models.IntegerField()),
                ('condition', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
            options={
                'db_table': 'buybay_logic_clothing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Home_appliance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('car', 'Car'), ('houses', 'Houses'), ('laptop_phone', 'Laptop & Phone'), ('clothing', 'Clothing'), ('accessories', 'Accessories'), ('home_appliance', 'Home Appliance'), ('spare_parts', 'Spare Parts')], max_length=20)),
                ('condition', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
            options={
                'db_table': 'buybay_logic_Home_appliance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('Type', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('car', 'Car'), ('houses', 'Houses'), ('laptop_phone', 'Laptop & Phone'), ('clothing', 'Clothing'), ('accessories', 'Accessories'), ('home_appliance', 'Home Appliance'), ('spare_parts', 'Spare Parts')], max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('facade', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'buybay_logic_house',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='laptop_phone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('car', 'Car'), ('houses', 'Houses'), ('laptop_phone', 'Laptop & Phone'), ('clothing', 'Clothing'), ('accessories', 'Accessories'), ('home_appliance', 'Home Appliance'), ('spare_parts', 'Spare Parts')], max_length=20)),
                ('processor', models.IntegerField()),
                ('ram', models.CharField(max_length=50)),
                ('rom', models.CharField(max_length=50)),
                ('graphic_card', models.CharField(max_length=20)),
                ('display', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
            options={
                'db_table': 'buybay_logic_laptop_phone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='spar_parts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('car', 'Car'), ('houses', 'Houses'), ('laptop_phone', 'Laptop & Phone'), ('clothing', 'Clothing'), ('accessories', 'Accessories'), ('home_appliance', 'Home Appliance'), ('spare_parts', 'Spare Parts')], max_length=20)),
                ('condition', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
            options={
                'db_table': 'buybay_logic_spar_parts',
                'managed': False,
            },
        ),
    ]