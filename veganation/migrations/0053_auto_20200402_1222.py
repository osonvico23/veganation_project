# Generated by Django 2.2.3 on 2020-04-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0052_auto_20200402_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, unique=True),
        ),
    ]