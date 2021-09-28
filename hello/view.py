from django.http import HttpResponse

def index(request):
    return HttpResponse("<marquee><h1>Hello World</h1></marquee>")