#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install

python backend/manage.py collectstatic --no-input
python backend/manage.py migrate