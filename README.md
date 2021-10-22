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