from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.


def home(request):
    return render(request, 'home.html')

def submit(request):
    return hr("submitted")
