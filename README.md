# How to execute this app?

- ## set up .env file in home directory

- ## upload images in face_upload/images/ folder
```sh
$ python face_upload/face_uploading.py
```

- ## execute kiosk app
```sh
$ python face_client/run.py
```

- ## access the home page to check visitors

# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.9.8 [installed in a virtual environment](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/AISVisioner/heroku-greeting-kiosk.git
$ cd heroku-greeting-kiosk

$ python3 -m venv venv
$ pip install -r requirements.txt

$ createdb greeting_kiosk

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
