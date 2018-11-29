#!/bin/bash

if [ "$1" == "makemigrations" ]; then
  rm app/migrations/00*.py
  python manage.py makemigrations
fi
mysql -uroot -e "DROP DATABASE preside"
mysql -uroot -e "CREATE DATABASE preside"
python manage.py migrate
python manage.py dbseed