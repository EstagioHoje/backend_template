FROM python:3.9.0

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip 
COPY ./requirements.txt /usr/src/app    
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install net-tools

COPY . ./

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]