from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("index home page")


def home(request):
    
    return render(request, 'home.html')

def home2(request):
    return render(request, 'learn/home.html')
