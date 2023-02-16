# django-admin.py runserver --pythonpath=./src --settings=main

# chmod +x manage.py
# python3 manage.py migrate
# ./manage.py runserver

FILE=docker-compose.yml
docker-compose -f $FILE down
docker-compose -f $FILE build
docker-compose -f $FILE up