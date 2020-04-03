import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veganation_project.settings')
import django
django.setup()
from veganation.models import UserProfile, User
from django.core.files import File
import pandas as pd
from django.contrib.auth.hashers import make_password


#population script to load the users.
class Populate():
    def __init__(self):
        self.populate_myaccounts()

    def populate_myaccounts(self):
        #reading through myaccounts csv file

        path = os.path.join(os.getcwd(), 'myaccounts.csv')
        data = pd.read_csv(path)

        print(data)

        #loop trough the rows
        for ir in data.itertuples():

            #Connect the path for images
            imgpath = os.path.join(os.getcwd(), 'media', 'profile_images', str(ir[12]) + '.jpg')


            #creating the user
            user=User.objects.create(
                username = ir[1],
                email = ir[2],
                password = make_password(ir[3]),

            )

            #create myaccount object and save data to all the fields.
            profile = UserProfile.objects.create(user = user)
            profile.image.save(str(ir[12]), File(open(imgpath, 'rb')))
            profile.firstName = ir[4]
            profile.lastName = ir[5]
            profile.gender = ir[6]
            profile.veganSince = ir[7]
            profile.age = ir[8]
            profile.quote = ir[9]
            profile.occupation = ir[10]
            profile.city = ir[11]

            user.save()
            profile.save()

if __name__ == "__main__":
    Populate()
    
    
    
   