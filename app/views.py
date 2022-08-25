from re import template
from django.shortcuts import render

# Create your views here.

def Home(requests):
    template_name = "index.html"
    return render (requests , template_name)