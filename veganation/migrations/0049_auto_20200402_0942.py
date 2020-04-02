# Generated by Django 2.2.1 on 2020-04-02 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0048_merge_20200402_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='myage',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='location',
            name='mygender',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='veganation@gmail.com', max_length=254),
        ),
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
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myaccount', to=settings.AUTH_USER_MODEL),
        ),
    ]