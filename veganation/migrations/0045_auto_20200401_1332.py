# Generated by Django 2.2.1 on 2020-04-01 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0044_auto_20200401_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastName',
        ),
    ]