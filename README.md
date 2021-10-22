## Steps to run the application

### Update your pip (note: double dash in --upgrade)
> python3 -m pip install —upgrade pip

### Create a virtual environment
> python3 -m venv venv

### Install the virtual environment (Skip if you have)
> pip3 install virtualenv
### Activate the virtual environment
> source venv/bin/activate (mac/linux)

> . venv/bin/activate (mac/linux)

> venv\Scripts\activate (windows - command prompt)

```bash
Side note: To deactivate virtual environment, run:
deactivate
```

### To create Docker Image for our project
> docker-compose run web sh -c "django-admin startproject todolist ."

### To run the web application
> docker-compose up

### To access admin panel, first migrate and create a user...
> docker-compose run web sh -c "python manage.py makemigrations"

> docker-compose run web sh -c "python manage.py migrate"

> docker-compose run web sh -c "python manage.py createsuperuser"


### To start a todo application
> docker-compose run web sh -c "python manage.py startapp todo"


---
## Steps for deployment
Install environ into your project
> pip install environ

Add a `.env` file in the same directory as your settings.py and add the value `DJANGO_SECRET_KEY=`

Import the environ module and require it…
```bash
import environ
env = environ.Env()
# reading .env
environ.Env.read_env()
```

Copy the secret key and paste it inside the .env file
eg. `DJANGO_SECRET_KEY=34235ewea`

In `settings.py`, replace the secret key with:
> SECRET_KEY = env('DJANGO_SECRET_KEY')

Push all your installed dependencies into `requirements.txt`
> pip freeze > requirements.txt

Add `.env` in `.gitignore`

## You’re now ready to push to a github repo!!!

*****************
Sign up for an account at: [Python Anywhere](https://www.pythonanywhere.com/)
Choose the free beginner account
*****************
Dashboard > New console > Bash > Clone your repo and navigate inside it

Create a virtual environment
> mkvirtualenv --python=/usr/bin/python3.8 venv

Notes:
to exit virtual environment: `deactivate`
to enter virutal environment: `workon venv`

Check working directory
`pwd`

Take note of the working directory.

Head on to [Python Anywhere](https://www.pythonanywhere.com/) and login. Click on the Web link from the navigation bar and click add a new web app


## In configuration page:
---
Under Code, set the working directory: 
```bash
— /home/<your username>/<git repo name>
```
Under Virtualenv, add the virtualenv name: venv
Edit the WSGI configuration file
Use only the DJANGO section (delete the rest), uncomment it
Edit the following:
> path=‘<your pwd>’
> os.environ['DJANGO_SETTINGS_MODULE'] = 'todolist.settings'

Click save > Click the python icon on the left > Click on web > Click the reload button

Install all dependencies from requirements.txt
> pip install -r requirements.txt

Edit `settings.py` inside of todolist directory
```bash
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEBUG=False
ALLOWED_HOST = ['<your-account-name>.pythonanywhere.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Add a `.env` file in your projet directory (inside of todolist folder):
> echo "DJANGO_SECRET_KEY=your-secret-key" >> .env

Execute in project dir (/home/<your-account-name>/<your-repository-name>):
> python manage.py collectstatic