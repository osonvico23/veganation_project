# Generated by Django 3.0.3 on 2020-03-19 11:26

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0004_auto_20200318_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
    ]
