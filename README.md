# HealthDeck
A Patients Management System



## Setup
What you need for the Django dev environment:

- Python 3.9.0
- virtualenv
- Django 3.1.4
- Database (PostgreSQL)


To get this repository, run the following command inside your git enabled terminal
```bash
$ git clone https://github.com/sakhimpungose/HealthDeck.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

Via console/cmd `cd` to project folder (healthdeck) and create virtual environment and install requirements.txt
```bash
mkvirtualenv yourEnv

pip install -r requirements.txt
```



Create Database
```sql
CREATE DATABASE healthdeck;
```

You may also want to look at these settings inside settings.py
```python
...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthdeck',
        'USER': 'postgres', # You may also change this if you did not use the default postgres user
        'PASSWORD': '[your password]',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
...
```

If you don't have postgresql, you can also use the default settings
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ python manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
$ python manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. Start the server by following command

```bash
$ python manage.py runserver
```

Now that the server is live, here are some of the places you can browse:

- Admin login: [Admin](http://localhost:8000/admin)
- To login: [Login](http://localhost:8000/accounts/register)
- To add patient: [Add patient](http://localhost:8000/dashboard/patient/create)

Cheers and Happy Coding :)
