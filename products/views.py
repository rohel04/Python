from itertools import product
from django.shortcuts import render
from django.http import HttpResponse as res
from .models import Product

# Create your views here.
def index(request):
    # return res("Welcome to first project")
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def add(request):
    return res("Add products")