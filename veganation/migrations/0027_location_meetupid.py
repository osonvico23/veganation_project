# Generated by Django 2.2.1 on 2020-03-31 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veganation', '0026_merge_20200331_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='meetupID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
