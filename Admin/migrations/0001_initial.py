# Generated by Django 4.0 on 2022-01-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_imei', models.PositiveIntegerField(max_length=15)),
                ('primary_sim', models.PositiveIntegerField(max_length=10)),
                ('secondary_sim', models.PositiveIntegerField(max_length=10)),
                ('firmware_option', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]