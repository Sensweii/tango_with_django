from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hey there partner!")

def about(request):
    return HttpResponse("Rango says this is about page.")
