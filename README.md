## Project Name
    Instagram

## Description
This is a simple web clone of the instagram website. A user can create an account and sign into it. The site supports uploading images, and following other users. users can view photos uploaded by other users in the home page of app.

## BDD
- A user can create an account and sign into it. The site supports uploading images, users can view photos uploaded by other users in the home page of app,and user can comment on image.

## Set Up and Installations
#### Prerequisites
Ubuntu Software
Python3.6
Postgres
python virtualenv

## Clone the Repo
Run the following command on the terminal: git clone https://github.com/uwizeyeh/instagram && cd Instagram

## Activate virtual environment
Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## .env file
Create .env file and paste paste the following filling where appropriate:

- SECRET_KEY = '<Secret_key>'
- DBNAME = 'insta'
- USER = '<Username>'
- PASSWORD = '<password>'
- DEBUG = True

- EMAIL_USE_TLS = True
- EMAIL_HOST = 'smtp.gmail.com'
- EMAIL_PORT = 587
- EMAIL_HOST_USER = '<your-email>'
- EMAIL_HOST_PASSWORD = '<your-password>'

## Run initial Migration
python3.6 manage.py makemigrations gram
python3.6 manage.py migrate

## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql
## Link
* But is not work:instagra222.herokuapp.com

## Support and contact details
- Contact me on uwizeyimanahulde1@gmail.com
- Tel:0782356570

## License
Copyright (c) 2019
















































