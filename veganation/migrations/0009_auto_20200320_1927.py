# Generated by Django 2.2.1 on 2020-03-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0008_auto_20200320_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
