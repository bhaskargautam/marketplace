#!/bin/bash

python tasks/manage.py migrate
python tasks/manage.py loaddata tasks/main/fixtures/initial_data.json
python manage.py collectstatic
