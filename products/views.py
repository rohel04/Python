from django.shortcuts import render
from django.http import HttpResponse as res

# Create your views here.
def index(request):
    return res("Welcome to first project")

def add(request):
    return res("Add products")