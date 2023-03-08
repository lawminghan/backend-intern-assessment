#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install
pipenv shell

python manage.py migrate