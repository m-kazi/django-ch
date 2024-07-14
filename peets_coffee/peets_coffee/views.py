from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("<h1>Welcome to Peets Coffee Home Page!<h1>")
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")
