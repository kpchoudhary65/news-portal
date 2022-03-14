# [Django REST framework][docs]

# Requirements

* Python (3.6, 3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.0, 3.1, 3.2, 4.0)

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

## Setup

The first thing to do is to clone the repository:


```sh
$ git clone https://github.com/kpchoudhary65/news-portal.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ cd news_api
(env)$ pip install -r requirements.txt
```
## News API login first

* https://newsapi.org/

Got the API key and change view.py file API key 

```sh
API_KEY = 'YOUR_API_KEY'
```


## Docker


* https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04


## Postgresql DB Setup

* https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu

* https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'YOUR_USER_NAME',
        'NAME': 'YOUR_DB_NAME',
        'PASSWORD': 'YOUR_DB_PASSWORD',
        'HOST': "db",
        'PORT': '5432',
    }
}
```

## Once pip & Docker has finished downloading the dependencies:

```sh
(env)$ sudo service postgresql start 
(env)$ docker-compose run web python manage.py migrate
(env)$ docker-compose run web python manage.py createsuperuser
(env)$ docker-compose build
(env)$ docker-compose up
```

## API Testing Postman

```sh
http://127.0.0.1:8000/
```