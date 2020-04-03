# veganation_project
Welcome to VegaNation, the latest platform for vegan people to try out top-rated restaurants around Glasgow!
This application is for people who would like to visit new vegan places, but do not happen to have vegan friends (yet). 
VegaNation aims to create a supporting community amongst vegan people who dine together and might go to eco-conscious protests together by 
finding users new buddies!

This project has been created as part of the University of Glasgow course on Web Application Development by Orla Sonvico, Kamilla Kurta, 
Marzia Deodato and Sonali Bhaskar.

You can run the website on PythonAnywhere at the following link @..............
or follow the steps below to run it locally.

# Run veganation_project locally
Clone veganation_project repository and go through your command line to veganation_project source folder. Make sure to do the following:

>
    pip install -r requirements.txt

    python manage.py makemigrations veganation

    python manage.py migrate

You will have to delete db.sqlite3 before running the population script to avoid duplicates.

>
    python population_script.py
 
And now you are good to run the server

    python manage.py runserver
    
 And after navigating to http://127.0.0.1:8000/ you will be welcomed to our page!
 
 ![](media/homepage.png)
