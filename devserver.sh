#!/bin/sh
source .venv/bin/activate
pip freeze > mysite/requirements.txt
python mysite/manage.py runserver $PORT
