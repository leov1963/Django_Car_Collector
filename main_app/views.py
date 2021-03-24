from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class Car:
    def __init__(self, name, make, model, description, year):
        self.name = name
        self.make = make
        self.model = model
        self.description = description
        self.year = year

cars = [
    Car('Foxy', 'Ford', 'fox-body mustang', 'angry little demon', 1987),
    Car('Little Dragon', 'Toyota', 'Celica gt-s', 'perfect 80s rust bucket', 1984),
    Car('Hell Camino', 'Chevy', 'el camino', 'Loud and dangerous', 1973)
]