# Generated by Django 5.0.3 on 2024-04-11 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buybay_logic', '0002_alter_client_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='client',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
