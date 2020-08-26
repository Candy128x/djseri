# Commands

---
## Setup Virtual Environment
- Create virtual environment 
- => virtualenv venv
- Activate virtual environment 
- => source venv/bin/activate

## pip3 install *packages
- => pip3 install django
- => [OR] python -m pip install Django
- => python -m django --version # Know which package is installed
- => pip3 install djangorestframework
- => [optional] pip install markdown       # Markdown support for the browsable API.
- => [optional] pip install django-filter  # Filtering support

## To Start, Work on Project 
- Create Project
- => django-admin startproject projdemo
- Create App
- => cd projdemo/
- Note: App name must be in plural
- => django-admin startapp employees

## install packages
- => cd projdemo
- => pip3 freeze > requirements.txt
- To install package dependency
- => pip3 install -r requirements.txt

- => pip3 install psycopg2
- => pip3 install psycopg2-binary
- => pip3 install python-decouple


**Note**

---
- check django version
- => django-admin --version

---
- make project
- => django-admin startproject projdemo

---
- make app
- => python3 manage.py startapp home

---
- => python3 manage.py makemigrations
- => python3 manage.py migrate

---
- create super user
- => python3 manage.py createsuperuser

