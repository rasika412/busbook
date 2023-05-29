# Generated by Django 4.1.4 on 2023-01-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Main_routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('bus_count', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('val', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='rout_detailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=100)),
                ('bus_type', models.CharField(max_length=100)),
                ('travel_hour', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('seating', models.CharField(max_length=100)),
                ('city_2', models.CharField(max_length=100)),
            ],
        ),
    ]
