# views goes here

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango say Hello !!! <a href = '/rango/about'> About</a>")


def about(request):
    return HttpResponse("Rango says it is about page <a href = '/rango'>Index</a>")
