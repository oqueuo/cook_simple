Mobile |  Desktop
:-------------------------:|:-------------------------:
<img src="images/cook_simple_mobile.png" width="225">  |  <img src="images/cook_simple_desktop.png" width="600">

Application hosted at: https://oqueuo.pythonanywhere.com

If you'd like to just demo, log in with: User - guest, Password - guestguest

<h1>Cook Simple</h1>

If you're tired of finding a recipe online and having to scroll past 6 paragraphs of history before you get to the actual recipe, Cook Simple is perfect for you. 

With this minimalist recipe storage app, you can create, edit, and share recipes with none of the extra fluff. To get started, simply make an account and click the "+" on the top right to make a recipe. Once you're ready to cook, just pick one of the recipe cards and begin cooking!


<h2>Installation</h2>

Install dependencies:

> pip install -r requirements.txt

To run, the settings.py file needs a secret key. Generate one by entering the following into your terminal:

> python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

Assign the secret key by opening 'cook-simple-master/appmain/settings.py' and pasting your key as SECRET_KEY on line 23

Run the following command to start the application:

> python manage.py runserver
