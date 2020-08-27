# Commands

---
## Setup Virtual Environment
- Create virtual environment 
- => virtualenv venv
- Activate virtual environment 
- => source venv/bin/activate

## pip3 install *packages
- Install Django
- => pip3 install django
- => [OR] python -m pip install Django
- Know which package is installed
- => python -m django --version
- Install DRF
- => pip3 install djangorestframework
- [optional] Markdown support for the browsable API.
- => pip install markdown
- [optional] Filtering support
- => pip install django-filter

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


---
### Note: Some Useful Command's

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

---
- To open Interactive Console / Terminal
- => python3 manage.py shell

