# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "landingpage/index.html")

def indexfa(request):
    return render(request, "landingpage/indexfa.html")
