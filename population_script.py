import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veganation_project.settings')
import django
django.setup()
from veganation.models import Rate

def populate():
    restaurants = [
        {'name': 'Picnic'},
        {'name': 'Serenity Now'},
        {'name': 'Mono'},
        {'name': 'Hug and Pint'},
        {'name': 'Puti Vegan Cafe'},
        {'name': 'The Glasvegan'},
        {'name': 'The V&V Cafe'},
        {'name': 'The 78'} ]

def add_restaurant(name):
    r = Rate.objects.get_or_create(name=name)[0]
    r.save()
    return r

if __name__=='__main__':
    print('Starting Veganation population script...')
    populate()