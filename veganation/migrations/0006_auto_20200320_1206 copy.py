from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0020_remove_userprofile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='meetupID',
        ),
    ]
