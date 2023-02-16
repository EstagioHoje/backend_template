# SECRET_KEY='helloworld'
# DEBUG = True
# ROOT_URLCONF = __name__

# from django.conf.urls import url, path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Django na prática - Hello World!')
