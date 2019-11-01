release: python tasks/manage.py migrate
release: python tasks/manage.py loaddata tasks/main/fixtures/initial_data.json
web: run-program waitress-serve --port=80 settings.wsgi:application