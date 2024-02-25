from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Koforidua'
    dest1.img = 'koforidua.jpg'
    dest1.desc = 'Your comfort zone'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Accra'
    dest2.img = 'accra.jpg'
    dest2.desc = 'The capital city for a reason'
    dest2.price = 1000

    dest3 = Destination()
    dest3.name = 'Kumasi'
    dest3.img = 'kumasi.jpg'
    dest3.desc = 'The Garden City'
    dest3.price = 850
    
    dests = [
        dest1, dest2, dest3
    ]

    return render(request, 'index.html', {'dests':dests})
