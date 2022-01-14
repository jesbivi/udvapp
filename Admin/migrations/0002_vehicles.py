# Generated by Django 4.0 on 2022-01-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=120)),
                ('brand', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120, unique=True)),
            ],
        ),
    ]